import os

from mock import patch

from .utils import unittest, ArgyleTest
from argyle import system


class PackageCommandsTest(ArgyleTest):
    "Package management (install, update, etc) commands."

    package = 'argyle.system'
    patched_commands = ['run', 'sudo', 'put', 'files', ]

    def test_install_single_package(self):
        "Install a single package throuh apt."
        system.install_packages('python')
        self.assertSudoCommand('apt-get install -y python')

    def test_install_multiple_packages(self):
        "Install multiple packages through apt."
        system.install_packages('python', 'python-setuptools')
        self.assertSudoCommand('apt-get install -y python python-setuptools')

    def test_install_from_file(self):
        "Install packages from a file."
        path = os.path.join(os.path.dirname(__file__), 'data/packages.txt')
        system.install_packages_from_file(path)
        self.assertSudoCommand('apt-get install -y python python-setuptools')

    def test_upgrade_packages(self):
        "Call apt-get upgrade."
        system.upgrade_apt_packages()
        self.assertSudoCommand('apt-get upgrade -y')

    def test_update_package_sources(self):
        "Call apt-get update."
        system.update_apt_sources()
        self.assertSudoCommand('apt-get update')

    def test_add_ppa(self):
        "Add PPA and refresh apt-sources."
        with patch('argyle.system.update_apt_sources') as update:
            system.add_ppa('ppa:nginx/stable')
            self.assertSudoCommand('add-apt-repository ppa:nginx/stable')
            self.assertTrue(update.called)

    def test_add_ppa_no_update(self):
        "Add PPA without updating sources."
        with patch('argyle.system.update_apt_sources') as update:
            system.add_ppa('ppa:nginx/stable', update=False)
            self.assertSudoCommand('add-apt-repository ppa:nginx/stable')
            self.assertFalse(update.called)

    def test_add_ppas_from_file(self):
        "Add PPAs from file list."
        path = os.path.join(os.path.dirname(__file__), 'data/ppas.txt')
        with patch('argyle.system.update_apt_sources') as update:
            with patch('argyle.system.add_ppa') as add_ppa:
                system.add_ppas_from_file(path)
                self.assertEqual(add_ppa.call_count, 2)
                self.assertEqual(update.call_count, 1)

    def test_add_apt_source_no_key(self):
        "Add apt souce without key url."
        with patch('argyle.system.update_apt_sources') as update:
            system.add_apt_source("deb http://example.com/deb lucid main")
            # Source file should be backed up
            self.assertSudoCommand('cp /etc/apt/sources.list{,.bak}')
            files = self.mocks['files']
            self.assertTrue(files.append.called)
            args, kwargs = files.append.call_args
            source_list = args[0]
            new_source = args[1]
            self.assertEqual(source_list, '/etc/apt/sources.list')
            self.assertEqual(new_source, 'deb http://example.com/deb lucid main')
            # Apt sources should be updated
            self.assertTrue(update.called)

    def test_add_apt_source_no_update(self):
        "Add apt souce without updating apt sources."
        with patch('argyle.system.update_apt_sources') as update:
            system.add_apt_source("deb http://example.com/deb lucid main", update=False)
            # Apt sources should not be updated
            self.assertFalse(update.called)

    def test_add_apt_source_with_key(self):
        "Add apt souce with key url."
        with patch('argyle.system.update_apt_sources') as update:
            source = "deb http://example.com/deb lucid main"
            key = "http://example.com/key"
            system.add_apt_source(source, key)
            # Key file should be added
            self.assertSudoCommand('wget -q http://example.com/key -O - | sudo apt-key add -')
            files = self.mocks['files']
            self.assertTrue(files.append.called)
            args, kwargs = files.append.call_args
            source_list = args[0]
            new_source = args[1]
            self.assertEqual(source_list, '/etc/apt/sources.list')
            self.assertEqual(new_source, source)
            # Apt sources should be updated
            self.assertTrue(update.called)

    def test_add_apt_sources_from_file(self):
        "Add a list of apt sources from a file."
        path = os.path.join(os.path.dirname(__file__), 'data/sources.txt')
        with patch('argyle.system.update_apt_sources') as update:
            with patch('argyle.system.add_apt_source') as add_source:
                system.add_sources_from_file(path)
                self.assertEqual(add_source.call_count, 2)
                self.assertEqual(update.call_count, 1)


if __name__ == '__main__':
    unittest.main()
