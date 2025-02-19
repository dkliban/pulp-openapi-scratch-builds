# pulpcore.client.pulp_npm.RepositoriesNpmApi

All URIs are relative to *https://console.stage.redhat.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](RepositoriesNpmApi.md#create) | **POST** /api/pulp/{pulp_domain}/api/v3/repositories/npm/npm/ | Create a npm repository
[**delete**](RepositoriesNpmApi.md#delete) | **DELETE** {npm_npm_repository_href} | Delete a npm repository
[**list**](RepositoriesNpmApi.md#list) | **GET** /api/pulp/{pulp_domain}/api/v3/repositories/npm/npm/ | List npm repositorys
[**modify**](RepositoriesNpmApi.md#modify) | **POST** {npm_npm_repository_href}modify/ | Modify Repository Content
[**partial_update**](RepositoriesNpmApi.md#partial_update) | **PATCH** {npm_npm_repository_href} | Update a npm repository
[**read**](RepositoriesNpmApi.md#read) | **GET** {npm_npm_repository_href} | Inspect a npm repository
[**set_label**](RepositoriesNpmApi.md#set_label) | **POST** {npm_npm_repository_href}set_label/ | Set a label
[**sync**](RepositoriesNpmApi.md#sync) | **POST** {npm_npm_repository_href}sync/ | Sync from remote
[**unset_label**](RepositoriesNpmApi.md#unset_label) | **POST** {npm_npm_repository_href}unset_label/ | Unset a label
[**update**](RepositoriesNpmApi.md#update) | **PUT** {npm_npm_repository_href} | Update a npm repository


# **create**
> NpmNpmRepositoryResponse create(pulp_domain, npm_npm_repository)

Create a npm repository

A ViewSet for NpmRepository.  Similar to the PackageViewSet above, define endpoint_name, queryset and serializer, at a minimum.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
npm_npm_repository = pulpcore.client.pulp_npm.NpmNpmRepository() # NpmNpmRepository | 

    try:
        # Create a npm repository
        api_response = api_instance.create(pulp_domain, npm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->create: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
npm_npm_repository = pulpcore.client.pulp_npm.NpmNpmRepository() # NpmNpmRepository | 

    try:
        # Create a npm repository
        api_response = api_instance.create(pulp_domain, npm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->create: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
npm_npm_repository = pulpcore.client.pulp_npm.NpmNpmRepository() # NpmNpmRepository | 

    try:
        # Create a npm repository
        api_response = api_instance.create(pulp_domain, npm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **npm_npm_repository** | [**NpmNpmRepository**](NpmNpmRepository.md)|  | 

### Return type

[**NpmNpmRepositoryResponse**](NpmNpmRepositoryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> AsyncOperationResponse delete(npm_npm_repository_href)

Delete a npm repository

Trigger an asynchronous delete task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 

    try:
        # Delete a npm repository
        api_response = api_instance.delete(npm_npm_repository_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->delete: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 

    try:
        # Delete a npm repository
        api_response = api_instance.delete(npm_npm_repository_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->delete: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 

    try:
        # Delete a npm repository
        api_response = api_instance.delete(npm_npm_repository_href)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> PaginatednpmNpmRepositoryResponseList list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)

List npm repositorys

A ViewSet for NpmRepository.  Similar to the PackageViewSet above, define endpoint_name, queryset and serializer, at a minimum.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
latest_with_content = 'latest_with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `description` - Description * `-description` - Description (descending) * `next_version` - Next version * `-next_version` - Next version (descending) * `retain_repo_versions` - Retain repo versions * `-retain_repo_versions` - Retain repo versions (descending) * `user_hidden` - User hidden * `-user_hidden` - User hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
prn__in = ['prn__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
remote = 'remote_example' # str | Foreign Key referenced by HREF (optional)
retain_repo_versions = 56 # int | Filter results where retain_repo_versions matches value (optional)
retain_repo_versions__gt = 56 # int | Filter results where retain_repo_versions is greater than value (optional)
retain_repo_versions__gte = 56 # int | Filter results where retain_repo_versions is greater than or equal to value (optional)
retain_repo_versions__isnull = True # bool | Filter results where retain_repo_versions has a null value (optional)
retain_repo_versions__lt = 56 # int | Filter results where retain_repo_versions is less than value (optional)
retain_repo_versions__lte = 56 # int | Filter results where retain_repo_versions is less than or equal to value (optional)
retain_repo_versions__ne = 56 # int | Filter results where retain_repo_versions not equal to value (optional)
retain_repo_versions__range = [56] # list[int] | Filter results where retain_repo_versions is between two comma separated values (optional)
with_content = 'with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List npm repositorys
        api_response = api_instance.list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->list: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
latest_with_content = 'latest_with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `description` - Description * `-description` - Description (descending) * `next_version` - Next version * `-next_version` - Next version (descending) * `retain_repo_versions` - Retain repo versions * `-retain_repo_versions` - Retain repo versions (descending) * `user_hidden` - User hidden * `-user_hidden` - User hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
prn__in = ['prn__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
remote = 'remote_example' # str | Foreign Key referenced by HREF (optional)
retain_repo_versions = 56 # int | Filter results where retain_repo_versions matches value (optional)
retain_repo_versions__gt = 56 # int | Filter results where retain_repo_versions is greater than value (optional)
retain_repo_versions__gte = 56 # int | Filter results where retain_repo_versions is greater than or equal to value (optional)
retain_repo_versions__isnull = True # bool | Filter results where retain_repo_versions has a null value (optional)
retain_repo_versions__lt = 56 # int | Filter results where retain_repo_versions is less than value (optional)
retain_repo_versions__lte = 56 # int | Filter results where retain_repo_versions is less than or equal to value (optional)
retain_repo_versions__ne = 56 # int | Filter results where retain_repo_versions not equal to value (optional)
retain_repo_versions__range = [56] # list[int] | Filter results where retain_repo_versions is between two comma separated values (optional)
with_content = 'with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List npm repositorys
        api_response = api_instance.list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->list: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    pulp_domain = 'pulp_domain_example' # str | 
latest_with_content = 'latest_with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
limit = 56 # int | Number of results to return per page. (optional)
name = 'name_example' # str | Filter results where name matches value (optional)
name__contains = 'name__contains_example' # str | Filter results where name contains value (optional)
name__icontains = 'name__icontains_example' # str | Filter results where name contains value (optional)
name__iexact = 'name__iexact_example' # str | Filter results where name matches value (optional)
name__in = ['name__in_example'] # list[str] | Filter results where name is in a comma-separated list of values (optional)
name__iregex = 'name__iregex_example' # str | Filter results where name matches regex value (optional)
name__istartswith = 'name__istartswith_example' # str | Filter results where name starts with value (optional)
name__regex = 'name__regex_example' # str | Filter results where name matches regex value (optional)
name__startswith = 'name__startswith_example' # str | Filter results where name starts with value (optional)
offset = 56 # int | The initial index from which to return the results. (optional)
ordering = ['ordering_example'] # list[str] | Ordering  * `pulp_id` - Pulp id * `-pulp_id` - Pulp id (descending) * `pulp_created` - Pulp created * `-pulp_created` - Pulp created (descending) * `pulp_last_updated` - Pulp last updated * `-pulp_last_updated` - Pulp last updated (descending) * `pulp_type` - Pulp type * `-pulp_type` - Pulp type (descending) * `name` - Name * `-name` - Name (descending) * `pulp_labels` - Pulp labels * `-pulp_labels` - Pulp labels (descending) * `description` - Description * `-description` - Description (descending) * `next_version` - Next version * `-next_version` - Next version (descending) * `retain_repo_versions` - Retain repo versions * `-retain_repo_versions` - Retain repo versions (descending) * `user_hidden` - User hidden * `-user_hidden` - User hidden (descending) * `pk` - Pk * `-pk` - Pk (descending) (optional)
prn__in = ['prn__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_href__in = ['pulp_href__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_id__in = ['pulp_id__in_example'] # list[str] | Multiple values may be separated by commas. (optional)
pulp_label_select = 'pulp_label_select_example' # str | Filter labels by search string (optional)
q = 'q_example' # str | Filter results by using NOT, AND and OR operations on other filters (optional)
remote = 'remote_example' # str | Foreign Key referenced by HREF (optional)
retain_repo_versions = 56 # int | Filter results where retain_repo_versions matches value (optional)
retain_repo_versions__gt = 56 # int | Filter results where retain_repo_versions is greater than value (optional)
retain_repo_versions__gte = 56 # int | Filter results where retain_repo_versions is greater than or equal to value (optional)
retain_repo_versions__isnull = True # bool | Filter results where retain_repo_versions has a null value (optional)
retain_repo_versions__lt = 56 # int | Filter results where retain_repo_versions is less than value (optional)
retain_repo_versions__lte = 56 # int | Filter results where retain_repo_versions is less than or equal to value (optional)
retain_repo_versions__ne = 56 # int | Filter results where retain_repo_versions not equal to value (optional)
retain_repo_versions__range = [56] # list[int] | Filter results where retain_repo_versions is between two comma separated values (optional)
with_content = 'with_content_example' # str | Content Unit referenced by HREF/PRN (optional)
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # List npm repositorys
        api_response = api_instance.list(pulp_domain, latest_with_content=latest_with_content, limit=limit, name=name, name__contains=name__contains, name__icontains=name__icontains, name__iexact=name__iexact, name__in=name__in, name__iregex=name__iregex, name__istartswith=name__istartswith, name__regex=name__regex, name__startswith=name__startswith, offset=offset, ordering=ordering, prn__in=prn__in, pulp_href__in=pulp_href__in, pulp_id__in=pulp_id__in, pulp_label_select=pulp_label_select, q=q, remote=remote, retain_repo_versions=retain_repo_versions, retain_repo_versions__gt=retain_repo_versions__gt, retain_repo_versions__gte=retain_repo_versions__gte, retain_repo_versions__isnull=retain_repo_versions__isnull, retain_repo_versions__lt=retain_repo_versions__lt, retain_repo_versions__lte=retain_repo_versions__lte, retain_repo_versions__ne=retain_repo_versions__ne, retain_repo_versions__range=retain_repo_versions__range, with_content=with_content, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pulp_domain** | **str**|  | 
 **latest_with_content** | **str**| Content Unit referenced by HREF/PRN | [optional] 
 **limit** | **int**| Number of results to return per page. | [optional] 
 **name** | **str**| Filter results where name matches value | [optional] 
 **name__contains** | **str**| Filter results where name contains value | [optional] 
 **name__icontains** | **str**| Filter results where name contains value | [optional] 
 **name__iexact** | **str**| Filter results where name matches value | [optional] 
 **name__in** | [**list[str]**](str.md)| Filter results where name is in a comma-separated list of values | [optional] 
 **name__iregex** | **str**| Filter results where name matches regex value | [optional] 
 **name__istartswith** | **str**| Filter results where name starts with value | [optional] 
 **name__regex** | **str**| Filter results where name matches regex value | [optional] 
 **name__startswith** | **str**| Filter results where name starts with value | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 
 **ordering** | [**list[str]**](str.md)| Ordering  * &#x60;pulp_id&#x60; - Pulp id * &#x60;-pulp_id&#x60; - Pulp id (descending) * &#x60;pulp_created&#x60; - Pulp created * &#x60;-pulp_created&#x60; - Pulp created (descending) * &#x60;pulp_last_updated&#x60; - Pulp last updated * &#x60;-pulp_last_updated&#x60; - Pulp last updated (descending) * &#x60;pulp_type&#x60; - Pulp type * &#x60;-pulp_type&#x60; - Pulp type (descending) * &#x60;name&#x60; - Name * &#x60;-name&#x60; - Name (descending) * &#x60;pulp_labels&#x60; - Pulp labels * &#x60;-pulp_labels&#x60; - Pulp labels (descending) * &#x60;description&#x60; - Description * &#x60;-description&#x60; - Description (descending) * &#x60;next_version&#x60; - Next version * &#x60;-next_version&#x60; - Next version (descending) * &#x60;retain_repo_versions&#x60; - Retain repo versions * &#x60;-retain_repo_versions&#x60; - Retain repo versions (descending) * &#x60;user_hidden&#x60; - User hidden * &#x60;-user_hidden&#x60; - User hidden (descending) * &#x60;pk&#x60; - Pk * &#x60;-pk&#x60; - Pk (descending) | [optional] 
 **prn__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_href__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_id__in** | [**list[str]**](str.md)| Multiple values may be separated by commas. | [optional] 
 **pulp_label_select** | **str**| Filter labels by search string | [optional] 
 **q** | **str**| Filter results by using NOT, AND and OR operations on other filters | [optional] 
 **remote** | [**str**](.md)| Foreign Key referenced by HREF | [optional] 
 **retain_repo_versions** | **int**| Filter results where retain_repo_versions matches value | [optional] 
 **retain_repo_versions__gt** | **int**| Filter results where retain_repo_versions is greater than value | [optional] 
 **retain_repo_versions__gte** | **int**| Filter results where retain_repo_versions is greater than or equal to value | [optional] 
 **retain_repo_versions__isnull** | **bool**| Filter results where retain_repo_versions has a null value | [optional] 
 **retain_repo_versions__lt** | **int**| Filter results where retain_repo_versions is less than value | [optional] 
 **retain_repo_versions__lte** | **int**| Filter results where retain_repo_versions is less than or equal to value | [optional] 
 **retain_repo_versions__ne** | **int**| Filter results where retain_repo_versions not equal to value | [optional] 
 **retain_repo_versions__range** | [**list[int]**](int.md)| Filter results where retain_repo_versions is between two comma separated values | [optional] 
 **with_content** | **str**| Content Unit referenced by HREF/PRN | [optional] 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**PaginatednpmNpmRepositoryResponseList**](PaginatednpmNpmRepositoryResponseList.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify**
> AsyncOperationResponse modify(npm_npm_repository_href, repository_add_remove_content)

Modify Repository Content

Trigger an asynchronous task to create a new repository version.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
repository_add_remove_content = pulpcore.client.pulp_npm.RepositoryAddRemoveContent() # RepositoryAddRemoveContent | 

    try:
        # Modify Repository Content
        api_response = api_instance.modify(npm_npm_repository_href, repository_add_remove_content)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->modify: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
repository_add_remove_content = pulpcore.client.pulp_npm.RepositoryAddRemoveContent() # RepositoryAddRemoveContent | 

    try:
        # Modify Repository Content
        api_response = api_instance.modify(npm_npm_repository_href, repository_add_remove_content)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->modify: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
repository_add_remove_content = pulpcore.client.pulp_npm.RepositoryAddRemoveContent() # RepositoryAddRemoveContent | 

    try:
        # Modify Repository Content
        api_response = api_instance.modify(npm_npm_repository_href, repository_add_remove_content)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->modify: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 
 **repository_add_remove_content** | [**RepositoryAddRemoveContent**](RepositoryAddRemoveContent.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_update**
> AsyncOperationResponse partial_update(npm_npm_repository_href, patchednpm_npm_repository)

Update a npm repository

Trigger an asynchronous partial update task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
patchednpm_npm_repository = pulpcore.client.pulp_npm.PatchednpmNpmRepository() # PatchednpmNpmRepository | 

    try:
        # Update a npm repository
        api_response = api_instance.partial_update(npm_npm_repository_href, patchednpm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->partial_update: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
patchednpm_npm_repository = pulpcore.client.pulp_npm.PatchednpmNpmRepository() # PatchednpmNpmRepository | 

    try:
        # Update a npm repository
        api_response = api_instance.partial_update(npm_npm_repository_href, patchednpm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->partial_update: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
patchednpm_npm_repository = pulpcore.client.pulp_npm.PatchednpmNpmRepository() # PatchednpmNpmRepository | 

    try:
        # Update a npm repository
        api_response = api_instance.partial_update(npm_npm_repository_href, patchednpm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 
 **patchednpm_npm_repository** | [**PatchednpmNpmRepository**](PatchednpmNpmRepository.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> NpmNpmRepositoryResponse read(npm_npm_repository_href, fields=fields, exclude_fields=exclude_fields)

Inspect a npm repository

A ViewSet for NpmRepository.  Similar to the PackageViewSet above, define endpoint_name, queryset and serializer, at a minimum.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a npm repository
        api_response = api_instance.read(npm_npm_repository_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->read: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a npm repository
        api_response = api_instance.read(npm_npm_repository_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->read: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
fields = ['fields_example'] # list[str] | A list of fields to include in the response. (optional)
exclude_fields = ['exclude_fields_example'] # list[str] | A list of fields to exclude from the response. (optional)

    try:
        # Inspect a npm repository
        api_response = api_instance.read(npm_npm_repository_href, fields=fields, exclude_fields=exclude_fields)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 
 **fields** | [**list[str]**](str.md)| A list of fields to include in the response. | [optional] 
 **exclude_fields** | [**list[str]**](str.md)| A list of fields to exclude from the response. | [optional] 

### Return type

[**NpmNpmRepositoryResponse**](NpmNpmRepositoryResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_label**
> SetLabelResponse set_label(npm_npm_repository_href, set_label)

Set a label

Set a single pulp_label on the object to a specific value or null.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
set_label = pulpcore.client.pulp_npm.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(npm_npm_repository_href, set_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->set_label: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
set_label = pulpcore.client.pulp_npm.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(npm_npm_repository_href, set_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->set_label: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
set_label = pulpcore.client.pulp_npm.SetLabel() # SetLabel | 

    try:
        # Set a label
        api_response = api_instance.set_label(npm_npm_repository_href, set_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->set_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 
 **set_label** | [**SetLabel**](SetLabel.md)|  | 

### Return type

[**SetLabelResponse**](SetLabelResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sync**
> AsyncOperationResponse sync(npm_npm_repository_href, repository_sync_url)

Sync from remote

Trigger an asynchronous task to sync content.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
repository_sync_url = pulpcore.client.pulp_npm.RepositorySyncURL() # RepositorySyncURL | 

    try:
        # Sync from remote
        api_response = api_instance.sync(npm_npm_repository_href, repository_sync_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->sync: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
repository_sync_url = pulpcore.client.pulp_npm.RepositorySyncURL() # RepositorySyncURL | 

    try:
        # Sync from remote
        api_response = api_instance.sync(npm_npm_repository_href, repository_sync_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->sync: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
repository_sync_url = pulpcore.client.pulp_npm.RepositorySyncURL() # RepositorySyncURL | 

    try:
        # Sync from remote
        api_response = api_instance.sync(npm_npm_repository_href, repository_sync_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->sync: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 
 **repository_sync_url** | [**RepositorySyncURL**](RepositorySyncURL.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_label**
> UnsetLabelResponse unset_label(npm_npm_repository_href, unset_label)

Unset a label

Unset a single pulp_label on the object.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
unset_label = pulpcore.client.pulp_npm.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(npm_npm_repository_href, unset_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->unset_label: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
unset_label = pulpcore.client.pulp_npm.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(npm_npm_repository_href, unset_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->unset_label: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
unset_label = pulpcore.client.pulp_npm.UnsetLabel() # UnsetLabel | 

    try:
        # Unset a label
        api_response = api_instance.unset_label(npm_npm_repository_href, unset_label)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->unset_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 
 **unset_label** | [**UnsetLabel**](UnsetLabel.md)|  | 

### Return type

[**UnsetLabelResponse**](UnsetLabelResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> AsyncOperationResponse update(npm_npm_repository_href, npm_npm_repository)

Update a npm repository

Trigger an asynchronous update task

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
npm_npm_repository = pulpcore.client.pulp_npm.NpmNpmRepository() # NpmNpmRepository | 

    try:
        # Update a npm repository
        api_response = api_instance.update(npm_npm_repository_href, npm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->update: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
npm_npm_repository = pulpcore.client.pulp_npm.NpmNpmRepository() # NpmNpmRepository | 

    try:
        # Update a npm repository
        api_response = api_instance.update(npm_npm_repository_href, npm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->update: %s\n" % e)
```

* OAuth Authentication (json_header_remote_authentication):
```python
from __future__ import print_function
import time
import pulpcore.client.pulp_npm
from pulpcore.client.pulp_npm.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://console.stage.redhat.com
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'

# Configure OAuth2 access token for authorization: json_header_remote_authentication
configuration = pulpcore.client.pulp_npm.Configuration(
    host = "https://console.stage.redhat.com"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pulpcore.client.pulp_npm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_npm.RepositoriesNpmApi(api_client)
    npm_npm_repository_href = 'npm_npm_repository_href_example' # str | 
npm_npm_repository = pulpcore.client.pulp_npm.NpmNpmRepository() # NpmNpmRepository | 

    try:
        # Update a npm repository
        api_response = api_instance.update(npm_npm_repository_href, npm_npm_repository)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RepositoriesNpmApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **npm_npm_repository_href** | **str**|  | 
 **npm_npm_repository** | [**NpmNpmRepository**](NpmNpmRepository.md)|  | 

### Return type

[**AsyncOperationResponse**](AsyncOperationResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth), [cookieAuth](../README.md#cookieAuth), [json_header_remote_authentication](../README.md#json_header_remote_authentication)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

