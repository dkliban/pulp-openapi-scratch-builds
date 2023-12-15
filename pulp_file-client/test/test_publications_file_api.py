# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import pulpcore.client.pulp_file
from pulpcore.client.pulp_file.api.publications_file_api import PublicationsFileApi  # noqa: E501
from pulpcore.client.pulp_file.rest import ApiException


class TestPublicationsFileApi(unittest.TestCase):
    """PublicationsFileApi unit test stubs"""

    def setUp(self):
        self.api = pulpcore.client.pulp_file.api.publications_file_api.PublicationsFileApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_role(self):
        """Test case for add_role

        Add a role  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create a file publication  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a file publication  # noqa: E501
        """
        pass

    def test_list(self):
        """Test case for list

        List file publications  # noqa: E501
        """
        pass

    def test_list_roles(self):
        """Test case for list_roles

        List roles  # noqa: E501
        """
        pass

    def test_my_permissions(self):
        """Test case for my_permissions

        List user permissions  # noqa: E501
        """
        pass

    def test_read(self):
        """Test case for read

        Inspect a file publication  # noqa: E501
        """
        pass

    def test_remove_role(self):
        """Test case for remove_role

        Remove a role  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()