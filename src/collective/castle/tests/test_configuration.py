import unittest2 as unittest

from zope.component import getMultiAdapter, getUtility
from zope.schema import getFieldNames

from plone.registry.interfaces import IRegistry, IRecordsProxy

from collective.castle.control_panel import ICAS4PASPluginSchema
from collective.castle.testing import COLLECTIVE_CASTLE_INTEGRATION_TESTING


class IntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CASTLE_INTEGRATION_TESTING

    def setUp(self):
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

    def test_records_proxy(self):
        record = getUtility(IRegistry).forInterface(ICAS4PASPluginSchema)
        self.assertTrue(IRecordsProxy.providedBy(record))

    def test_plugin_creation(self):
        """Test CAS4PAS plugin gets created upon first access."""
        self.assertNotIn('cas', self.portal.acl_users)
        record = getUtility(IRegistry).forInterface(ICAS4PASPluginSchema)
        record.login_url = u'http://cas.localhost/cas/login'
        self.assertIn('cas', self.portal.acl_users)

    def test_value_proxy(self):
        """Test that CAS4PAS plugin receives values from registry."""
        record = getUtility(IRegistry).forInterface(ICAS4PASPluginSchema)
        record.login_url = u'http://login'
        record.logout_url = u'http://logout'
        record.validate_url = u'http://validate'
        record.session_var = u'cookie'
        record.use_ACTUAL_URL = False

        cas = self.portal.acl_users.cas
        for field in getFieldNames(ICAS4PASPluginSchema):
            self.assertEqual(getattr(cas, field), getattr(record, field))

