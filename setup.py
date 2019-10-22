import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

requires = ["requests == 2.20.0"]

setup(
    name='pystex',
    version='0.0.20',
    description='Python StackExchange API Client',
    author='Steven Cheng',
    author_email='stevenc81@gmail.com',
    url='https://github.com/stevenc81/pystex',
    packages=['pystex'],
    package_data={'': ['LICENSE']},
    install_requires=requires,
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    'Topic :: Software Development :: Libraries :: Python Modules',
    ],
 )


