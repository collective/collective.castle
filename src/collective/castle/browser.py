from zope.publisher.browser import BrowserPage
from collective.castle import util


class LoginUrl(BrowserPage):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        return util.login_URL(self.context)


class Logout(BrowserPage):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        util.logout(self.context, self.request)
