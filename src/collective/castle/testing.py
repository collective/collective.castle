from plone.app.testing import PloneSandboxLayer, PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import quickInstallProduct


class CollectiveCastleLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        from plone.testing import z2
        with z2.zopeApp() as app:
            z2.installProduct(app, 'Products.CAS4PAS')

        # Load ZCML
        import collective.castle
        self.loadZCML(package=collective.castle, context=configurationContext)

    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'collective.castle:default')
        quickInstallProduct(portal, 'Products.CAS4PAS')


COLLECTIVE_CASTLE_FIXTURE = CollectiveCastleLayer()
COLLECTIVE_CASTLE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(COLLECTIVE_CASTLE_FIXTURE,),
    name="collective.castle:Integration"
)
