Nginx Functions
======================================

Nginx is an awesome webserver and these are functions to help manage site
configurations.


.. function:: remove_default_site()

    Nginx installs with a default server listening on 80 defined in
    ``/etc/nginx/sites-enabled/default.conf``. This task removes that configuration.


.. function:: upload_nginx_site_conf(site_name, template_name=None, context=None, enable=True)

    This task uploads a new configuration to ``/etc/nginx/sites-available/<site_name>``. This
    looks for a template named ``nginx/<site_name>.conf`` and if not found uploads the default
    ``nginx/site.conf`` unless ``template_name`` is given. By default this site configuration 
    will be enabled ``/etc/nginx/sites-enabled/``.


.. function:: enable_site(site_name)

    Enables a site in ``/etc/nginx/sites-available/<site_name>`` and links it to
    ``/etc/nginx/sites-enabled/<site_name>``.


.. function:: disable_site(site_name)

    Disables a site in ``/etc/nginx/sites-enabled/`` by the name. The configuration in
    ``/etc/nginx/sites-available/`` is not touched.
