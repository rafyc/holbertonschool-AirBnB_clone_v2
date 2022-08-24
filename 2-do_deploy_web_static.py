#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local, run
from datetime import datetime
import os

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
    '''
    Function that distributes an archive to your web servers
    '''
    if os.path.exists(archive_path) == False:
        return False
    run('scp -o StrictHostKeyChecking=no -i /etc/ssh/school archive_path ubuntu@54.147.180.101:/tmp')
    run('scp -o StrictHostKeyChecking=no -i /etc/ssh/school archive_path ubuntu@54.147.180.101:/tmp')
