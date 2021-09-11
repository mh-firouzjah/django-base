from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class SessionExpiryMiddleware(MiddlewareMixin):
    """ Set the session expiry according to settings SESSION_EXPIRY"""

    def process_request(self, request):
        if getattr(settings, 'SESSION_EXPIRY', None):
            request.session.set_expiry(settings.SESSION_EXPIRY)
        return None
