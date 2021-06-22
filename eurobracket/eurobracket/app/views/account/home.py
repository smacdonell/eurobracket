from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import logging


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    #redirect_url = '/'
    #required_state = 'PICKS_NEEDED'
    template_name = 'account/home.html'
    logger = logging.getLogger('logger')

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
