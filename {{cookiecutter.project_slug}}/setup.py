#!/usr/bin/env python3

"""The setup script."""

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()
with open('HISTORY.rst') as history_file:
    history = history_file.read()


name = '{{ cookiecutter.project_slug }}'
version = '{{ cookiecutter.version }}'
url = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}'
author = "{{ cookiecutter.full_name.replace('\"', '\\\"') }}"
author_email = '{{ cookiecutter.email }}'
description = '{{ cookiecutter.project_short_description }}'
requirements = [{% if cookiecutter.command_line_interface|lower == 'click' %}'Click>=6.0', {% endif %}]
setup_requirements = [{% if cookiecutter.use_pytest == 'y' %}'pytest-runner', {% endif %}]
test_requirements = [{% if cookiecutter.use_pytest == 'y' %}'pytest', {% endif %}]
console_scripts = [
    '{{ cookiecutter.project_slug }}={{ cookiecutter.project_slug }}.cli:main',
]

{%- set licenses=(
    'MIT license',
    'BSD license',
    'ISC license',
    'Apache Software License 2.0',
    'GNU General Public License v3'
    )
%}


setup(
    name=name,
    version=version,
    url=url,
    author=author,
    author_email=author_email,
    {%- if cookiecutter.open_source_license in licenses %}
    license='{{ cookiecutter.open_source_license }}',
    {%- endif %}
    description=description,
    long_description=readme + '\n\n' + history,
    packages=find_packages(include=['{{ cookiecutter.project_slug }}']),
    setup_requires=setup_requirements,
    install_requires=requirements,
    tests_require=test_requirements,
    include_package_data=True,
    zip_safe=False,
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    entry_points={'console_scripts': console_scripts, },
    {%- endif %}
    classifiers=[
        {%- if cookiecutter.open_source_license != "Not open source" %}
        'License :: OSI Approved :: {{ cookiecutter.open_source_license }}',
        {%- endif %}
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
