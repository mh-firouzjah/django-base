import re

from django.conf import settings
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.shortcuts import redirect
from django.urls import resolve, reverse

IGNORE_PATHS = [re.compile(settings.LOGIN_URL)]

IGNORE_PATHS += [re.compile(url)
                 for url in getattr(settings,
                 'LOGIN_REQUIRED_IGNORE_PATHS', [])
                 ]

IGNORE_VIEW_NAMES = [
    name for name in getattr(settings, 'LOGIN_REQUIRED_IGNORE_VIEW_NAMES', [])
]


class LoginRequiredMiddleware(AuthenticationMiddleware):
    def process_view(self, request, *args, **kwargs):
        path = request.path
        if request.user.is_authenticated:
            return

        resolver = resolve(path)
        views = ((name == resolver.view_name) for name in IGNORE_VIEW_NAMES)

        if not any(views) and not any(url.match(path) for url in IGNORE_PATHS):
            return redirect('{}?next={}'.format(reverse('admin:login'),
                                                request.path))
