from zope.component import getUtility
from zope.schema import getFieldNames

from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName

from collective.castle.control_panel import ICAS4PASPluginSchema


PROFILE_ID = 'profile-collective.castle:default'

def run_import_step(context, step):
    """Re-import some specified import step for Generic Setup.
    """
    setup = getToolByName(context, 'portal_setup')
    return setup.runImportStepFromProfile(PROFILE_ID, step)

def upgrade_controlpanel(context):
    run_import_step(context, 'controlpanel')

def upgrade_actions(context):
    run_import_step(context, 'actions')

def upgrade_to_plone_app_registry(context):
    run_import_step(context, 'plone.app.registry')

    #Configure settings by loading values from CAS plugin
    acl_users = getToolByName(context, 'acl_users')

    cas_auth_helpers = acl_users.objectValues(['CAS Auth Helper'])
    if cas_auth_helpers:
        cas = cas_auth_helpers[0]
        settings = getUtility(IRegistry).forInterface(ICAS4PASPluginSchema)

        #Step through fields and migrate values across to the registry
        for key in getFieldNames(ICAS4PASPluginSchema):
            old_value = getattr(cas, key)
            if isinstance(old_value, str):
                #Convert old strings to unicode
                old_value = unicode(old_value)
            setattr(settings, key, old_value)





