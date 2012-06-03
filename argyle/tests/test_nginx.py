from mock import patch

from .utils import unittest, ArgyleTest
from argyle import nginx


class NginxTest(ArgyleTest):
    "Base for setting up necessary patches."

    package = 'argyle.nginx'
    patched_commands = ['sudo', 'files', 'upload_template', 'restart_service', ]


class EnableDisableSitesTest(NginxTest):
    "Enabling and disabling site configurations."

    def test_remove_default_site(self):
        "Remove default site if it exists."
        self.mocks['files'].exists.return_value = True
        nginx.remove_default_site()
        self.assertSudoCommand('rm /etc/nginx/sites-enabled/default')

    def test_default_site_already_removed(self):
        "Ignore removing default site if it is already removed."
        self.mocks['files'].exists.return_value = False
        nginx.remove_default_site()
        self.assertFalse(self.mocks['sudo'].called)

    def test_enable_site(self):
        "Enable a site in sites-available."
        self.mocks['files'].exists.return_value = True
        nginx.enable_site('foo')
        self.assertSudoCommand('ln -s -f /etc/nginx/sites-available/foo /etc/nginx/sites-enabled/foo')
        # Restart should be called
        self.assertTrue(self.mocks['restart_service'].called)

    def test_enable_missing_site(self):
        "Abort if attempting to enable a site which is not available."
        self.mocks['files'].exists.return_value = False
        with patch('argyle.nginx.abort') as abort:
            nginx.enable_site('foo')
            self.assertTrue(abort.called)
            # Restart should not be called
            self.assertFalse(self.mocks['restart_service'].called)

    def test_disable_site(self):
        "Remove a site from sites-enabled."
        self.mocks['files'].exists.return_value = True
        nginx.disable_site('foo')
        self.assertSudoCommand('rm /etc/nginx/sites-enabled/foo')
        # Restart should be called
        self.assertTrue(self.mocks['restart_service'].called)

    def test_disable_site_already_removed(self):
        "Ignore removing a site if it is already removed."
        self.mocks['files'].exists.return_value = False
        nginx.disable_site('foo')
        self.assertFalse(self.mocks['sudo'].called)
        # Restart should not be called
        self.assertFalse(self.mocks['restart_service'].called)


if __name__ == '__main__':
    unittest.main()
