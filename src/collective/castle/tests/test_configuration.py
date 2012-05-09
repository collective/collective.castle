import unittest2 as unittest

from zope.component import getUtility
from zope.schema import getFieldNames

from plone.registry.interfaces import IRegistry, IRecordsProxy
from plone.app.testing import TEST_USER_ID, setRoles

from collective.castle.control_panel import ICAS4PASPluginSchema
from collective.castle.testing import COLLECTIVE_CASTLE_INTEGRATION_TESTING


class IntegrationTest(unittest.TestCase):

    layer = COLLECTIVE_CASTLE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

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
            if hasattr(cas, field):
                self.assertEqual(getattr(cas, field), getattr(record, field))

    def test_non_plugin_fields(self):
        """Test CAS4PAS plugin doesn't receive values specific to castle."""
        record = getUtility(IRegistry).forInterface(ICAS4PASPluginSchema)
        record.users_require_role = True

        cas = self.portal.acl_users.cas
        self.assertFalse(hasattr(cas, 'users_require_role'))

    def test_monkey_patch(self):
        from Products.CAS4PAS.CASAuthHelper import CASAuthHelper
        self.assertIn('Monkey patch',
                      CASAuthHelper.authenticateCredentials.__doc__)
        self.assertTrue(hasattr(CASAuthHelper, '_old_authenticateCredentials'))

    def test_users_require_role(self):
        """Test CAS4PAS monkey patch requiring users to have a role to auth."""
        record = getUtility(IRegistry).forInterface(ICAS4PASPluginSchema)
        record.users_require_role = True

        cas = self.portal.acl_users.cas
        credentials = {'source': 'plone.session',
                       'login': TEST_USER_ID,
                       'extractor': 'cas'}

        #User has no access with no roles or Anonymous only
        for roles in ([], ['Anonymous']):
            setRoles(self.portal, TEST_USER_ID, roles)
            self.assertEqual(cas.authenticateCredentials(credentials),
                             (None, None))

        #User now has access with any other role
        for roles in ('Member', 'Contributor', 'Editor', 'Reader', 'Reviewer'):
            setRoles(self.portal, TEST_USER_ID, roles)
            self.assertEqual(cas.authenticateCredentials(credentials),
                             (TEST_USER_ID, TEST_USER_ID))
