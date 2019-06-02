#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages
import versioneer

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


name = 'pycookiecutter'
packages = find_packages()
url = 'https://github.com/mqlab-dev/pycookiecutter'
version = versioneer.get_version()
cmdclass = versioneer.get_cmdclass()
author = "Qiong X. Michaels"
author_email = 'qiong@mqlab.dev'
description = "Starting template for creating a Python package."
keywords = ['cookiecutter', 'template', 'package']
requirements = ['versioneer==0.18', ]
setup_requirements = ['pytest-runner', ]
test_requirements = ['pytest', ]


setup(
    name=name,
    packages=packages,
    url=url,
    version=version,
    cmdclass=cmdclass,
    author=author,
    author_email=author_email,
    license="BSD license",
    description=description,
    setup_requires=setup_requirements,
    install_requires=requirements,
    tests_require=test_requirements,
    long_description=readme + '\n\n' + history,
    keywords=keywords,
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
