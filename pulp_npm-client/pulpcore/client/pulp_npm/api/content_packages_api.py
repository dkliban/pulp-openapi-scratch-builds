# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pulpcore.client.pulp_npm.api_client import ApiClient
from pulpcore.client.pulp_npm.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ContentPackagesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create(self, relative_path, name, version, pulp_domain="default", **kwargs):  # noqa: E501
        """Create a package  # noqa: E501

        Perform bookkeeping when saving Content.  \"Artifacts\" need to be popped off and saved independently, as they are not actually part of the Content model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(pulp_domain, relative_path, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param str relative_path: (required)
        :param str name: (required)
        :param str version: (required)
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param str artifact: Artifact file representing the physical content
        :param file file: An uploaded file that may be turned into the content unit.
        :param str upload: An uncommitted upload that may be turned into the content unit.
        :param str file_url: A url that Pulp can download and turn into the content unit.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NpmPackageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(relative_path, name, version, pulp_domain=pulp_domain, **kwargs)  # noqa: E501

    def create_with_http_info(self, relative_path, name, version, pulp_domain="default", **kwargs):  # noqa: E501
        """Create a package  # noqa: E501

        Perform bookkeeping when saving Content.  \"Artifacts\" need to be popped off and saved independently, as they are not actually part of the Content model.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(pulp_domain, relative_path, name, version, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param str relative_path: (required)
        :param str name: (required)
        :param str version: (required)
        :param str repository: A URI of a repository the new content unit should be associated with.
        :param str artifact: Artifact file representing the physical content
        :param file file: An uploaded file that may be turned into the content unit.
        :param str upload: An uncommitted upload that may be turned into the content unit.
        :param str file_url: A url that Pulp can download and turn into the content unit.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NpmPackageResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'pulp_domain',
            'relative_path',
            'name',
            'version',
            'repository',
            'artifact',
            'file',
            'upload',
            'file_url'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pulp_domain' is set
        if self.api_client.client_side_validation and ('pulp_domain' not in local_var_params or  # noqa: E501
                                                        local_var_params['pulp_domain'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pulp_domain` when calling `create`")  # noqa: E501
        # verify the required parameter 'relative_path' is set
        if self.api_client.client_side_validation and ('relative_path' not in local_var_params or  # noqa: E501
                                                        local_var_params['relative_path'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `relative_path` when calling `create`")  # noqa: E501
        # verify the required parameter 'name' is set
        if self.api_client.client_side_validation and ('name' not in local_var_params or  # noqa: E501
                                                        local_var_params['name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `name` when calling `create`")  # noqa: E501
        # verify the required parameter 'version' is set
        if self.api_client.client_side_validation and ('version' not in local_var_params or  # noqa: E501
                                                        local_var_params['version'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `version` when calling `create`")  # noqa: E501

        if self.api_client.client_side_validation and ('relative_path' in local_var_params and  # noqa: E501
                                                        len(local_var_params['relative_path']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `relative_path` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('name' in local_var_params and  # noqa: E501
                                                        len(local_var_params['name']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `name` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('version' in local_var_params and  # noqa: E501
                                                        len(local_var_params['version']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `version` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        if self.api_client.client_side_validation and ('file_url' in local_var_params and  # noqa: E501
                                                        len(local_var_params['file_url']) < 1):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `file_url` when calling `create`, length must be greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'pulp_domain' in local_var_params:
            path_params['pulp_domain'] = local_var_params['pulp_domain']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'repository' in local_var_params:
            form_params.append(('repository', local_var_params['repository']))  # noqa: E501
        if 'artifact' in local_var_params:
            form_params.append(('artifact', local_var_params['artifact']))  # noqa: E501
        if 'relative_path' in local_var_params:
            form_params.append(('relative_path', local_var_params['relative_path']))  # noqa: E501
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'upload' in local_var_params:
            form_params.append(('upload', local_var_params['upload']))  # noqa: E501
        if 'file_url' in local_var_params:
            form_params.append(('file_url', local_var_params['file_url']))  # noqa: E501
        if 'name' in local_var_params:
            form_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'version' in local_var_params:
            form_params.append(('version', local_var_params['version']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth', 'json_header_remote_authentication']  # noqa: E501

        return self.api_client.call_api(
            '/api/pulp/{pulp_domain}/api/v3/content/npm/packages/', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NpmPackageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, pulp_domain="default", **kwargs):  # noqa: E501
        """List packages  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/npm/units/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(pulp_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `version` - Version * `-version` - Version (descending) * `pk` - Pk * `-pk` - Pk (descending)
        :param float orphaned_for: Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.
        :param list[str] prn__in: Multiple values may be separated by commas.
        :param list[str] pulp_href__in: Multiple values may be separated by commas.
        :param list[str] pulp_id__in: Multiple values may be separated by commas.
        :param str q: Filter results by using NOT, AND and OR operations on other filters
        :param str repository_version: Repository Version referenced by HREF/PRN
        :param str repository_version_added: Repository Version referenced by HREF/PRN
        :param str repository_version_removed: Repository Version referenced by HREF/PRN
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PaginatednpmPackageResponseList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.list_with_http_info(pulp_domain=pulp_domain, **kwargs)  # noqa: E501

    def list_with_http_info(self, pulp_domain="default", **kwargs):  # noqa: E501
        """List packages  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/npm/units/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(pulp_domain, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str pulp_domain: (required)
        :param int limit: Number of results to return per page.
        :param str name: Filter results where name matches value
        :param list[str] name__in: Filter results where name is in a comma-separated list of values
        :param int offset: The initial index from which to return the results.
        :param list[str] ordering: Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `upstream_id` - Upstream id * `-upstream_id` - Upstream id (descending) * `timestamp_of_interest` - Timestamp of interest * `-timestamp_of_interest` - Timestamp of interest (descending) * `name` - Name * `-name` - Name (descending) * `version` - Version * `-version` - Version (descending) * `pk` - Pk * `-pk` - Pk (descending)
        :param float orphaned_for: Minutes Content has been orphaned for. -1 uses ORPHAN_PROTECTION_TIME.
        :param list[str] prn__in: Multiple values may be separated by commas.
        :param list[str] pulp_href__in: Multiple values may be separated by commas.
        :param list[str] pulp_id__in: Multiple values may be separated by commas.
        :param str q: Filter results by using NOT, AND and OR operations on other filters
        :param str repository_version: Repository Version referenced by HREF/PRN
        :param str repository_version_added: Repository Version referenced by HREF/PRN
        :param str repository_version_removed: Repository Version referenced by HREF/PRN
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PaginatednpmPackageResponseList, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'pulp_domain',
            'limit',
            'name',
            'name__in',
            'offset',
            'ordering',
            'orphaned_for',
            'prn__in',
            'pulp_href__in',
            'pulp_id__in',
            'q',
            'repository_version',
            'repository_version_added',
            'repository_version_removed',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'pulp_domain' is set
        if self.api_client.client_side_validation and ('pulp_domain' not in local_var_params or  # noqa: E501
                                                        local_var_params['pulp_domain'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pulp_domain` when calling `list`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pulp_domain' in local_var_params:
            path_params['pulp_domain'] = local_var_params['pulp_domain']  # noqa: E501

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name__in' in local_var_params and local_var_params['name__in'] is not None:  # noqa: E501
            query_params.append(('name__in', local_var_params['name__in']))  # noqa: E501
            collection_formats['name__in'] = 'csv'  # noqa: E501
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'ordering' in local_var_params and local_var_params['ordering'] is not None:  # noqa: E501
            query_params.append(('ordering', local_var_params['ordering']))  # noqa: E501
            collection_formats['ordering'] = 'csv'  # noqa: E501
        if 'orphaned_for' in local_var_params and local_var_params['orphaned_for'] is not None:  # noqa: E501
            query_params.append(('orphaned_for', local_var_params['orphaned_for']))  # noqa: E501
        if 'prn__in' in local_var_params and local_var_params['prn__in'] is not None:  # noqa: E501
            query_params.append(('prn__in', local_var_params['prn__in']))  # noqa: E501
            collection_formats['prn__in'] = 'csv'  # noqa: E501
        if 'pulp_href__in' in local_var_params and local_var_params['pulp_href__in'] is not None:  # noqa: E501
            query_params.append(('pulp_href__in', local_var_params['pulp_href__in']))  # noqa: E501
            collection_formats['pulp_href__in'] = 'csv'  # noqa: E501
        if 'pulp_id__in' in local_var_params and local_var_params['pulp_id__in'] is not None:  # noqa: E501
            query_params.append(('pulp_id__in', local_var_params['pulp_id__in']))  # noqa: E501
            collection_formats['pulp_id__in'] = 'csv'  # noqa: E501
        if 'q' in local_var_params and local_var_params['q'] is not None:  # noqa: E501
            query_params.append(('q', local_var_params['q']))  # noqa: E501
        if 'repository_version' in local_var_params and local_var_params['repository_version'] is not None:  # noqa: E501
            query_params.append(('repository_version', local_var_params['repository_version']))  # noqa: E501
        if 'repository_version_added' in local_var_params and local_var_params['repository_version_added'] is not None:  # noqa: E501
            query_params.append(('repository_version_added', local_var_params['repository_version_added']))  # noqa: E501
        if 'repository_version_removed' in local_var_params and local_var_params['repository_version_removed'] is not None:  # noqa: E501
            query_params.append(('repository_version_removed', local_var_params['repository_version_removed']))  # noqa: E501
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth', 'json_header_remote_authentication']  # noqa: E501

        return self.api_client.call_api(
            '/api/pulp/{pulp_domain}/api/v3/content/npm/packages/', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaginatednpmPackageResponseList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, npm_package_href,  **kwargs):  # noqa: E501
        """Inspect a package  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/npm/units/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(npm_package_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str npm_package_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NpmPackageResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.read_with_http_info(npm_package_href,  **kwargs)  # noqa: E501

    def read_with_http_info(self, npm_package_href,  **kwargs):  # noqa: E501
        """Inspect a package  # noqa: E501

        A ViewSet for Package.  Define endpoint name which will appear in the API endpoint for this content type. For example::     http://pulp.example.com/pulp/api/v3/content/npm/units/  Also specify queryset and serializer for Package.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(npm_package_href, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str npm_package_href: (required)
        :param list[str] fields: A list of fields to include in the response.
        :param list[str] exclude_fields: A list of fields to exclude from the response.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NpmPackageResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'npm_package_href',
            'fields',
            'exclude_fields'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'npm_package_href' is set
        if self.api_client.client_side_validation and ('npm_package_href' not in local_var_params or  # noqa: E501
                                                        local_var_params['npm_package_href'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `npm_package_href` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'npm_package_href' in local_var_params:
            path_params['npm_package_href'] = local_var_params['npm_package_href']  # noqa: E501

        query_params = []
        if 'fields' in local_var_params and local_var_params['fields'] is not None:  # noqa: E501
            query_params.append(('fields', local_var_params['fields']))  # noqa: E501
            collection_formats['fields'] = 'multi'  # noqa: E501
        if 'exclude_fields' in local_var_params and local_var_params['exclude_fields'] is not None:  # noqa: E501
            query_params.append(('exclude_fields', local_var_params['exclude_fields']))  # noqa: E501
            collection_formats['exclude_fields'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth', 'cookieAuth', 'json_header_remote_authentication']  # noqa: E501

        return self.api_client.call_api(
            '{npm_package_href}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NpmPackageResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
