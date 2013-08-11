import pystex

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='pystex',
    version=pystex.__version__,
    description='Python StackExchange API Client',
    author='Steven Cheng',
    author_email='stevenc81@gmail.com',
    url='https://github.com/stevenc81/pystex',
    packages=['pystex'],
 )

