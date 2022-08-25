#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz
archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import local, put, run, env
from datetime import datetime
from os.path import exists
env.hosts = ['54.209.251.89', '54.147.180.101']


def do_deploy(archive_path):
    """ deploy archive on server """
    if exists(archive_path) is False:
        return False
    try:
        filename = archive_path.split('/')[-1]
        fname_noext = filename.split('.')[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, fname_noext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(filename, path, fname_noext))
        run('rm /tmp/{}'.format(filename))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, fname_noext))
        run('rm -rf {}{}/web_static'.format(path, fname_noext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, fname_noext))
        print("New version deployed!")
        return True
    except Exception:
        return False
