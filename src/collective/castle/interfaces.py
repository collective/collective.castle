from zope import schema
from zope.interface import Interface

from Products.CMFPlone import PloneMessageFactory as _


class ICAS4PASPluginSchema(Interface):

    login_url = schema.TextLine(
        title=_(u"CAS Log in URL"),
        description=_(u"The absolute URL for CAS log in."),
        default=u"https://your.cas.server:port/cas/login",
        required=True)

    logout_url = schema.TextLine(
        title=_(u"CAS Log out URL"),
        description=_(u"The absolute URL for CAS log out."),
        default=u"https://your.cas.server:port/cas/logout",
        required=True)

    validate_url = schema.TextLine(
        title=_(u"CAS Validate URL"),
        description=_(u"The absolute URL for CAS validation."),
        default=u"https://your.cas.server:port/cas/validate",
        required=True)

    session_var = schema.TextLine(
        title=_(u"Session Variable"),
        description=_(u"The identifier for the session cookie in use."),
        default=u"__ac",
        required=True)

    use_ACTUAL_URL = schema.Bool(
        title=_(u"Use Actual URL"),
        description=_(u""),
        required=True)

    users_require_role = schema.Bool(
        title=_(u"Users Require Role"),
        description=_(u"If enabled, users require a role on the portal"
                      u" in order to be authenticated. If disabled, all users"
                      u" authenticating via CAS are allowed."),
        default=False,
        required=True)


