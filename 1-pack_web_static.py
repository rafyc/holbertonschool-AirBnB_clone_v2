#!/usr/bin/python3
"""
script that generates a .tgz archive from the contents of the web_static
folder of your AirBnB Clone repo, using the function do_pack.
"""

from fabric.api import local
from datetime import datetime

def do_pack():
    """
    function that create an archiv .tgz
    """
    time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    local('mkdir -p versions')
    file_name = f'version/web_static_{time}.tgz'
    try:
        local(f'tar -czvf {file_name} web_static')
        return file_name
    except Exception:
        return None
