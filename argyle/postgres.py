from argyle.base import upload_template
from fabric.api import sudo, task


def create_db_user(username, password=None, flags=None):
    """Create a databse user."""

    flags = flags or u''
    sudo(u'createuser -D -A -R %s' % username, user=u'postgres')
    if password:
        change_db_user_password(username, password)


def change_db_user_password(username, password):
    """Change a db user's password."""

    sql = "ALTER USER %s WITH PASSWORD '%s'" % (username, password)
    sudo('psql -c "%s"' % sql, user='postgres')


def create_db(name, owner=None, encoding=u'UTF-8'):
    """Create a Postgres database."""

    flags = u''
    if encoding:
        flags = u'-E %s' % encoding
    if owner:
        flags = u'%s -O %s' % (flags, owner)
    sudo('createdb %s %s' % (flags, name), user='postgres')
