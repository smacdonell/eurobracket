from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import logging
import random

from eurobracket.app.models import Prediction, Round


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    template_name = 'account/home.html'
    logger = logging.getLogger('eurobracket')

    def get(self, request, *args, **kwargs):
        predictions = {
            'ROUND_OF_SIXTEEN': Prediction.objects.filter(user=request.user, round=Round.objects.get(ref_code='ROUND_OF_SIXTEEN')),
            'QUARTER_FINALS': Prediction.objects.filter(user=request.user, round=Round.objects.get(ref_code='QUARTER_FINALS')),
            'SEMI_FINALS': Prediction.objects.filter(user=request.user, round=Round.objects.get(ref_code='SEMI_FINALS')),
            'FINALS': Prediction.objects.filter(user=request.user, round=Round.objects.get(ref_code='FINALS'))
        }

        score = 0
        for pred in Prediction.objects.filter(user=request.user):
            if pred.game.game_happened and pred.winning_team_id == pred.game.winning_team_id:
                score += pred.game.round.points

        context = {
            'predictions': predictions,
            'score': score
        }
        return render(request, self.template_name, context)
