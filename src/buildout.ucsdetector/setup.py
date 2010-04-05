from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='buildout.ucsdetector',
      version=version,
      description="A buildout extensions that enable set diferent dependency links to install eggs.",
      long_description="""\
""",
      classifiers=[
          "Framework :: Buildout ",
          "Intended Audience :: Developers ",
          "Topic :: Software Development :: Build Tools ",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      keywords='buildout ucs extension',
      author='Diego Manh\xc3\xa3es Pinheiro',
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
      tests_require=[
          'zc.buildout',
      ],
      test_suite = "buildout.ucsdetector.tests",
      entry_points={
          'zc.buildout.extension': ['ext = buildout.ucsdetector:ext'],
          'zc.buildout.unloadextension': ['ext = buildout.ucsdetector:unload']
          }
      )
