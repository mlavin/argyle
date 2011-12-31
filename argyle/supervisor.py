from argyle.base import upload_template
from fabric.api import sudo, task
from fabric.contrib import files


@task
def supervisor_command(command):
    """Run a supervisorctl command."""

    sudo(u'supervisorctl %s' % command)


@task
def upload_supervisor_app_conf(app_name, template_name=None, context=None):
    """Upload Supervisor app configuration from a template."""
    
    template_name = template_name or [u'supervisor/%s.conf' % app_name, u'supervisor/base.conf']
    destination = u'/etc/supervisor/conf.d/%s.conf' % app_name
    upload_template(template_name, destination, context=context, use_sudo=True)
    supervisor_command(u'update')


@task
def remove_supervisor_app(app_name):
    """Remove Supervisor app configuration."""

    app = u'/etc/supervisor/conf.d/%s.conf' % app_name
    if files.exists(site):
        sudo(u'rm %s' % app)
        supervisor_command(u'update')
