#!/usr/bin/env python

from distutils.core import setup

setup(name='uesyllabus',
      version='0.1',
      description='get UEC Syllabus Data',
      author='suzu',
      author_email='suzuzusu123@icloud.com',
      packages=['uesyllabus'],
      package_data={'uesyllabus': ['resource/*.json']},
      scripts=['bin/uesyllabus']
     )
