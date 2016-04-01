# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

entry_points = {
    "console_scripts": [
        "p2a = phone2address.cli:main",
    ]
}

setup(
    name="phone2address",
    version="0.0.2",
    url="https://xuanwo.org/",
    author="Xuanwo",
    author_email="xuanwo.cn@gmail.com",
    description="phone2address is a tool for phone number address.",
    long_description="phone2address is a tool for phone number address.",
    keywords="phone, address, script",
    license="MIT License",
    packages=find_packages(),
    include_package_data=True,
    entry_points=entry_points,
    install_requires=[
        'docopt',
        'openpyxl',
        'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
    ],
)