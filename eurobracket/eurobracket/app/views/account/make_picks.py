from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import logging
import json

from eurobracket.app.forms.prediction_forms import *
from eurobracket.app.models import Team, TeamStatus, Game, Prediction, Round, GameRel, UserStateRel, UserState
from eurobracket.app.src.mixins.user_has_state import UserHasStateMixin


class MakePicksView(LoginRequiredMixin, UserHasStateMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    auth_redirect_url = '/account/home/'
    anon_redirect_url = '/'
    required_state = 'PICKS_NEEDED'
    template_name = 'account/makepicks.html'
    logger = logging.getLogger('eurobracket')

    def construct_context(self, request):
        user = request.user
        predictions = Prediction.objects.filter(user=user)
        current_round = None
        for p in predictions:
            if current_round is None:
                current_round = p.game.round

            if p.game.round.id > current_round.id:
                current_round = p.game.round

        if current_round is None:
            current_round = Round.objects.get(ref_code='ROUND_OF_SIXTEEN')
        else:
            current_round = Round.objects.get(id=(current_round.id+1))

        games = Game.objects.filter(round=current_round)
        pred_games = []
        for game in games:
            game_rel = GameRel.objects.filter(game=game)
            if current_round.ref_code == 'ROUND_OF_SIXTEEN':
                pred_games.append({
                    'game': game,
                    'team_one': game.team_one,
                    'team_two': game.team_two
                })
            else:
                pred_games.append({
                    'game': game,
                    'team_one': predictions.filter(game=game_rel[0].prev_game_one)[0].winning_team,
                    'team_two': predictions.filter(game=game_rel[0].prev_game_two)[0].winning_team
                })

        context = {
            'games': games,
            'predictions': predictions,
            'current_round': current_round,
            'pred_games': pred_games
        }

        return context

    def get(self, request, *args, **kwargs):
        context = self.construct_context(request)

        context['form'] = PredictionForm()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.logger.info(request.POST)

        user = request.user
        predictions = PredictionForm(request.POST)
        if predictions.is_valid():
            pred_data = json.loads(predictions.data['pred_data'])
            current_round = Round.objects.get(ref_code=pred_data['round'])
            for game_id in pred_data['games']:
                winning_team_id = pred_data['games'][game_id]['winner']
                losing_team_id = pred_data['games'][game_id]['loser']
                Prediction.objects.create(user=request.user,
                                          game=Game.objects.get(pk=game_id),
                                          winning_team=Team.objects.get(pk=winning_team_id),
                                          losing_team=Team.objects.get(pk=losing_team_id), round=current_round)

            if current_round.ref_code == 'FINALS':
                user_state = UserStateRel.objects.get(user=user)
                user_state.state = UserState.objects.get(state='PICKS_MADE')
                user_state.save()
                return HttpResponseRedirect('/account/home')
            else:
                return HttpResponseRedirect('/account/makepicks')

        context = self.construct_context(request)
        context['form'] = predictions
        return render(request, self.template_name, context)
