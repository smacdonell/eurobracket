from django.shortcuts import render

"""
Custom error response handlers to delegate to the error views in the /templates/error directory.
"""


def error_400(request, exception):
    return render(request, 'error/400.html', {})


def error_403(request, exception):
    return render(request, 'error/403.html', {})


def error_404(request, exception):
    return render(request, 'error/404.html', {})


def error_500(request, exception=None):
    return render(request, 'error/500.html', {})
