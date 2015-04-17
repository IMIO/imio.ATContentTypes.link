# -*- coding: utf-8 -*-
"""Setup/installation tests for this package."""

from imio.ATContentTypes.link.testing import IntegrationTestCase
from plone import api


class TestInstall(IntegrationTestCase):
    """Test installation of imio.ATContentTypes.link into Plone."""

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if imio.ATContentTypes.link is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('imio.ATContentTypes.link'))

    def test_uninstall(self):
        """Test if imio.ATContentTypes.link is cleanly uninstalled."""
        self.installer.uninstallProducts(['imio.ATContentTypes.link'])
        self.assertFalse(self.installer.isProductInstalled('imio.ATContentTypes.link'))

    # browserlayer.xml
    def test_browserlayer(self):
        """Test that IImioAtcontenttypesLinkLayer is registered."""
        from imio.ATContentTypes.link.interfaces import IImioAtcontenttypesLinkLayer
        from plone.browserlayer import utils
        self.assertIn(IImioAtcontenttypesLinkLayer, utils.registered_layers())
