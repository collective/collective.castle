from StringIO import StringIO

from zope.interface import Interface
from zope.interface import implements

from zope.component import adapts

from zope.schema import TextLine
from zope.schema import Bool

from zope.formlib import form

from Products.CMFCore.utils import getToolByName

from Products.CMFPlone import PloneMessageFactory as _
from Products.CMFPlone.interfaces import IPloneSiteRoot

from Products.PlonePAS.Extensions.Install import activatePluginInterfaces

from plone.fieldsets.form import FieldsetsEditForm
from plone.app.controlpanel.interfaces import IPloneControlPanelForm

from Products.statusmessages.interfaces import IStatusMessage

from rwproperty import getproperty
from rwproperty import setproperty


class ICAS4PASPluginSchema(Interface):

    login_url = TextLine(
        title=_(u"CAS Log in URL"),
        description=_(u""),
        required=True)

    logout_url = TextLine(
        title=_(u"CAS Log out URL"),
        description=_(u""),
        required=True)

    validate_url = TextLine(
        title=_(u"CAS Validate URL"),
        description=_(u""),
        required=True)

    session_var = TextLine(
        title=_(u"Session Variable"),
        description=_(u""),
        required=True)

    use_ACTUAL_URL = Bool(
        title=_(u"Use Actual URL"),
        description=_(u""),
        required=True)


class CASSettingsAdapter(object):

    implements(ICAS4PASPluginSchema)
    adapts(IPloneSiteRoot)

    def __init__(self, context):
        url_tool = getToolByName(context, 'portal_url')
        portal = url_tool.getPortalObject()
        acl_users = portal.acl_users
        cas_auth_helpers = acl_users.objectValues(['CAS Auth Helper'])
        if not cas_auth_helpers:
            cas = acl_users.manage_addProduct['CAS4PAS']
            cas.addCASAuthHelper('cas', 'CAS Auth Helper')
            cas.login_url = 'https://your.cas.server:port/cas/login'
            cas.logout_url = 'https://your.cas.server:port/cas/logout'
            cas.validate_url = 'https://your.cas.server:port/cas/validate'
            cas.session_var = '__ac'
            cas.use_ACTUAL_URL = True
            out = StringIO()
            activatePluginInterfaces(portal, 'cas', out)
            msg = 'Created CAS plugin. %s' % out.getvalue()
            IStatusMessage(context.request).addStatusMessage(msg, 'info')
        else:
            cas = cas_auth_helpers[0]
        self.cas = cas

    @getproperty
    def login_url(self):
        return self.cas.login_url

    @setproperty
    def login_url(self, login_url):
        self.cas.login_url = login_url

    @getproperty
    def logout_url(self):
        return self.cas.logout_url

    @setproperty
    def logout_url(self, logout_url):
        self.cas.logout_url = logout_url

    @getproperty
    def validate_url(self):
        return self.cas.validate_url

    @setproperty
    def validate_url(self, validate_url):
        self.cas.validate_url = validate_url

    @getproperty
    def session_var(self):
        return self.cas.session_var

    @setproperty
    def session_var(self, session_var):
        self.cas.session_var = session_var

    @getproperty
    def use_ACTUAL_URL(self):
        return self.cas.use_ACTUAL_URL

    @setproperty
    def use_ACTUAL_URL(self, use_ACTUAL_URL):
        self.cas.use_ACTUAL_URL = use_ACTUAL_URL


class CASControlPanel(FieldsetsEditForm):

    implements(IPloneControlPanelForm)

    form_fields = form.FormFields(ICAS4PASPluginSchema)

    label = _(u"CAS settings")
    description = _(u"CAS settings for this site.")
    form_name = _(u"CAS settings")

    @form.action(_(u"Save"))
    def save(self, action, data):
        if form.applyChanges(self.context,
                self.form_fields,
                data,
                self.adapters):
            self.status = _(u"Changes saved.")
        else:
            self.status = _(u"No changes made.")

    @form.action(_(u"Cancel"))
    def cancel(self, action, data):
        pass
        # TODO: redirect to plone control panel
