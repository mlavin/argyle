Settings
==================

Below are the available settings for configuring Argyle. Each of these settings
can be used by setting them in the Fabric environment 
`env <http://docs.fabfile.org/en/1.4.0/usage/env.html>`_ dictionary.


.. _ARGYLE_SERVICE_COMMAND_TEMPLATE:

ARGYLE_SERVICE_COMMAND_TEMPLATE
--------------------------------------

This settings configures the behavior of the system 
:ref:`stop/start/restart tasks <service_command>`. This should be a string with 
takes the formatting parameters ``name`` and ``command``.

Default: ``u'/etc/init.d/%(name)s %(command)s'``


.. _ARGYLE_TEMPLATE_DIRS:

ARGYLE_TEMPLATE_DIRS
--------------------------------------

By default Argyle loads various configuration templates from the templates
directory inside the argyle module. However, if you wish to override, extend or
include additional templates you can include additional directories using
this setting. Jinja will look for templates in any directories included here
first before loading from the default template directory. See the 
:ref:`upload_template` command for additional information on the usage.

Default: ``()``
