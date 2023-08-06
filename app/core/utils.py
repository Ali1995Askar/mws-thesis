from functools import wraps
from django.shortcuts import redirect


def prevent_logged_in(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)

    return _wrapped_view
