#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz
archive from the contents of the web_static folder
of your AirBnB Clone repo, using the function do_pack."""

from fabric.api import local, put, env, run
from datetime import datetime
from os.path import exists

env.hosts = ['54.209.251.89', '54.147.180.101']

def do_pack():
    """
    function that create an archiv .tgz
    """
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    local('mkdir -p versions')
    file_name = 'versions/web_static_{}.tgz'.format(time)
    try:
        local('tar -czvf {} web_static'.format(file_name))
        return file_name
    except Exception:
        return None

def do_deploy(archive_path):
    """ The function do_deploy """
    if not exists(archive_path):
        return False
    try:
        """archive_path = versions/web_static_20170315003959.tgz """
        file_name = archive_path.split("/")[-1]
        """file_name = web_static_20170315003959.tgz"""
        file_with_no_ext = file_name.split(".")[0]
        """file_with_no_ext = web_static_20170315003959"""
        path = "/data/web_static/releases/"
        """Upload the archive to the /tmp/ directory of the web server"""
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, file_with_no_ext))
        """Uncompress the archive"""
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, file_with_no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, file_with_no_ext))
        run('rm -rf {}{}/web_static'.format(path, file_with_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, file_with_no_ext))
        return True
    except Exception:
        return False
