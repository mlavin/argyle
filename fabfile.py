"""
This is an example fabfile to test out the functionality in
argyle. It connects and runs commands on a VM provisioned using
Vagrant.
"""

from fabric.api import env, run, task

import argyle.nginx
import argyle.system


env.user = 'vagrant'
env.key_filename = '/usr/lib/ruby/gems/1.8/gems/vagrant-0.8.7/keys/vagrant'
env.hosts = ['33.33.33.10', ]


@task
def test():
    run('uname -s')   
