# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os


# with open(os.path.join('VERSION')) as f:
#     version = f.read().strip()


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pytest_framework',
    version="1.0",
    packages=find_packages(),
    # package_data={
    #     '': ['README.md', 'VERSION', 'requirements.txt', 'MANIFEST.in']
    # },
    author="Bo Xiao",
    author_email="x17621500741@gmail.com",
    description="pytest framework for test",
    # long_description=read('README.md'),
    include_package_data=True,
    platforms="linux,windows",
    entry_points={'pytest11': [
        'pytest_framework = pytest_framework.utils.common',
        'pytest_framework = pytest_framework.utils.common2'
    ]}  # must add the plugin file or package
)
# Build CMD    python setup.py build
# Packaging CMD python setup.py sdist
