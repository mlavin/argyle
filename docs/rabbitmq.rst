RabbitMQ Functions
======================================

Tasks for managing vhosts, users and configurations for RabbitMQ.


.. function:: rabbitmq_command(command)

    This is a simple way to execute a ``rabbitmqctl`` command on the remote server
    similar to the :py:func:`service_command`.


.. function:: create_user(username, password)

    Creates a new RabbitMQ user with the given name and password.


.. function:: create_vhost(name)

    Creates a new vhost on the remote RabbitMQ server.


.. function:: set_vhost_permissions(vhost, username, permissions='".*" ".*" ".*"')

    Grants the given permissions to the user on the given vhost. By default all permissions
    are granted.


.. function:: upload_rabbitmq_environment_conf(template_name=None, context=None, restart=True)

    Uploads the RabbitMQ environment configuration to ``/etc/rabbitmq/rabbitmq-env.conf``. This
    looks for a template named ``rabbitmq/rabbitmq-env.conf`` if the ``template_name`` is not
    given. A default for this template is not given.


.. function:: upload_rabbitmq_conf(template_name=None, context=None, restart=True)

    Uploads the RabbitMQ configuration to ``/etc/rabbitmq/rabbitmq.config``. This
    looks for a template named ``rabbitmq/rabbitmq.config`` if the ``template_name`` is not
    given. A default for this template is not given.
