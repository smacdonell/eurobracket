from django.views.generic import RedirectView
from django.shortcuts import render, redirect
from django.contrib.auth import logout
import logging


class LogoutView(RedirectView):
    logger = logging.getLogger('eurobracket')

    def get(self, request, *args, **kwargs):
        logout(request)
        self.logger.info(request, 'Logged out user')
        return redirect("/")
