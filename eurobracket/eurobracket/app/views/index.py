from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
import logging


class IndexView(TemplateView):
    template_name = 'index/index.html'
    logger = logging.getLogger('logger')

    """
     Constructs the forms and objects needed for the splash page 
    """
    def construct_context(self, request, *args, **kwargs):
        model = {
            'test': 'value'
        }

        return model

    def get(self, request, *args, **kwargs):
        context = self.construct_context(request, *args, **kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.logger.info(request.POST)

        context = self.construct_context(request, *args, **kwargs)
        return render(request, self.template_name, context)


