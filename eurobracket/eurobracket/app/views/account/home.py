from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
import logging
import random


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = '/'
    redirect_field_name = '/'
    template_name = 'account/home.html'
    messages = [
        'Wow, those are some bad picks',
        'Those might be the worst picks I\'ve ever seen',
        'Well, you\'re definitely losing now',
        'Those predictions are incredibly stupid',
        'Yikes, good luck with those terrible picks'
    ]
    logger = logging.getLogger('logger')

    def get(self, request, *args, **kwargs):
        context = {
            'message': self.messages[random.randint(0, 4)]
        }
        return render(request, self.template_name, context)
