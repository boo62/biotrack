try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'version': '0.1',
    'description': 'See changes in UniProt to protein components of a model.',
    'url': 'https://boo62@bitbucket.org/boo62/biotrack.git',
    'author': 'Daniel Boocock',
    'author_email': 'daniel.boocock@protonmail.ch',
    'licence': ''  
    'install_requires': [],
    'packages': ["biotrack", "tests"],
    'scripts': ["bin/modcomp"],
    'name': 'biotrack'
}

setup(**config)
