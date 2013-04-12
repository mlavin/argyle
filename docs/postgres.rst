Postgres Functions
======================================

Tasks for managing clusters, databases, users and configurations for a Postgres server.


.. function:: create_db_user(username, password=None, flags=None)

    Creates a database user and sets a password if given. You can pass additional
    creation flags with the ``flags`` parameter.

.. function:: db_user_exists(username)

    Return True if the database user already exists.

.. function:: excute_query(query, db=None, flags=None, use_sudo=False, **kwargs)

    Execute a SQL query on the remote server. You can specify the DB and additional
    flags with the ``db`` and ``flags`` parameter. If ``use_sudo`` is True then this
    will be executed as the ``postgres`` user.  Additional ``**kwargs`` are
    passed to ``sudo`` or ``run``.


.. function:: create_db(name, owner=None, encoding=u'UTF-8')

    Creates a new database with a given owner (if given) and encoding.

.. function:: db_exists(name)

    Return True if the database already exists.

.. function:: upload_pg_hba_conf(template_name=None, pg_version=None, pg_cluster='main', restart=True)

    Uploads a configuration to ``/etc/postgresql/<version>/<cluster>/pg_hba.conf`` from a template.
    If not given the Postgres version will be detected on the server. The default template name
    is ``postgres/pg_hba.conf``.


.. function:: reset_cluster(pg_cluster='main', pg_version=None, encoding=u'UTF-8', locale=u'en_US.UTF-8')

    Drops and restores a given cluster. This is mainly used for provisioning a new server
    to ensure the cluster has the desired default encoding.
