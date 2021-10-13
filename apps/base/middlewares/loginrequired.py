'''Custom login required middleware
add the following into `settings.py` in order to:
LOGIN_REQUIRED_IGNORE_PATHS:
    list of url-paths that most be ignored by this middleware, e.g: login/
LOGIN_REQUIRED_IGNORE_VIEW_NAMES:
    list of view-names that most be ignored by this middleware, e.g: login_view
'''
import re

from django.conf import settings
from django.contrib.auth.middleware import AuthenticationMiddleware
from django.shortcuts import redirect
from django.urls import resolve
from django.urls import reverse

IGNORE_PATHS = [re.compile(settings.LOGIN_URL)]

IGNORE_PATHS += [re.compile(url)
                 for url in getattr(settings,
                 'LOGIN_REQUIRED_IGNORE_PATHS', [])
                 ]

IGNORE_VIEW_NAMES = list(getattr(settings,
                                 'LOGIN_REQUIRED_IGNORE_VIEW_NAMES', []))


class LoginRequiredMiddleware(AuthenticationMiddleware):
    '''A subclass of AuthenticationMiddleware
        processes all requests that are not ignored
    '''

    def process_view(self, request, *args, **kwargs):
        '''Main function to check requests
            redirects unauthenticated users to login url
        '''
        if not request.user.is_authenticated:

            path = request.path
            resolver = resolve(path)
            path_in_ignored_pathes = any(url.match(path)
                                         for url in IGNORE_PATHS)
            path_in_ignored_views = any(name == resolver.view_name
                                        for name in IGNORE_VIEW_NAMES)

            if not path_in_ignored_views and not path_in_ignored_pathes:
                return redirect('{}?next={}'.format(
                    reverse(settings.LOGIN_URL),
                    request.path))
