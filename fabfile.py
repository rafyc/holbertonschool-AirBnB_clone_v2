#!/usr/bin/ python3
from fabric.api import *

def anonymous():
    run("uname -a")
