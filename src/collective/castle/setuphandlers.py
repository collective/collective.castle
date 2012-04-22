from Products.CMFCore.utils import getToolByName


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
