#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys, os, imp
from setuptools import setup, find_packages
from pkg_resources import resource_string

VERSION = '0.5'

MODULE_NAME='buildout.ucsdetector'
README = resource_string(MODULE_NAME, 'README.txt')
parent_directory = os.path.dirname(__file__)
CHANGES = open(os.path.join(parent_directory, "CHANGES.txt")).read()


setup(name=MODULE_NAME,
      version=VERSION,
      description="A buildout extension that enables dependency links\
      to install eggs according to the UCS(Unicode Character Set)\
      version of the python distribution.",
      long_description=README,
      classifiers=[
          "Framework :: Buildout",
          "Intended Audience :: Developers",
          "Topic :: Software Development :: Build Tools",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='buildout ucs extension',
      author='Diego Manhães Pinheiro',
      author_email='dmpinheiro@gmail.com',
      url='http://github.com/dmpinheiro/buildout.ucsdetector',
      license='MIT',
      namespace_packages = ['buildout'],
      packages=find_packages(exclude=['distribute_setup']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
          'zc.buildout',
      ],
      test_suite = MODULE_NAME+".tests.test_suite",
      entry_points="""
          [zc.buildout.extension]
          default=buildout.ucsdetector:detect
          """
      )
