from mock import patch

from .utils import unittest, ArgyleTest
from argyle import rabbitmq


class RabbitTest(ArgyleTest):
    "Base for setting up necessary patches."

    package = 'argyle.rabbitmq'
    patched_commands = ['sudo', 'upload_template', 'restart_service', ]


class RabbitCommandsTest(RabbitTest):
    "Common rabbitmqctl commands for creating users/vhosts."

    def test_create_user(self):
        "Create a RabbitMQ user."
        rabbitmq.create_user('foo', 'bar')
        self.assertSudoCommand('rabbitmqctl add_user foo bar')

    def test_create_vhost(self):
        "Create a RabbitMQ vhost."
        rabbitmq.create_vhost('baz')
        self.assertSudoCommand('rabbitmqctl add_vhost baz')

    def test_set_default_permissions(self):
        "Grant use all permssions on a given vhost."
        rabbitmq.set_vhost_permissions(vhost='baz', username='foo')
        self.assertSudoCommand('rabbitmqctl set_permissions -p baz foo ".*" ".*" ".*"')

    def test_set_custom_permissions(self):
        "Grant permissions other than the default."
        rabbitmq.set_vhost_permissions(vhost='baz', username='foo', permissions='".*" "^amq.gen.*$" ".*"')
        self.assertSudoCommand('rabbitmqctl set_permissions -p baz foo ".*" "^amq.gen.*$" ".*"')


if __name__ == '__main__':
    unittest.main()
