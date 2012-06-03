from mock import patch

from .utils import unittest, ArgyleTest
from argyle import supervisor


class SupervisorTest(ArgyleTest):
    "Base for setting up necessary patches."

    package = 'argyle.supervisor'
    patched_commands = ['sudo', 'upload_template', 'files', ]


class SupervisorCommandTest(SupervisorTest):
    "Calling supervisorctl commands."

    def test_update_command(self):
        "Call update command."
        supervisor.supervisor_command("update")
        self.assertSudoCommand('supervisorctl update')

    def test_restart_all(self):
        "Restart all supervisor managed processes."
        supervisor.supervisor_command("restart all")
        self.assertSudoCommand('supervisorctl restart all')


if __name__ == '__main__':
    unittest.main()
