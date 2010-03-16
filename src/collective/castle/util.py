from Products.CMFCore.utils import getToolByName
from urllib import quote
from Products.statusmessages.interfaces import IStatusMessage
#from zExceptions import NotFound


def URL(context):
    return context.restrictedTraverse('@@plone').getCurrentUrl()


def login_URL_base(context):
    acl_users = getToolByName(context, 'acl_users')
    cas_auth_helpers = acl_users.objectValues(['CAS Auth Helper'])
    if cas_auth_helpers:
        return cas_auth_helpers[0].getLoginURL()
    else:
        return None


def login_query_string(context):
    quoted_here_url = mtool = quote(URL(context), '')
    querystring = '?came_from=%s' % quoted_here_url
    portal = getToolByName(context, 'portal_url')()
    if portal[-1:] == '/':
        portal = portal[:-1]
    service_URL =('%s/logged_in%s' % (portal, querystring))
    return '?service=%s' % quote(service_URL, '')


def login_URL(context):
    base = login_URL_base(context)
    if base is None:
        request = context.request
        IStatusMessage(request).addStatusMessage(u"CAS Login is not available. \
            Please configure CAS ", type="warning")
        return None
    return '%s%s' % (base, login_query_string(context))


def logout(context, request):
    mt = getToolByName(context, 'portal_membership')
    mt.logoutUser(REQUEST=request)
    #if request.has_key('portal_skin'):
    #    context.portal_skins.clearSkinCookie()
    #request.RESPONSE.expireCookie('__ac', path='/')
    IStatusMessage(request).addStatusMessage(u'You are now logged out.',
        type='info') # XXX TODO: i18n the actual message
    portal = getToolByName(context, 'portal_url').getPortalObject().absolute_url()
    return request.RESPONSE.redirect(portal)

