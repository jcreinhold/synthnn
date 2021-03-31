#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup

Module installs the synthtorch package
Can be run via command: python setup.py install (or develop)

Author: Jacob Reinhold (jacob.reinhold@jhu.edu)

Created on: Nov 2, 2018
"""

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

version = '0.3.10'

args = dict(
    name='synthtorch',
    version=version,
    description="pytorch-based image synthesis",
    long_description=readme,
    author='Jacob Reinhold',
    author_email='jacob.reinhold@jhu.edu',
    url='https://gitlab.com/jcreinhold/synthtorch',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'tutorials')),
    keywords="mr image-synthesis",
    entry_points={
        'console_scripts': ['nn-train=synthtorch.exec.nn_train:main',
                            'nn-predict=synthtorch.exec.nn_predict:main']
    },
    dependency_links=[f'git+git://github.com/jcreinhold/niftidataset.git@master#egg=niftidataset-0.1.4']
)

setup(install_requires=['matplotlib',
                        'nibabel>=2.3.1',
                        'niftidataset>=0.1.4',
                        'numpy>=1.15.4',
                        'pillow>=5.3.0'
                        'torch>=1.1.0',
                        'torchvision>=0.2.2'], **args)
