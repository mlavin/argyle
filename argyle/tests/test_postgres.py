from mock import patch

from .utils import unittest, ArgyleTest
from argyle import postgres


class PostgresTest(ArgyleTest):
    "Base for setting up necessary patches."

    package = 'argyle.postgres'
    patched_commands = ['run', 'sudo', 'upload_template', 'restart_service', ]


class ExcuteQueryTest(PostgresTest):
    "Excute Sql on the remote server."

    def test_basic_sql(self):
        "Excute a command which does not require using the postgres user."
        postgres.excute_query("SELECT version();")
        self.assertRunCommand('psql  -c "SELECT version();"')

    def test_use_sudo(self):
        "Excute a command which does requires using the postgres user."
        postgres.excute_query("SELECT version();", use_sudo=True)
        self.assertSudoCommand('psql  -c "SELECT version();"')
        sudo = self.mocks['sudo']
        args, kwargs = sudo.call_args
        user = kwargs.get('user', None)
        self.assertEqual(user, 'postgres')

    def test_set_query_db(self):
        "Set the DB to be used by the query."
        postgres.excute_query("SELECT version();", db='test')
        self.assertRunCommand('psql  -d test -c "SELECT version();"')

    def test_query_flags(self):
        "Set additional command line flags."
        postgres.excute_query("SELECT version();", flags='-p 5433')
        self.assertRunCommand('psql -p 5433 -c "SELECT version();"')


class CreateUserTest(PostgresTest):
    "Create users on the Postgres server."

    def test_user_defaults(self):
        "Default flags for use creation."
        postgres.create_db_user('foo')
        self.assertSudoCommand('createuser -D -A -R foo')
        # Command should use the postgres user
        sudo = self.mocks['sudo']
        args, kwargs = sudo.call_args
        user = kwargs.get('user', None)
        self.assertEqual(user, 'postgres')

    def test_change_user_flags(self):
        "Create user with different flags."
        postgres.create_db_user('foo', flags='-s')
        self.assertSudoCommand('createuser -s foo')

    def test_set_user_password(self):
        "Create user then set their password."
        with patch('argyle.postgres.change_db_user_password') as change_password:
            postgres.create_db_user('foo', password='bar')
            self.assertSudoCommand('createuser -D -A -R foo')
            self.assertTrue(change_password.called)
            args, kwargs = change_password.call_args
            self.assertEqual(list(args), ['foo', 'bar'])

    def test_change_user_password(self):
        "Execute query to change user password."
        postgres.change_db_user_password('foo', 'bar')
        self.assertSudoCommand('psql  -c "ALTER USER foo WITH PASSWORD \'bar\'"')


class CreateDBTest(PostgresTest):
    "Create databases on the Postgres server."
    
    def test_database_defaults(self):
        "Create database with default flags."
        postgres.create_db('foo')
        self.assertSudoCommand('createdb -E UTF-8 foo')
        # Command should use the postgres user
        sudo = self.mocks['sudo']
        args, kwargs = sudo.call_args
        user = kwargs.get('user', None)
        self.assertEqual(user, 'postgres')
        
    def test_database_owner(self):
        "Set the owner of the database on creation."
        postgres.create_db('foo', owner='bar')
        self.assertSudoCommand('createdb -E UTF-8 -O bar foo')

    def test_database_encoding(self):
        "Change the encoding when creating the database."
        postgres.create_db('foo', encoding='LATIN1')
        self.assertSudoCommand('createdb -E LATIN1 foo')


class DetectVersionTest(PostgresTest):
    "Attempt to detect Postgres version running on the server."

    def test_check_run_output(self):
        "Detect via psql --version output."
        run = self.mocks['run']
        run.return_value = 'psql (PostgreSQL) 9.1.3'
        postgres.detect_version()
        self.assertRunCommand('psql --version')

    def test_parse_version(self):
        "Returns the parsed major and minor version number."
        run = self.mocks['run']
        run.return_value = 'psql (PostgreSQL) 9.1.3'
        version = postgres.detect_version()
        self.assertEqual(version, '9.1')

    def test_parse_failed(self):
        "Abort command on parse failure."
        run = self.mocks['run']
        run.return_value = ''
        with patch('argyle.postgres.abort') as abort:
            postgres.detect_version()
            self.assertTrue(abort.called)


if __name__ == '__main__':
    unittest.main()
