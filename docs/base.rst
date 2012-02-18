Base Functions
======================================

``argyle.base`` contains functions which extend the Fabric api to make the rest
of the Argyle framework work.


sshagent_run
-----------------------------------

The base ssh library paramiko and hence Fabric does not support SSH Agent
forwarding. However, using agent forwarding can be helpful for accessing private
repositories (such as hg/git) using ssh without having to generate and allow the
ssh key for the server on the repository. To use this function you must enable 
SSH forwarding on your system.::

    ForwardAgent yes

This code is based on code from `Lincoln Loop <http://lincolnloop.com/blog/2009/sep/22/easy-fabric-deployment-part-1-gitmercurial-and-ssh/>`_. For more info you can see the `Fabric issue <https://github.com/fabric/fabric/issues/72>`_ 
and `paramiko issue <https://bugs.launchpad.net/paramiko/+bug/483697>`_ for adding
support for agent forwarding.


.. _upload_template:

upload_template
-----------------------------------

Fabric comes with support for uploading files using a template. See
`fabric.contrib.files.upload_template <http://docs.fabfile.org/en/1.2.2/api/contrib/files.html#fabric.contrib.files.upload_template>`_. With this you can use either
Python string formatting or Jinja2. Argyle uses this same idea but with a few differences:

    1. All templates use Jinja2.

    2. The current Fabric environment is always passed into the template context.

    3. You can pass list of template names. The first matched template will be used.

Argyle ships with templates which are loaded using `jinja2.PackageLoader 
<http://jinja.pocoo.org/docs/api/#jinja2.PackageLoader>`_. You can override these
template by defining :ref:`env.ARGYLE_TEMPLATE_DIRS <ARGYLE_TEMPLATE_DIRS>` 
as a tuple of template locations.
