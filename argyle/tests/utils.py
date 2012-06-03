"Test helper utility methods."

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from mock import patch


class ArgyleTest(unittest.TestCase):
    "Common test base."

    package = ''
    patched_commands = []

    def setUp(self):
        "Setup patches for Fabric commands."
        self.patches = {}
        self.mocks = {}
        for command in self.patched_commands:
            self.patches[command] = patch('%s.%s' % (self.package, command))
            self.mocks[command] = self.patches[command].start()            

        
    def tearDown(self):
        "Remove patched commands."
        for command, patched in self.patches.items():
            patched.stop()

    def assertSudoCommand(self, expected):
        "Assert sudo was called with a particular command."
        sudo = self.mocks['sudo']
        self.assertTrue(sudo.called)
        args, kwargs = sudo.call_args
        command = args[0]
        self.assertEqual(command, expected)         
