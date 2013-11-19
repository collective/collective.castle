from zope.component import getUtility

from plone.registry.interfaces import IRegistry
from Products.CMFCore.utils import getToolByName
from Products.PluggableAuthService.interfaces.plugins import IRolesPlugin

from collective.castle.interfaces import ICAS4PASPluginSchema


def authenticateCredentials(self, credentials):
    result = self._old_authenticateCredentials(credentials)
    userId = result[0]
    if userId:
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ICAS4PASPluginSchema)

        #Check whether the option is set and user has a portal role
        if settings.users_require_role:
            acl = getToolByName(self, 'acl_users')
            rolemakers = acl.plugins.listPlugins(IRolesPlugin)
            user = acl.getUserById(userId)
            allAssignedRoles = []

            if user:
                for rolemaker_id, rolemaker in rolemakers:
                    allAssignedRoles.extend(
                        rolemaker.getRolesForPrincipal(user)
                    )

            if not user or \
               not allAssignedRoles \
               or allAssignedRoles == ['Anonymous']:
                #If no user or no role assigned, then prevent authentication
                result = (None, None)

    return result
