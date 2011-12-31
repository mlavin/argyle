import re

from argyle.base import upload_template
from argyle.system import restart_service
from fabric.api import abort, hide, run, sudo, task


@task
def create_db_user(username, password=None, flags=None):
    """Create a databse user."""

    flags = flags or u'-D -A -R'
    sudo(u'createuser %s %s' % (flags, username), user=u'postgres')
    if password:
        change_db_user_password(username, password)


@task
def excute_query(query, db=None, flags=None, use_sudo=False):
    """Execute remote psql query."""

    flags = flags or u''
    if db:
        flags = u"%s -d %s" % (flags, db)
    command = u'psql %s -c "%s"' % (flags, query)
    if use_sudo:
        sudo(command, user='postgres')
    else:    
        run(command)


@task
def change_db_user_password(username, password):
    """Change a db user's password."""

    sql = "ALTER USER %s WITH PASSWORD '%s'" % (username, password)
    excute_query(sql, use_sudo=True)


@task
def create_db(name, owner=None, encoding=u'UTF-8'):
    """Create a Postgres database."""

    flags = u''
    if encoding:
        flags = u'-E %s' % encoding
    if owner:
        flags = u'%s -O %s' % (flags, owner)
    sudo('createdb %s %s' % (flags, name), user='postgres')


@task
def upload_pg_hba_conf(filename='postgres/pg_hba.conf',
    pg_version=None, pg_cluster='main', restart=True):
    """
    Upload configuration for pg_hba.conf
    If the version is not given it will be guessed.
    """

    if not pg_version:
        version_regex = re.compile(r'\(PostgreSQL\) (?P<major>\d)\.(?P<minor>\d)\.(?P<bugfix>\d)')
        with hide('running', 'stdout', 'stderr'):
            output = run('psql --version')
        match = version_regex.search(output)
        if match:
            result = match.groupdict()
            if 'major' in result and 'minor' in result:
                pg_version = u'%(major)s.%(minor)s' % result
        if not pg_version:
            abort(u"Error: Could not determine Postgres version of the server.")
    config = {'version': pg_version, 'cluster': pg_cluster}
    destination = u'/etc/postgresql/%(version)s/%(cluster)s/pg_hba.conf' % config
    upload_template(filename, destination, use_sudo=True)
    if restart:
        restart_service(u'postgresql')
