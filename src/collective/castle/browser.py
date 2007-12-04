from zope.publisher.browser import BrowserPage
from Products.CMFCore.utils import getToolByName
from zExceptions import NotFound
from urllib import quote


def URL(context):
    return context.restrictedTraverse('@@plone').getCurrentUrl()

class LoginUrl(BrowserPage):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        base = self.loginURL()
        if base is None:
            raise NotFound
        return '%s%s' % (base, self.loginQueryString())

    def loginURL(self):
        acl_users = getToolByName(self.context, 'acl_users')
        cas_auth_helpers = acl_users.objectValues(['CAS Auth Helper'])
        if cas_auth_helpers:
            return cas_auth_helpers[0].getLoginURL()
        else:
            return None

    def loginQueryString(self):
        quoted_here_url = mtool = quote(URL(self.context), '')
        querystring = '?came_from=%s' % quoted_here_url
        portal = URL(getToolByName(self.context, 'portal_url').getPortalObject())
        if portal[-1:] == '/':
            portal = portal[:-1]
        service_URL =('%s/logged_in%s' % (portal, querystring))
        return '?service=%s' % quote(service_URL, '')

class Logout(BrowserPage):

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        mt = getToolByName(self.context, 'portal_membership')
        mt.logoutUser(REQUEST=self.request)
        #if self.request.has_key('portal_skin'):
        #    self.context.portal_skins.clearSkinCookie()
        #self.request.RESPONSE.expireCookie('__ac', path='/')
        portal = getToolByName(self.context, 'portal_url').getPortalObject().absolute_url()
        return self.request.RESPONSE.redirect(portal)
