#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    name='pycookiecutter',
    packages=find_packages(include=['pycookiecutter']),
    url='https://github.com/mqlab-dev/pycookiecutter',
    version='0.1.0',
    author="Qiong X. Michaels",
    author_email='qiong@mqlab.dev',
    license="BSD license",
    description="Starting template for creating a Python package.",
    long_description=readme + '\n\n' + history,
    keywords=['cookiecutter', 'template', 'package', ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development',
    ]
)
