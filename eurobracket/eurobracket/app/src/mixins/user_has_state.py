from django.http import HttpResponseRedirect

from eurobracket.app.models import UserStateRel


class UserHasStateMixin:
    auth_redirect_url = None
    anon_redirect_url = None
    required_state = None

    """Verify that the current user has state ."""
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_rel = UserStateRel.objects.get(user=request.user)
            if user_rel.state.state == self.required_state:
                return super().dispatch(request, *args, **kwargs)
            else:
                return HttpResponseRedirect(self.auth_redirect_url)
        return HttpResponseRedirect(self.anon_redirect_url)
