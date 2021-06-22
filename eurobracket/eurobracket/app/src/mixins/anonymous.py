from django.http import HttpResponseRedirect


class AnonymousRequiredMixin:
    redirect_url = None

    """Verify that the current user is anonymous."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_anonymous:
            return HttpResponseRedirect(self.redirect_url)
        return super().dispatch(request, *args, **kwargs)