#!/usr/bin/env python

from setuptools import find_packages, setup


with open("README.md") as fp:
    long_description = fp.read()

with open("requirements.txt") as _file:
    install_reqs = []
    dependency_links = []
    for req in _file.readlines():

        if req.startswith("--extra-index-url"):
            dependency_links.append(req.replace("--extra-index-url ", ""))
        else:
            install_reqs.append(req)

with open("tests/requirements.txt") as _file:
    test_reqs = [req for req in _file.readlines()]

setup(
    name="lit_rstudio",
    version="0.0.1",
    description="RStudio component for ⚡",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Krishna",
    author_email="krishna@lightning.ai",
    url="https://github.com/krishnakalyan3/rstudio_component",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=install_reqs,
    dependency_links=dependency_links,
    extras_require={
        "test": test_reqs,
    },
    python_requires=">=3.7",
)
