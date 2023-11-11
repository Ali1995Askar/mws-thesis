import pydoc
from functools import wraps
from django.shortcuts import redirect


def prevent_logged_in(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request, *args, **kwargs)

    return _wrapped_view


def my_import(object_path: str, ignore_errors: bool = False):
    if object_path is None and ignore_errors:
        return
    object_path = object_path.replace('/', '.')
    obj = pydoc.locate(object_path)
    return obj
