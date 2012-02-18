Motivation
======================================

We love Fabric for deployments. We also use it for our server provisioning scripts.
However, I found myself repeatedly writing the same Fabric tasks over and over again
without a good way to reuse them from project to project. This was leading to a
lot of wasted time and copy-paste errors.

While there are a number of existing projects out there for Django deployments
with Fabric, I found most to be very opinionated about project/server layout.
Unfortunately I am also very opinionated about server layout. I also found that
they did not scale up well to multiple servers (separate app and db servers,
multiple app servers behind a load balancer).

In no particular order my goals in creating this project are:

- Standardize common Fabric tasks for server configuration and deployment
- Provide sane defaults for configurations with the ability to override
- Remain as agnostic as possible for directory layout
- Works well for single server and muli-server deployments


Related Projects
-----------------------------------

There are some similar projects. If this project does work for you
then I would recommend you check out:

1. `woven <https://github.com/bretth/woven>`_
2. `django-fab-deploy <https://bitbucket.org/kmike/django-fab-deploy>`_
3. `django-fab <https://github.com/hbussell/django-fab>`_
4. `django-fabtastic <https://github.com/duointeractive/django-fabtastic>`_

I apologize in advance if you felt I've left out your project.
