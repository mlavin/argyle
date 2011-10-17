System Functions
======================================

`argyle.system` contains functions for managing system packages and users. Most
of these system functions require sudo permissions. They should be run with
a user with sufficient permission on the remote server.


install_packages
-----------------------------------

This function installs a list of packages using `apt-get`. You can use
this function from both the command-line::

    fab -H 33.33.33.10 install_packages:nginx
    fab -H 33.33.33.10 install_packages:git-core,subversion,mercurial

or from another Fabric task

.. code-block:: python


    def install_python_packages():
        package_list = [
            'python2.6', 'python-all-dev', 'python-setuptools'
        ]
        install_packages(*package_list)


install_packages_from_file
-----------------------------------

A common use case for installing packages is to install a list of packages
from a file. `install_packages_from_file` is a thin wrapper around `install_packages`
which takes a filename and installs the listed packages. This file should contain 
single package name per line. The file is read from the local filesystem not the
remote.


update_apt_sources
-----------------------------------

Not much to say here. It just runs `apt-get update` to reload the sources.


upgrade_apt_packages
-----------------------------------

Again this is pretty simple. It runs a `safe-upgrade` on the remote system.


add_ppa
-----------------------------------

Adds a personal package archive and updates the sources. This requires that
python-software-properties is installed on the system.


create_user
-----------------------------------

This is used to create a new user on the remote server. You can optionally
pass a list of groups and the user will be added to them. In addition you can
pass the location of a key file. If given the public key will be added to the
newly created user`s authorized_keys. All users are created without passwords.


service_command
-----------------------------------

This is a task for calling service commands (such as init.d). This takes the
name of the service and the command to run::

    fab -H 33.33.33.10 service_command:apache2,reload

By default this will call `sudo /etc/init.d/name command`. You can configure this
by setting `env.ARGYLE_SERVICE_COMMAND_TEMPLATE`. This should be a string with
takes the formatting parameters `name` and `command`.

.. code-block:: python

    from fabric.api import env

    env.ARGYLE_SERVICE_COMMAND_TEMPLATE = u'invoke-rc.d %(name)s %(command)'

`start_service`, `stop_service` and `restart_service` are wrappers around
`service_command` to call start, stop and restart commands for a particular
service. As such they are also impacted by setting `ARGYLE_SERVICE_COMMAND_TEMPLATE`.
