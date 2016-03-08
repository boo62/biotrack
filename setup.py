try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Track changes in databases to components in a model.',
    'author': 'Daniel Boocock',
    'url': 'https://boo62@bitbucket.org/boo62/biotrack.git',
    'download_url': 'https://boo62@bitbucket.org/boo62/biotrack.git',
    'author_email': 'daniel.boocock@protonmail.ch',
    'version': '0.1',
    'install_requires': [],
    'packages': [],
    'scripts': [],
    'name': 'biotrack'
}

setup(**config)
