#!/usr/bin/env python
# -*- coding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="number-to-text",
    version="0.0.4",
    author="Hasan Budak",
    author_email="budak.hasan.apc@gmail.com",
    description="Helps you convert to numbers to text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AOF-BudakHasan/number_to_text",
    packages=setuptools.find_packages(exclude=['tests', 'test.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"number_to_text": "number_to_text"},
    python_requires='>=3.0',
    test_suite='tests',
    setup_requires=['wheel'],
    include_package_data=True
)
