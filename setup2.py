from setuptools import setup

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(name='biotrack',
      version='0.1',
      description='See changes in UniProt to protein components of a model.',
      long_description=readme(),
      url='https://boo62@bitbucket.org/boo62/biotrack.git',
      author='Daniel Boocock',
      author_email='daniel.boocock@protonmail.ch',
      licence='',
      packages=["biotrack", "tests"],
      scripts=["bin/modcomp"],
      install_requires=[
          'biopython',
      ],
      test_suite="tests",
      test_require=['pytest'],
      zip_safe=False)
