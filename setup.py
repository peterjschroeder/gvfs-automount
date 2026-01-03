#!/usr/bin/env python3

from distutils.core import setup

setup(
        name='gvfs_automount', 
        version='0.1', 
        description='Simple auto-mounting daemon for gvfs. ', 
        author='Laurence Gonsalves', 
        url='https://github.com/peterjschroeder/gvfs-automount',
        scripts=['gvfs_automount'],
        install_requires=[]
)

