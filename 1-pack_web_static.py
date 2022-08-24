#!/usr/bin/env python3
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
    file_name =  "versions/web_static_{}{}{}{}{}{}.tgz".format(time("%Y"),
                                                                  time("%m"),
                                                                  time("%d"),
                                                                  time("%H"),
                                                                  time("%M"),
                                                                  time("%S"))
    try:
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception:
        return None
