

from django.http import HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from django.contrib import auth
from re import compile
from accounts.models import User

EXEMPT_URLS = [compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [compile(expr) for expr in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if not request.user.is_authenticated():
            path = request.path_info.lstrip('/')
            if not any(m.match(path) for m in EXEMPT_URLS):
                raise Http404("Not Authenticated to view this Page")
        return response

    # def process_request(self, request):
    #     assert hasattr(request, 'user'), "The Login Required middleware\
    #     requires authentication middleware to be installed. Edit your\
    #     MIDDLEWARE_CLASSES setting to insert\
    #     'django.contrib.auth.middlware.AuthenticationMiddleware'. If that doesn't\
    #     work, ensure your TEMPLATE_CONTEXT_PROCESSORS setting includes\
    #     'django.core.context_processors.auth'."
    #     response = get_response(request)
    #     if not response.user.is_authenticated():
    #         path = response.path_info.lstrip('/')
    #         if not any(m.match(path) for m in LOGIN_EXEMPT_URLS):
    #             return HttpResponseRedirect(settings.LOGIN_URL)