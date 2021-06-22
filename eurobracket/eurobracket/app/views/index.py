from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from eurobracket.app.forms.account_forms import LoginForm
from eurobracket.app.forms.account_forms import CreateAccountForm
import logging

from eurobracket.app.models import UserStateRel, UserState
from eurobracket.app.src.mixins.anonymous import AnonymousRequiredMixin


class IndexView(AnonymousRequiredMixin, TemplateView):
    redirect_url = 'account/makepicks/'
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
            if 'login' in request.POST:
                login_form = LoginForm(request.POST)
                create_account_form = CreateAccountForm()
            else:
                login_form = LoginForm()
                create_account_form = CreateAccountForm(request.POST)

        model = {
            'login_form': login_form,
            'create_account_form': create_account_form,
            'user': request.user
        }

        return model

    def get(self, request, *args, **kwargs):
        context = self.construct_context(request, *args, **kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        self.logger.info(request.POST)

        context = self.construct_context(request, *args, **kwargs)
        login_form = context['login_form']
        create_account_form = context['create_account_form']

        if 'login' in request.POST:
            if login_form.is_valid():
                user = authenticate(username=request.POST['username'], password=request.POST['password'])
                if user is not None:
                    login(request, user)
                    context['user'] = user
        elif 'create_account' in request.POST:
            if create_account_form.is_valid():
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'],
                    first_name=request.POST['first_name'], last_name=request.POST['last_name'])
                UserStateRel.objects.create(user=user, state=UserState.objects.get(state='PICKS_NEEDED'))

                if user is not None:
                    login(request, user)
                    context['user'] = user

        try :
            if user.is_authenticated:
                return HttpResponseRedirect(self.redirect_url)
        except NameError as e:
            self.logger.warning(e)

        return render(request, self.template_name, context)
