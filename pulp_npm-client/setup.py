# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "pulp_npm-client"
VERSION = "0.1.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]
setup(
    name=NAME,
    version=VERSION,
    description="Pulp 3 API",
    author="Pulp Team",
    author_email="pulp-list@redhat.com",
    url="",
    keywords=["pulp", "pulpcore", "client", "Pulp 3 API"],
    install_requires=REQUIRES,
    python_requires='>=3.4',  # restrict client usage to Python 3 only
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    license="GPLv2+",
    long_description="""\
    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501
    """
)
