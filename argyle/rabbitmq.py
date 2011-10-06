from fabric.api import sudo, task


@task
def rabbitmq_command(command):
    """Run a rabbitmqctl command."""

    sudo(u'rabbitmqctl %s' % command)


@task
def create_user(username, password):
    """Create a rabbitmq user."""

    rabbitmq_command(u'add_user %s %s' % (username, password))


@task
def create_vhost(name):
    """Create a rabbitmq vhost."""

    rabbitmq_command(u'add_vhost %s' % name)


@task
def set_vhost_permissions(vhost, username, permissions='".*" ".*" ".*"')
    """Set permssions for a user on a given vhost."""

    rabbitmq_command(u'set_permissions -p %s %s %s' % (vhost, username, permissions))
