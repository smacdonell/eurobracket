from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import logging

from eurobracket.app.models import Team, TeamStatus
from eurobracket.app.src.mixins.user_has_state import UserHasStateMixin


class MakePicksView(LoginRequiredMixin, UserHasStateMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    auth_redirect_url = '/account/home/'
    anon_redirect_url = '/'
    required_state = 'PICKS_NEEDED'
    template_name = 'account/makepicks.html'
    logger = logging.getLogger('logger')

    def get(self, request, *args, **kwargs):
        active_teams_statuses = TeamStatus.objects.filter(active=True)
        teams = list(map(lambda x: x.team, active_teams_statuses))

        context = {
            'active_teams': teams
        }

        return render(request, self.template_name, context)
