Supevisord Functions
======================================

Tasks for configuring processes which will be managed by Supervisord.


.. function:: supervisor_command(command)

    This is a simple way to execute a ``supervisorctl`` command on the remote server
    similar to the :py:func:`service_command`.


.. function:: upload_supervisor_app_conf(app_name, template_name=None, context=None)

    Uploads a configuration to ``/etc/supervisor/conf.d/<app_name>.conf`` for managing a new process.
    If the ``template_name`` is not given it will look for templates named ``supervisor/<app_name>.conf``
    and if not found it will use the ``supervisor/base.conf`` included with this project. The
    ``app_name`` parameter is passed in the context and additional context can be provided
    with the ``context`` parameter.

    The default ``supervisor/base.conf`` is shown below.

    .. literalinclude:: ../argyle/templates/supervisor/base.conf


.. function:: remove_supervisor_app(app_name)

    Deletes the ``/etc/supervisor/conf.d/<app_name>.conf`` configuration.


.. function:: upload_celery_conf(command='celeryd', app_name=None, template_name=None, context=None)

    A wrapper around :py:func:`upload_supervisor_app_conf` for managing a
    `Celery <http://www.celeryproject.org/>`_ process such as ``celeryd`` or ``celerybeat``.
    The ``app_name`` defaults to the ``command`` and both are pass in the context. A
    default ``supervisor/celery.conf`` is included which will be used instead of ``supervisor/base.conf``
    if ``supervisor/<app_name>.conf`` is not found.

    The default ``supervisor/celery.conf`` is shown below.

    .. literalinclude:: ../argyle/templates/supervisor/celery.conf


.. function:: upload_gunicorn_conf(command='gunicorn', app_name=None, template_name=None, context=None)

    A wrapper around :py:func:`upload_supervisor_app_conf` for managing a
    `Gunicorn <http://gunicorn.org/>`_ process such as ``gunicorn`` or ``gunicorn_django``.
    The ``app_name`` defaults to the ``command`` and both are pass in the context. A
    default ``supervisor/gunicorn.conf`` is included which will be used instead of ``supervisor/base.conf``
    if ``supervisor/<app_name>.conf`` is not found.

    The default ``supervisor/gunicorn.conf`` is shown below.

    .. literalinclude:: ../argyle/templates/supervisor/gunicorn.conf
