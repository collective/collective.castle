# -*- coding: utf-8 -*-
from StringIO import StringIO

from zope.component import adapter
from zope.schema import getFields
from zope.app.component.hooks import getSite

from Products.CMFPlone import PloneMessageFactory as _
from Products.PlonePAS.Extensions.Install import activatePluginInterfaces
from Products.statusmessages.interfaces import IStatusMessage

from plone.app.registry.browser import controlpanel
from plone.registry.interfaces import IRecordModifiedEvent

from collective.castle.interfaces import ICAS4PASPluginSchema


@adapter(ICAS4PASPluginSchema, IRecordModifiedEvent)
def updateCASSettings(settings, event):
    portal = getSite()
    acl_users = portal.acl_users
    cas_auth_helpers = acl_users.objectValues(['CAS Auth Helper'])
    if not cas_auth_helpers:
        cas4pas = acl_users.manage_addProduct['CAS4PAS']
        cas4pas.addCASAuthHelper('cas', 'CAS Auth Helper')
        cas = acl_users['cas']

        #Load defaults from fields
        fields = getFields(ICAS4PASPluginSchema)
        for field in fields:
            setattr(cas, field, fields[field].default)

        out = StringIO()
        activatePluginInterfaces(portal, 'cas', out)
        msg = 'Created CAS plugin. %s' % out.getvalue()
        IStatusMessage(portal.REQUEST).addStatusMessage(msg, 'info')
    else:
        cas = cas_auth_helpers[0]

    #Proxy the changed value to the CAS4PAS helper
    setattr(cas, event.record.fieldName, event.newValue)

class CASSettingsEditForm(controlpanel.RegistryEditForm):

    schema = ICAS4PASPluginSchema
    label = _(u"CAS settings")
    description = _(u"CAS settings for this site.")

    def updateWidgets(self):
        super(CASSettingsEditForm, self).updateWidgets()
        for field in ('login_url', 'logout_url', 'validate_url'):
            self.widgets[field].displayWidth = 60

class CASSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = CASSettingsEditForm
