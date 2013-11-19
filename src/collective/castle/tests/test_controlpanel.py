import unittest2 as unittest
import transaction

from zope.component import getMultiAdapter


from collective.castle.testing import COLLECTIVE_CASTLE_INTEGRATION_TESTING


class IntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CASTLE_INTEGRATION_TESTING

    def setUp(self):
        self.app = self.layer['app']
        self.portal = self.layer['portal']

    def test_controlpanel_view(self):
        view = getMultiAdapter((self.portal, self.portal.REQUEST),
                               name='cas_control_panel')
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_controlpanel_view_protected(self):
        from AccessControl import Unauthorized
        from plone.app.testing import logout
        logout()
        self.assertRaises(Unauthorized,
                          self.portal.restrictedTraverse,
                          '@@cas_control_panel')

    def test_createplugin(self):
        from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, \
            TEST_USER_PASSWORD
        from plone.app.testing import setRoles, login

        login(self.portal, TEST_USER_NAME)
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        transaction.commit()

        from plone.testing.z2 import Browser
        browser = Browser(self.app)
        browser.addHeader('Authorization',
                          'Basic %s:%s' % (TEST_USER_NAME,
                                           TEST_USER_PASSWORD))
        browser.open(self.portal.absolute_url() + '/@@cas_control_panel')

        #The plugin should not yet exist
        self.assertNotIn('cas', self.portal.acl_users)

        browser.getControl('Recreate Plugin').click()

        #The plugin now exists post button press
        self.assertIn('cas', self.portal.acl_users)

        #Ensure plugin can be recreated if broken
        cas = self.portal.acl_users.cas
        cas.login_url = 'dummy'
        browser.getControl('Recreate Plugin').click()

        #Should be the default URL, not dummy
        self.assertEqual(self.portal.acl_users.cas.login_url,
                         'https://your.cas.server:port/cas/login')
