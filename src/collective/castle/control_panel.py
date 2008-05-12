from zope.interface import Interface
from zope.interface import implements

from zope.component import getUtility

from zope.schema import TextLine

from zope.formlib.form import action
from zope.formlib.form import FormFields

from Products.CMFCore.utils import getToolByName

from Products.CMFPlone import PloneMessageFactory as _

from Products.Five.formlib.formbase import EditForm

from Products.PlonePAS.Extensions.Install import activatePluginInterfaces

class ICAS4PASPluginSchema(Interface):
    login_url = TextLine(title=_(u"CAS Log in URL"), 
        description=_(u""), required=True)
    logout_url = TextLine(title=_(u"CAS Log out URL"), 
        description=_(u""), required=True)
    validate_url = TextLine(title=_(u"CAS Validate URL"), 
        description=_(u""), required=True)

class CASControlPanel(EditForm):
    
    form_fields = FormFields(ICAS4PASPluginSchema)
    label = _(u"CAS settings")
    description = _(u"CAS settings for this site.")
    form_name = _(u"CAS settings")
    
    @action(_(u"Save"))
    def save(self, action, data):
        pass
    
    @action(_(u"Cancel"))
    def cancel(self, action, data):
        pass
    
    def update(self):
    	pass

def CASPluginFactory(context):
    # TODO: Implement sophisticated logic to find an existing CAS plugin
    # that doesn't have 'cas' as the id.
    return getUtility('ICASConfiguration')
    
    if 'cas' not in portal.acl_users:
        cas = portal.acl_users.manage_addProduct['CAS4PAS']
        cas.addCASAuthHelper('cas', 'CAS')
        portal.acl_users['cas'].login_url = 'https://your.cas.server:port/cas/login'
        portal.acl_users['cas'].logout_url = 'https://your.cas.server:port/cas/logout'
        portal.acl_users['cas'].validate_url = 'https://your.cas.server:port/cas/validate'
        portal.acl_users['cas'].session_var = '__ac'
        portal.acl_users['cas'].use_ACTUAL_URL = True
    else:
    	pass
