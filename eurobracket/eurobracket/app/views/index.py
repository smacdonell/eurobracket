from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from eurobracket.app.forms.account_forms import LoginForm
from eurobracket.app.forms.account_forms import CreateAccountForm
import logging


class IndexView(TemplateView):
    template_name = 'index/index.html'
    logger = logging.getLogger('logger')

    """
     Constructs the forms and objects needed for the splash page 
    """
    def construct_context(self, request, *args, **kwargs):
        if request.method == 'GET':
            login_form = LoginForm()
            create_account_form = CreateAccountForm()
        else:
            login_form = LoginForm(request.POST)
            create_account_form = CreateAccountForm(request.POST)

        model = {
            'login_form': login_form,
            'create_account_form': create_account_form
        }

        return model

    def get(self, request, *args, **kwargs):
        context = self.construct_context(request, *args, **kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.logger.info(request.POST)

        login_form = LoginForm(request.POST)
        create_account_form = CreateAccountForm(request.POST)

        #context = self.construct_context(request, *args, **kwargs)
        context = {}

        if 'login' in request.POST:
            login_form = LoginForm(request.POST)
            create_account_form = CreateAccountForm()

            if login_form.is_valid():
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                context['user'] = user
        elif 'create_account' in request.POST:
            login_form = LoginForm()
            create_account_form = CreateAccountForm(request.POST)

            if create_account_form.is_valid():
                user = User.objects.create_user(request.POST['username'], request.POST['password'])
                context['user'] = user

        context['login_form'] = login_form
        context['create_account_form'] = create_account_form

        return render(request, self.template_name, context)
