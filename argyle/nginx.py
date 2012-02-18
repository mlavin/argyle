from argyle.base import upload_template
from argyle.system import start_service, stop_service, restart_service
from fabric.api import abort, sudo, task
from fabric.contrib import files


@task
def remove_default_site():
    """Remove the default Nginx site if it exists."""

    nginx_default = u'/etc/nginx/sites-enabled/default'
    if files.exists(nginx_default):
        sudo(u'rm %s' % nginx_default)


@task
def upload_nginx_site_conf(site_name, template_name=None, context=None, enable=True):
    """Upload Nginx site configuration from a template."""
    
    template_name = template_name or [u'nginx/%s.conf' % site_name, u'nginx/site.conf']
    site_available = u'/etc/nginx/sites-available/%s' % site_name
    upload_template(template_name, site_available, context=context, use_sudo=True)
    if enable:
        enable_site(site_name)


@task
def enable_site(site_name):
    """Enable an available Nginx site."""

    site_available = u'/etc/nginx/sites-available/%s' % site_name
    site_enabled = u'/etc/nginx/sites-enabled/%s' % site_name
    if files.exists(site_available):
        sudo(u'ln -s -f %s %s' % (site_available, site_enabled))
        restart_service(u'nginx')
    else:
        abort(u'%s site configuration is not available' % site_name)


@task
def disable_site(site_name):
    """Disables Nginx site configuration."""

    site = u'/etc/nginx/sites-enabled/%s' % site_name
    if files.exists(site):
        sudo(u'rm %s' % site)
        restart_service(u'nginx')
