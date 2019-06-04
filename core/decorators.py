from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.urls import reverse


def register_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.register_completed():
            return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('register'))

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__

    return wrap
