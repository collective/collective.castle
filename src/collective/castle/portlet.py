from zope.interface import Interface, implements
from zope.formlib import form
from plone.app.portlets.portlets import base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.castle import util
from Products.CMFCore.utils import getToolByName


class IPortlet(Interface):
    pass


class Assignment(base.Assignment):
    implements(IPortlet)

    title = u'CAS Log in'


class Renderer(base.Renderer):
    render = ViewPageTemplateFile('login_portlet.pt')

    @property
    def submit_url(self):
        if self.is_logged_in():
            return 'castle_logout'
        else:
            return util.login_URL(self.context)

    @property
    def submit_name(self):
        if self.is_logged_in():
            return u'CAS Log out' # XXX TODO: i18n
        else:
            return u'CAS Log in' # XXX TODO: i18n

    def is_logged_in(self):
        mt = getToolByName(self.context, 'portal_membership')
        return not mt.isAnonymousUser()


class AddForm(base.AddForm):
    form_fields = form.Fields(IPortlet)

    def create(self, data):
        return Assignment()
