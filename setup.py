from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()


def get_requirements(filename):
    with open(filename) as f:
        return f.read().splitlines()


setup(name='wscelery',
      version='0.1.0',
      # Autor detauls
      author='Antonis Kalou',
      author_email='antonis@johan-sports.com',
      # Project details
      description='Real time celery monitoring using websockets',
      long_description=long_description,
      url='https://github.com/johan-sports/wscelery',
      license='MIT',

      classifiers=[
          # Project maturity
          'Development Status :: 3 - Alpha',

          # Intended audience
          'Intended Audience :: Developers',
          'Topic :: System :: Distributed Computing',

          # License
          'License :: OSI Approved :: MIT License',

          # Supported python versions
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
          'Operating System :: OS Independent',
      ],
      keywords=['celery', 'websocket', 'monitoring'],
      packages=find_packages(exclude=['tests', 'tests.*']),
      install_requires=get_requirements('requirements.txt'),
      test_suite='wscelery.tests',
      tests_require=get_requirements('test-requirements.txt'),
      entry_points={
          'console_scripts': [
              'wscelery = wscelery.__main__:main',
          ],
          'celery.commands': [
              'wscelery = wscelery.command:WsCeleryCommand',
          ]
      })
