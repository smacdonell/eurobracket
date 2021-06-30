import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView

from eurobracket.app.models import UserStateRel, Prediction, Round
from eurobracket.app.src.mixins.user_has_state import UserHasStateMixin


class UserPredictionsView(LoginRequiredMixin, UserHasStateMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    auth_redirect_url = '/account/home/'
    anon_redirect_url = '/'
    required_state = 'PICKS_MADE'
    template_name = 'predictions/user.html'
    logger = logging.getLogger('eurobracket')

    def get(self, request, *args, **kwargs):
        user_id = int(self.kwargs['id'])
        user = None
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            self.logger.info("No user for ID: {}".format(user_id))
            return HttpResponseRedirect(self.auth_redirect_url)

        user_state_rel = UserStateRel.objects.get(user=user)
        if user_state_rel is None or user_state_rel.state.state == 'PICKS_NEEDED':
            return HttpResponseRedirect(self.auth_redirect_url)

        predictions = {
            'ROUND_OF_SIXTEEN': Prediction.objects.filter(user=user, round=Round.objects.get(ref_code='ROUND_OF_SIXTEEN')),
            'QUARTER_FINALS': Prediction.objects.filter(user=user, round=Round.objects.get(ref_code='QUARTER_FINALS')),
            'SEMI_FINALS': Prediction.objects.filter(user=user, round=Round.objects.get(ref_code='SEMI_FINALS')),
            'FINALS': Prediction.objects.filter(user=user, round=Round.objects.get(ref_code='FINALS'))
        }

        score = 0
        for pred in Prediction.objects.filter(user=user):
            if pred.game.game_happened and pred.winning_team_id == pred.game.winning_team_id:
                score += pred.game.round.points

        context = {
            'user': user,
            'predictions': predictions,
            'score': score
        }

        return render(request, self.template_name, context)
