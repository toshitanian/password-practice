#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def _load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()]


def _install_requires():
    requires = _load_requires_from_file('requirements.txt')
    return requires


def _test_requires():
    test_requires = _load_requires_from_file('test-requirements.txt')
    return test_requires


def _packages():
    return find_packages(
        exclude=[
            '*.tests',
            '*.tests.*',
            'tests.*',
            'tests'
        ],
    )


if __name__ == '__main__':
    description = ''
    setup(
        name='password-practice',
        version='v1.0',
        description=description,
        author='Toshiya Kawasaki',
        author_email='kawasakitoshiya@gmail.com',
        classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
        ],
        packages=_packages(),
        install_requires=_install_requires(),
        tests_require=_test_requires(),
        test_suite='nose.collector',
        include_package_data=True,
        zip_safe=False,
        entry_points="""
        [console_scripts]
        password-practice = main:main
        """,
    )
