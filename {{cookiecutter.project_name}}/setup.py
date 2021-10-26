#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''The setup script for {{cookiecutter.project_name}}'''

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

# Load our Requirements files
extra_require_files = dict()
for file_prefix in ['', 'dev_', 'build_']:
    filename = f'{file_prefix}requirements'
    with open(f'{filename}.txt') as requirements_file:
        fk = file_prefix.strip('_') if file_prefix else filename
        lines = requirements_file.read().split('\n')
        extra_require_files[fk] = []
        for line in lines:
            line = line.strip()
            if line and (line[0] != '-') and (line[0] != '#'):
                extra_require_files[fk].append(line)

build_requirements = extra_require_files['build']
test_requirements = extra_require_files['dev'] + build_requirements

extras = dict(test=test_requirements, packaging=build_requirements, dev=extra_require_files['dev'])


authors = [
    ('Institute for Disease Modeling - RSE Team', 'SWResearch@idmod.org')
]

setup(
    author=[author[0] for author in authors],
    author_email=[author[1] for author in authors],
    license = 'Creative Commons Attribution-ShareAlike 4.0',
    classifiers=[
        'License :: Creative Commons Attribution-ShareAlike 4.0',
        'Programming Language :: Python :: 3.9'
    ],
    description='{{cookiecutter.project_description}}',
    install_requires=extra_require_files['requirements'],
    long_description=readme,
    include_package_data=True,
    keywords='modeling, IDM',
    name='{{cookiecutter.project_name}}',
    packages=find_packages(),
    setup_requires=[],
    python_requires='>=3.9.*',
    test_suite='tests',
    extras_require=extras,
    version='0.0.1'
)