from argyle.base import upload_template
from fabric.api import sudo, task


@task
def create_db_user(username, password=None, flags=None):
    """Create a databse user."""

    flags = flags or u'-D -A -R'
    sudo(u'createuser %s %s' % (flags, username), user=u'postgres')
    if password:
        change_db_user_password(username, password)


@task
def excute_query(query, user='postgres', db=None, flags=None):
    """Execute remote psql query."""

    flags = flags or u''
    if db:
        flags = u"%s -d %s" % (flags, db)
    sudo('psql %s -c "%s"' % (flags, query), user=user)


@task
def change_db_user_password(username, password):
    """Change a db user's password."""

    sql = "ALTER USER %s WITH PASSWORD '%s'" % (username, password)
    excute_query(sql)


@task
def create_db(name, owner=None, encoding=u'UTF-8'):
    """Create a Postgres database."""

    flags = u''
    if encoding:
        flags = u'-E %s' % encoding
    if owner:
        flags = u'%s -O %s' % (flags, owner)
    sudo('createdb %s %s' % (flags, name), user='postgres')
