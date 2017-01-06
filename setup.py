# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name="PROJECT",
    version="0.0.1",
    description="A fancy description of PROJECT",
    long_description=readme,
    author="Author's name",
    url="URL where the project is hosted",
    download_url="Where to download it",
    author_email="Author's email",
    install_requires=["nose"],
    scripts=[],
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
