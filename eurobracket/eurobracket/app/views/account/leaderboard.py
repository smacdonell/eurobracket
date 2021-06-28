import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from eurobracket.app.models import Prediction, UserState, UserStateRel


class LeaderboardView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    template_name = 'account/leaderboard.html'
    logger = logging.getLogger('eurobracket')

    def get(self, request, *args, **kwargs):
        made_rel = UserStateRel.objects.filter(state=UserState.objects.get(state='PICKS_MADE'))
        user_scores = []
        for rel in made_rel:
            score = 0
            user_preds = Prediction.objects.filter(user=rel.user)
            for pred in user_preds:
                if pred.game.game_happened and pred.winning_team == pred.game.winning_team:
                    score += pred.game.round.points
            user_scores.append({
                'user': rel.user,
                'score': score
            })

        user_scores.sort(key=lambda x: x['score'], reverse=True)

        context = {
            'users': user_scores
        }
        return render(request, self.template_name, context)