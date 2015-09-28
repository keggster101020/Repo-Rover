#!/usr/bin/env python

from setuptools import setup

version = '1.0'

setup(name='repo_rover',
      version=version,
      description='Take back control of your unruly git repositories.',
      author='Cody Kinneer, Keegan Shudy',
      author_email='kinneerc@allegheny.edu',
      url='https://github.com/keggster101020/Repo-Rover',
      packages=['repo_rover'],
      package_data={'repo_rover':['*.html','*.css']},
      scripts=['repo_rover/reporover'],
      classifiers=['Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Version Control',]
     )
