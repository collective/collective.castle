from Products.CMFCore.utils import getToolByName
from zExceptions import NotFound
from urllib import quote
from Products.statusmessages.interfaces import IStatusMessage
from collective.castle import CastleMessageFactory as _

def URL(context):
    return context.restrictedTraverse('@@plone').getCurrentUrl()

def get_cas_plugin(context):
    acl_users = getToolByName(context, 'acl_users')
    cas_auth_helpers = acl_users.objectValues(['CAS Auth Helper'])
    if cas_auth_helpers:
        return cas_auth_helpers[0]

def login_URL_base(context):
    p = get_cas_plugin(context)
    if p:
        return p.getLoginURL()

def login_query_string(context): 
    quoted_here_url = mtool = quote(URL(context), '')
    querystring = '?came_from=%s' % quoted_here_url
    portal = URL(getToolByName(context, 'portal_url').getPortalObject())
    if portal[-1:] == '/':
        portal = portal[:-1]
    service_URL =('%s/logged_in%s' % (portal, querystring))
    return '?service=%s' % quote(service_URL, '')

def login_URL(context):
    base = login_URL_base(context)
    if base is None:
        request = context.request
        IStatusMessage(request).addStatusMessage(
            _(u"CAS Login is not available. Please configure CAS"), 
            type="warning"
        )
        return None
    return '%s%s' % (base, login_query_string(context))

def logout(context, request):
    mt = getToolByName(context, 'portal_membership')
    p = get_cas_plugin(context)
    # forget user on logout
    mt.logoutUser(REQUEST=request)
    session = request.SESSION
    if session.has_key(p.session_var):
        session[p.session_var] = None
    # let cas finnish the logout
    portal = quote(
        getToolByName(
            context, 'portal_url'
        ).getPortalObject().absolute_url()
    )
    IStatusMessage(request).addStatusMessage(
        _(u'You are now logged out.'), 
        type='info'
    ) 
    return request.RESPONSE.redirect( 
        '%s?url=%s' % (p.logout_url, portal)
    )
