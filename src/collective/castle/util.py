# -*- coding: utf-8 -*-

from Products.CMFCore.utils import getToolByName
from urllib import quote, unquote
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
    quoted_here_url = quote(unquote(URL(context)), '')
    portal = getToolByName(context, 'portal_url')()
    if portal[-1:] == '/':
        portal = portal[:-1]
    # retrieve correct came_from from url
    splitted = quoted_here_url.split('came_from%3D')
    if len(splitted) > 1:
        quoted_here_url = splitted[-1]
    querystring = '?came_from=%s' % quoted_here_url
    service_URL = ('%s/logged_in%s' % (portal, querystring))
    return '?service=%s' % quote(service_URL, '')


def login_URL(context):
    base = login_URL_base(context)
    if base is None:
        request = context.REQUEST
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

    #if request.has_key('portal_skin'):
    #    context.portal_skins.clearSkinCookie()
    #request.RESPONSE.expireCookie('__ac', path='/')

    session = request.SESSION
    if p.session_var in session.keys():
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
        '%s?service=%s' % (p.logout_url, portal)
    )
