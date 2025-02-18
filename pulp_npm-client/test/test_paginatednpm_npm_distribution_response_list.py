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
import datetime

import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.models.paginatednpm_npm_distribution_response_list import PaginatednpmNpmDistributionResponseList  # noqa: E501
from pulpcore.client.pulp_npm.rest import ApiException

class TestPaginatednpmNpmDistributionResponseList(unittest.TestCase):
    """PaginatednpmNpmDistributionResponseList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaginatednpmNpmDistributionResponseList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = pulpcore.client.pulp_npm.models.paginatednpm_npm_distribution_response_list.PaginatednpmNpmDistributionResponseList()  # noqa: E501
        if include_optional :
            return PaginatednpmNpmDistributionResponseList(
                count = 123, 
                next = 'http://api.example.org/accounts/?offset=400&limit=100', 
                previous = 'http://api.example.org/accounts/?offset=200&limit=100', 
                results = [
                    pulpcore.client.pulp_npm.models.npm/npm_distribution_response.npm.NpmDistributionResponse(
                        pulp_href = '0', 
                        prn = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        base_path = '0', 
                        base_url = '0', 
                        content_guard = '0', 
                        no_content_change_since = '0', 
                        hidden = True, 
                        pulp_labels = {
                            'key' : '0'
                            }, 
                        name = '0', 
                        repository = '0', )
                    ]
            )
        else :
            return PaginatednpmNpmDistributionResponseList(
                count = 123,
                results = [
                    pulpcore.client.pulp_npm.models.npm/npm_distribution_response.npm.NpmDistributionResponse(
                        pulp_href = '0', 
                        prn = '0', 
                        pulp_created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        pulp_last_updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        base_path = '0', 
                        base_url = '0', 
                        content_guard = '0', 
                        no_content_change_since = '0', 
                        hidden = True, 
                        pulp_labels = {
                            'key' : '0'
                            }, 
                        name = '0', 
                        repository = '0', )
                    ],
        )

    def testPaginatednpmNpmDistributionResponseList(self):
        """Test PaginatednpmNpmDistributionResponseList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
