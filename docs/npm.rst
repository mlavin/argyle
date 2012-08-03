NPM Functions
======================================

Tasks for installing, updating and removing packages installed with NPM, the package
manager for Node.JS.

.. versionadded:: 0.2


.. function:: npm_command(command)

    Execute any ``npm`` command on the remote server. This requires that ``npm``
    is installed.


.. function:: npm_install(package, flags=None)

    Install a given package from ``npm``. The ``flags`` parameter can be used to
    pass flags such as ``--tag``, ``--force``, ``--global`` or ``--link``. 


.. function:: npm_uninstall(package)

    Uninstall a package.


.. function:: npm_update(package)

    Update a package to the latest version.
