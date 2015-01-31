#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='amazon-echo',
    version='0.1',

    description='Amazon Echo Python API',
    url='https://github.com/nmercer/echo-python',

    author='Nicholas John Mercer',
    author_email='nm3rc3r@gmail.com',

    packages = find_packages(),
    license='MIT',

    install_requires = [
        "beautifulsoup4",
        "requests"
    ],
    include_package_data = True,
)
