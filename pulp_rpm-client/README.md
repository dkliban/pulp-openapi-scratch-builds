# pulp_rpm-client
Fetch, Upload, Organize, and Distribute Software Packages

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v3
- Package version: 3.24.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://pulpproject.org](https://pulpproject.org)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import pulpcore.client.pulp_rpm
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pulpcore.client.pulp_rpm
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import pulpcore.client.pulp_rpm
from pulpcore.client.pulp_rpm.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8080
# See configuration.py for a list of all supported configuration parameters.
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8080"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Configure API key authorization: cookieAuth
configuration = pulpcore.client.pulp_rpm.Configuration(
    host = "http://localhost:8080",
    api_key = {
        'sessionid': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionid'] = 'Bearer'


# Enter a context with an instance of the API client
with pulpcore.client.pulp_rpm.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pulpcore.client.pulp_rpm.AcsRpmApi(api_client)
    rpm_rpm_alternate_content_source_href = 'rpm_rpm_alternate_content_source_href_example' # str | 
nested_role = pulpcore.client.pulp_rpm.NestedRole() # NestedRole | 

    try:
        # Add a role
        api_response = api_instance.add_role(rpm_rpm_alternate_content_source_href, nested_role)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AcsRpmApi->add_role: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:8080*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AcsRpmApi* | [**add_role**](docs/AcsRpmApi.md#add_role) | **POST** {rpm_rpm_alternate_content_source_href}add_role/ | Add a role
*AcsRpmApi* | [**create**](docs/AcsRpmApi.md#create) | **POST** /pulp/api/v3/acs/rpm/rpm/ | Create a rpm alternate content source
*AcsRpmApi* | [**delete**](docs/AcsRpmApi.md#delete) | **DELETE** {rpm_rpm_alternate_content_source_href} | Delete a rpm alternate content source
*AcsRpmApi* | [**list**](docs/AcsRpmApi.md#list) | **GET** /pulp/api/v3/acs/rpm/rpm/ | List rpm alternate content sources
*AcsRpmApi* | [**list_roles**](docs/AcsRpmApi.md#list_roles) | **GET** {rpm_rpm_alternate_content_source_href}list_roles/ | List roles
*AcsRpmApi* | [**my_permissions**](docs/AcsRpmApi.md#my_permissions) | **GET** {rpm_rpm_alternate_content_source_href}my_permissions/ | List user permissions
*AcsRpmApi* | [**partial_update**](docs/AcsRpmApi.md#partial_update) | **PATCH** {rpm_rpm_alternate_content_source_href} | Update a rpm alternate content source
*AcsRpmApi* | [**read**](docs/AcsRpmApi.md#read) | **GET** {rpm_rpm_alternate_content_source_href} | Inspect a rpm alternate content source
*AcsRpmApi* | [**refresh**](docs/AcsRpmApi.md#refresh) | **POST** {rpm_rpm_alternate_content_source_href}refresh/ | 
*AcsRpmApi* | [**remove_role**](docs/AcsRpmApi.md#remove_role) | **POST** {rpm_rpm_alternate_content_source_href}remove_role/ | Remove a role
*AcsRpmApi* | [**update**](docs/AcsRpmApi.md#update) | **PUT** {rpm_rpm_alternate_content_source_href} | Update a rpm alternate content source
*ContentAdvisoriesApi* | [**create**](docs/ContentAdvisoriesApi.md#create) | **POST** /pulp/api/v3/content/rpm/advisories/ | Create an update record
*ContentAdvisoriesApi* | [**list**](docs/ContentAdvisoriesApi.md#list) | **GET** /pulp/api/v3/content/rpm/advisories/ | List update records
*ContentAdvisoriesApi* | [**read**](docs/ContentAdvisoriesApi.md#read) | **GET** {rpm_update_record_href} | Inspect an update record
*ContentDistributionTreesApi* | [**list**](docs/ContentDistributionTreesApi.md#list) | **GET** /pulp/api/v3/content/rpm/distribution_trees/ | List distribution trees
*ContentDistributionTreesApi* | [**read**](docs/ContentDistributionTreesApi.md#read) | **GET** {rpm_distribution_tree_href} | Inspect a distribution tree
*ContentModulemdDefaultsApi* | [**create**](docs/ContentModulemdDefaultsApi.md#create) | **POST** /pulp/api/v3/content/rpm/modulemd_defaults/ | Create a modulemd defaults
*ContentModulemdDefaultsApi* | [**list**](docs/ContentModulemdDefaultsApi.md#list) | **GET** /pulp/api/v3/content/rpm/modulemd_defaults/ | List modulemd defaultss
*ContentModulemdDefaultsApi* | [**read**](docs/ContentModulemdDefaultsApi.md#read) | **GET** {rpm_modulemd_defaults_href} | Inspect a modulemd defaults
*ContentModulemdObsoletesApi* | [**create**](docs/ContentModulemdObsoletesApi.md#create) | **POST** /pulp/api/v3/content/rpm/modulemd_obsoletes/ | Create a modulemd obsolete
*ContentModulemdObsoletesApi* | [**list**](docs/ContentModulemdObsoletesApi.md#list) | **GET** /pulp/api/v3/content/rpm/modulemd_obsoletes/ | List modulemd obsoletes
*ContentModulemdObsoletesApi* | [**read**](docs/ContentModulemdObsoletesApi.md#read) | **GET** {rpm_modulemd_obsolete_href} | Inspect a modulemd obsolete
*ContentModulemdsApi* | [**create**](docs/ContentModulemdsApi.md#create) | **POST** /pulp/api/v3/content/rpm/modulemds/ | Create a modulemd
*ContentModulemdsApi* | [**list**](docs/ContentModulemdsApi.md#list) | **GET** /pulp/api/v3/content/rpm/modulemds/ | List modulemds
*ContentModulemdsApi* | [**read**](docs/ContentModulemdsApi.md#read) | **GET** {rpm_modulemd_href} | Inspect a modulemd
*ContentPackagecategoriesApi* | [**list**](docs/ContentPackagecategoriesApi.md#list) | **GET** /pulp/api/v3/content/rpm/packagecategories/ | List package categorys
*ContentPackagecategoriesApi* | [**read**](docs/ContentPackagecategoriesApi.md#read) | **GET** {rpm_package_category_href} | Inspect a package category
*ContentPackageenvironmentsApi* | [**list**](docs/ContentPackageenvironmentsApi.md#list) | **GET** /pulp/api/v3/content/rpm/packageenvironments/ | List package environments
*ContentPackageenvironmentsApi* | [**read**](docs/ContentPackageenvironmentsApi.md#read) | **GET** {rpm_package_environment_href} | Inspect a package environment
*ContentPackagegroupsApi* | [**list**](docs/ContentPackagegroupsApi.md#list) | **GET** /pulp/api/v3/content/rpm/packagegroups/ | List package groups
*ContentPackagegroupsApi* | [**read**](docs/ContentPackagegroupsApi.md#read) | **GET** {rpm_package_group_href} | Inspect a package group
*ContentPackagelangpacksApi* | [**list**](docs/ContentPackagelangpacksApi.md#list) | **GET** /pulp/api/v3/content/rpm/packagelangpacks/ | List package langpackss
*ContentPackagelangpacksApi* | [**read**](docs/ContentPackagelangpacksApi.md#read) | **GET** {rpm_package_langpacks_href} | Inspect a package langpacks
*ContentPackagesApi* | [**create**](docs/ContentPackagesApi.md#create) | **POST** /pulp/api/v3/content/rpm/packages/ | Create a package
*ContentPackagesApi* | [**list**](docs/ContentPackagesApi.md#list) | **GET** /pulp/api/v3/content/rpm/packages/ | List packages
*ContentPackagesApi* | [**read**](docs/ContentPackagesApi.md#read) | **GET** {rpm_package_href} | Inspect a package
*ContentRepoMetadataFilesApi* | [**list**](docs/ContentRepoMetadataFilesApi.md#list) | **GET** /pulp/api/v3/content/rpm/repo_metadata_files/ | List repo metadata files
*ContentRepoMetadataFilesApi* | [**read**](docs/ContentRepoMetadataFilesApi.md#read) | **GET** {rpm_repo_metadata_file_href} | Inspect a repo metadata file
*DistributionsRpmApi* | [**add_role**](docs/DistributionsRpmApi.md#add_role) | **POST** {rpm_rpm_distribution_href}add_role/ | Add a role
*DistributionsRpmApi* | [**create**](docs/DistributionsRpmApi.md#create) | **POST** /pulp/api/v3/distributions/rpm/rpm/ | Create a rpm distribution
*DistributionsRpmApi* | [**delete**](docs/DistributionsRpmApi.md#delete) | **DELETE** {rpm_rpm_distribution_href} | Delete a rpm distribution
*DistributionsRpmApi* | [**list**](docs/DistributionsRpmApi.md#list) | **GET** /pulp/api/v3/distributions/rpm/rpm/ | List rpm distributions
*DistributionsRpmApi* | [**list_roles**](docs/DistributionsRpmApi.md#list_roles) | **GET** {rpm_rpm_distribution_href}list_roles/ | List roles
*DistributionsRpmApi* | [**my_permissions**](docs/DistributionsRpmApi.md#my_permissions) | **GET** {rpm_rpm_distribution_href}my_permissions/ | List user permissions
*DistributionsRpmApi* | [**partial_update**](docs/DistributionsRpmApi.md#partial_update) | **PATCH** {rpm_rpm_distribution_href} | Update a rpm distribution
*DistributionsRpmApi* | [**read**](docs/DistributionsRpmApi.md#read) | **GET** {rpm_rpm_distribution_href} | Inspect a rpm distribution
*DistributionsRpmApi* | [**remove_role**](docs/DistributionsRpmApi.md#remove_role) | **POST** {rpm_rpm_distribution_href}remove_role/ | Remove a role
*DistributionsRpmApi* | [**set_label**](docs/DistributionsRpmApi.md#set_label) | **POST** {rpm_rpm_distribution_href}set_label/ | Set a label
*DistributionsRpmApi* | [**unset_label**](docs/DistributionsRpmApi.md#unset_label) | **POST** {rpm_rpm_distribution_href}unset_label/ | Unset a label
*DistributionsRpmApi* | [**update**](docs/DistributionsRpmApi.md#update) | **PUT** {rpm_rpm_distribution_href} | Update a rpm distribution
*PublicationsRpmApi* | [**add_role**](docs/PublicationsRpmApi.md#add_role) | **POST** {rpm_rpm_publication_href}add_role/ | Add a role
*PublicationsRpmApi* | [**create**](docs/PublicationsRpmApi.md#create) | **POST** /pulp/api/v3/publications/rpm/rpm/ | Create a rpm publication
*PublicationsRpmApi* | [**delete**](docs/PublicationsRpmApi.md#delete) | **DELETE** {rpm_rpm_publication_href} | Delete a rpm publication
*PublicationsRpmApi* | [**list**](docs/PublicationsRpmApi.md#list) | **GET** /pulp/api/v3/publications/rpm/rpm/ | List rpm publications
*PublicationsRpmApi* | [**list_roles**](docs/PublicationsRpmApi.md#list_roles) | **GET** {rpm_rpm_publication_href}list_roles/ | List roles
*PublicationsRpmApi* | [**my_permissions**](docs/PublicationsRpmApi.md#my_permissions) | **GET** {rpm_rpm_publication_href}my_permissions/ | List user permissions
*PublicationsRpmApi* | [**read**](docs/PublicationsRpmApi.md#read) | **GET** {rpm_rpm_publication_href} | Inspect a rpm publication
*PublicationsRpmApi* | [**remove_role**](docs/PublicationsRpmApi.md#remove_role) | **POST** {rpm_rpm_publication_href}remove_role/ | Remove a role
*RemotesRpmApi* | [**add_role**](docs/RemotesRpmApi.md#add_role) | **POST** {rpm_rpm_remote_href}add_role/ | Add a role
*RemotesRpmApi* | [**create**](docs/RemotesRpmApi.md#create) | **POST** /pulp/api/v3/remotes/rpm/rpm/ | Create a rpm remote
*RemotesRpmApi* | [**delete**](docs/RemotesRpmApi.md#delete) | **DELETE** {rpm_rpm_remote_href} | Delete a rpm remote
*RemotesRpmApi* | [**list**](docs/RemotesRpmApi.md#list) | **GET** /pulp/api/v3/remotes/rpm/rpm/ | List rpm remotes
*RemotesRpmApi* | [**list_roles**](docs/RemotesRpmApi.md#list_roles) | **GET** {rpm_rpm_remote_href}list_roles/ | List roles
*RemotesRpmApi* | [**my_permissions**](docs/RemotesRpmApi.md#my_permissions) | **GET** {rpm_rpm_remote_href}my_permissions/ | List user permissions
*RemotesRpmApi* | [**partial_update**](docs/RemotesRpmApi.md#partial_update) | **PATCH** {rpm_rpm_remote_href} | Update a rpm remote
*RemotesRpmApi* | [**read**](docs/RemotesRpmApi.md#read) | **GET** {rpm_rpm_remote_href} | Inspect a rpm remote
*RemotesRpmApi* | [**remove_role**](docs/RemotesRpmApi.md#remove_role) | **POST** {rpm_rpm_remote_href}remove_role/ | Remove a role
*RemotesRpmApi* | [**set_label**](docs/RemotesRpmApi.md#set_label) | **POST** {rpm_rpm_remote_href}set_label/ | Set a label
*RemotesRpmApi* | [**unset_label**](docs/RemotesRpmApi.md#unset_label) | **POST** {rpm_rpm_remote_href}unset_label/ | Unset a label
*RemotesRpmApi* | [**update**](docs/RemotesRpmApi.md#update) | **PUT** {rpm_rpm_remote_href} | Update a rpm remote
*RemotesUlnApi* | [**add_role**](docs/RemotesUlnApi.md#add_role) | **POST** {rpm_uln_remote_href}add_role/ | Add a role
*RemotesUlnApi* | [**create**](docs/RemotesUlnApi.md#create) | **POST** /pulp/api/v3/remotes/rpm/uln/ | Create an uln remote
*RemotesUlnApi* | [**delete**](docs/RemotesUlnApi.md#delete) | **DELETE** {rpm_uln_remote_href} | Delete an uln remote
*RemotesUlnApi* | [**list**](docs/RemotesUlnApi.md#list) | **GET** /pulp/api/v3/remotes/rpm/uln/ | List uln remotes
*RemotesUlnApi* | [**list_roles**](docs/RemotesUlnApi.md#list_roles) | **GET** {rpm_uln_remote_href}list_roles/ | List roles
*RemotesUlnApi* | [**my_permissions**](docs/RemotesUlnApi.md#my_permissions) | **GET** {rpm_uln_remote_href}my_permissions/ | List user permissions
*RemotesUlnApi* | [**partial_update**](docs/RemotesUlnApi.md#partial_update) | **PATCH** {rpm_uln_remote_href} | Update an uln remote
*RemotesUlnApi* | [**read**](docs/RemotesUlnApi.md#read) | **GET** {rpm_uln_remote_href} | Inspect an uln remote
*RemotesUlnApi* | [**remove_role**](docs/RemotesUlnApi.md#remove_role) | **POST** {rpm_uln_remote_href}remove_role/ | Remove a role
*RemotesUlnApi* | [**set_label**](docs/RemotesUlnApi.md#set_label) | **POST** {rpm_uln_remote_href}set_label/ | Set a label
*RemotesUlnApi* | [**unset_label**](docs/RemotesUlnApi.md#unset_label) | **POST** {rpm_uln_remote_href}unset_label/ | Unset a label
*RemotesUlnApi* | [**update**](docs/RemotesUlnApi.md#update) | **PUT** {rpm_uln_remote_href} | Update an uln remote
*RepositoriesRpmApi* | [**add_role**](docs/RepositoriesRpmApi.md#add_role) | **POST** {rpm_rpm_repository_href}add_role/ | Add a role
*RepositoriesRpmApi* | [**create**](docs/RepositoriesRpmApi.md#create) | **POST** /pulp/api/v3/repositories/rpm/rpm/ | Create a rpm repository
*RepositoriesRpmApi* | [**delete**](docs/RepositoriesRpmApi.md#delete) | **DELETE** {rpm_rpm_repository_href} | Delete a rpm repository
*RepositoriesRpmApi* | [**list**](docs/RepositoriesRpmApi.md#list) | **GET** /pulp/api/v3/repositories/rpm/rpm/ | List rpm repositorys
*RepositoriesRpmApi* | [**list_roles**](docs/RepositoriesRpmApi.md#list_roles) | **GET** {rpm_rpm_repository_href}list_roles/ | List roles
*RepositoriesRpmApi* | [**modify**](docs/RepositoriesRpmApi.md#modify) | **POST** {rpm_rpm_repository_href}modify/ | Modify Repository Content
*RepositoriesRpmApi* | [**my_permissions**](docs/RepositoriesRpmApi.md#my_permissions) | **GET** {rpm_rpm_repository_href}my_permissions/ | List user permissions
*RepositoriesRpmApi* | [**partial_update**](docs/RepositoriesRpmApi.md#partial_update) | **PATCH** {rpm_rpm_repository_href} | Update a rpm repository
*RepositoriesRpmApi* | [**read**](docs/RepositoriesRpmApi.md#read) | **GET** {rpm_rpm_repository_href} | Inspect a rpm repository
*RepositoriesRpmApi* | [**remove_role**](docs/RepositoriesRpmApi.md#remove_role) | **POST** {rpm_rpm_repository_href}remove_role/ | Remove a role
*RepositoriesRpmApi* | [**set_label**](docs/RepositoriesRpmApi.md#set_label) | **POST** {rpm_rpm_repository_href}set_label/ | Set a label
*RepositoriesRpmApi* | [**sync**](docs/RepositoriesRpmApi.md#sync) | **POST** {rpm_rpm_repository_href}sync/ | Sync from remote
*RepositoriesRpmApi* | [**unset_label**](docs/RepositoriesRpmApi.md#unset_label) | **POST** {rpm_rpm_repository_href}unset_label/ | Unset a label
*RepositoriesRpmApi* | [**update**](docs/RepositoriesRpmApi.md#update) | **PUT** {rpm_rpm_repository_href} | Update a rpm repository
*RepositoriesRpmVersionsApi* | [**delete**](docs/RepositoriesRpmVersionsApi.md#delete) | **DELETE** {rpm_rpm_repository_version_href} | Delete a repository version
*RepositoriesRpmVersionsApi* | [**list**](docs/RepositoriesRpmVersionsApi.md#list) | **GET** {rpm_rpm_repository_href}versions/ | List repository versions
*RepositoriesRpmVersionsApi* | [**read**](docs/RepositoriesRpmVersionsApi.md#read) | **GET** {rpm_rpm_repository_version_href} | Inspect a repository version
*RepositoriesRpmVersionsApi* | [**repair**](docs/RepositoriesRpmVersionsApi.md#repair) | **POST** {rpm_rpm_repository_version_href}repair/ | 
*RpmCompsApi* | [**rpm_comps_upload**](docs/RpmCompsApi.md#rpm_comps_upload) | **POST** /pulp/api/v3/rpm/comps/ | Upload comps.xml
*RpmCopyApi* | [**copy_content**](docs/RpmCopyApi.md#copy_content) | **POST** /pulp/api/v3/rpm/copy/ | Copy content


## Documentation For Models

 - [AddonResponse](docs/AddonResponse.md)
 - [ArtifactResponse](docs/ArtifactResponse.md)
 - [AsyncOperationResponse](docs/AsyncOperationResponse.md)
 - [ChecksumResponse](docs/ChecksumResponse.md)
 - [CompsXml](docs/CompsXml.md)
 - [ContentSummaryResponse](docs/ContentSummaryResponse.md)
 - [Copy](docs/Copy.md)
 - [ImageResponse](docs/ImageResponse.md)
 - [MetadataChecksumTypeEnum](docs/MetadataChecksumTypeEnum.md)
 - [MyPermissionsResponse](docs/MyPermissionsResponse.md)
 - [NestedRole](docs/NestedRole.md)
 - [NestedRoleResponse](docs/NestedRoleResponse.md)
 - [ObjectRolesResponse](docs/ObjectRolesResponse.md)
 - [PackageChecksumTypeEnum](docs/PackageChecksumTypeEnum.md)
 - [PaginatedRepositoryVersionResponseList](docs/PaginatedRepositoryVersionResponseList.md)
 - [PaginatedrpmDistributionTreeResponseList](docs/PaginatedrpmDistributionTreeResponseList.md)
 - [PaginatedrpmModulemdDefaultsResponseList](docs/PaginatedrpmModulemdDefaultsResponseList.md)
 - [PaginatedrpmModulemdObsoleteResponseList](docs/PaginatedrpmModulemdObsoleteResponseList.md)
 - [PaginatedrpmModulemdResponseList](docs/PaginatedrpmModulemdResponseList.md)
 - [PaginatedrpmPackageCategoryResponseList](docs/PaginatedrpmPackageCategoryResponseList.md)
 - [PaginatedrpmPackageEnvironmentResponseList](docs/PaginatedrpmPackageEnvironmentResponseList.md)
 - [PaginatedrpmPackageGroupResponseList](docs/PaginatedrpmPackageGroupResponseList.md)
 - [PaginatedrpmPackageLangpacksResponseList](docs/PaginatedrpmPackageLangpacksResponseList.md)
 - [PaginatedrpmPackageResponseList](docs/PaginatedrpmPackageResponseList.md)
 - [PaginatedrpmRepoMetadataFileResponseList](docs/PaginatedrpmRepoMetadataFileResponseList.md)
 - [PaginatedrpmRpmAlternateContentSourceResponseList](docs/PaginatedrpmRpmAlternateContentSourceResponseList.md)
 - [PaginatedrpmRpmDistributionResponseList](docs/PaginatedrpmRpmDistributionResponseList.md)
 - [PaginatedrpmRpmPublicationResponseList](docs/PaginatedrpmRpmPublicationResponseList.md)
 - [PaginatedrpmRpmRemoteResponseList](docs/PaginatedrpmRpmRemoteResponseList.md)
 - [PaginatedrpmRpmRepositoryResponseList](docs/PaginatedrpmRpmRepositoryResponseList.md)
 - [PaginatedrpmUlnRemoteResponseList](docs/PaginatedrpmUlnRemoteResponseList.md)
 - [PaginatedrpmUpdateRecordResponseList](docs/PaginatedrpmUpdateRecordResponseList.md)
 - [PatchedrpmRpmAlternateContentSource](docs/PatchedrpmRpmAlternateContentSource.md)
 - [PatchedrpmRpmDistribution](docs/PatchedrpmRpmDistribution.md)
 - [PatchedrpmRpmRemote](docs/PatchedrpmRpmRemote.md)
 - [PatchedrpmRpmRepository](docs/PatchedrpmRpmRepository.md)
 - [PatchedrpmUlnRemote](docs/PatchedrpmUlnRemote.md)
 - [PolicyEnum](docs/PolicyEnum.md)
 - [Repair](docs/Repair.md)
 - [RepositoryAddRemoveContent](docs/RepositoryAddRemoveContent.md)
 - [RepositoryVersionResponse](docs/RepositoryVersionResponse.md)
 - [RpmDistributionTreeResponse](docs/RpmDistributionTreeResponse.md)
 - [RpmModulemd](docs/RpmModulemd.md)
 - [RpmModulemdDefaults](docs/RpmModulemdDefaults.md)
 - [RpmModulemdDefaultsResponse](docs/RpmModulemdDefaultsResponse.md)
 - [RpmModulemdObsolete](docs/RpmModulemdObsolete.md)
 - [RpmModulemdObsoleteResponse](docs/RpmModulemdObsoleteResponse.md)
 - [RpmModulemdResponse](docs/RpmModulemdResponse.md)
 - [RpmPackage](docs/RpmPackage.md)
 - [RpmPackageCategoryResponse](docs/RpmPackageCategoryResponse.md)
 - [RpmPackageEnvironmentResponse](docs/RpmPackageEnvironmentResponse.md)
 - [RpmPackageGroupResponse](docs/RpmPackageGroupResponse.md)
 - [RpmPackageLangpacksResponse](docs/RpmPackageLangpacksResponse.md)
 - [RpmPackageResponse](docs/RpmPackageResponse.md)
 - [RpmRepoMetadataFileResponse](docs/RpmRepoMetadataFileResponse.md)
 - [RpmRepositorySyncURL](docs/RpmRepositorySyncURL.md)
 - [RpmRpmAlternateContentSource](docs/RpmRpmAlternateContentSource.md)
 - [RpmRpmAlternateContentSourceResponse](docs/RpmRpmAlternateContentSourceResponse.md)
 - [RpmRpmDistribution](docs/RpmRpmDistribution.md)
 - [RpmRpmDistributionResponse](docs/RpmRpmDistributionResponse.md)
 - [RpmRpmPublication](docs/RpmRpmPublication.md)
 - [RpmRpmPublicationResponse](docs/RpmRpmPublicationResponse.md)
 - [RpmRpmRemote](docs/RpmRpmRemote.md)
 - [RpmRpmRemoteResponse](docs/RpmRpmRemoteResponse.md)
 - [RpmRpmRemoteResponseHiddenFields](docs/RpmRpmRemoteResponseHiddenFields.md)
 - [RpmRpmRepository](docs/RpmRpmRepository.md)
 - [RpmRpmRepositoryResponse](docs/RpmRpmRepositoryResponse.md)
 - [RpmUlnRemote](docs/RpmUlnRemote.md)
 - [RpmUlnRemoteResponse](docs/RpmUlnRemoteResponse.md)
 - [RpmUpdateCollection](docs/RpmUpdateCollection.md)
 - [RpmUpdateCollectionResponse](docs/RpmUpdateCollectionResponse.md)
 - [RpmUpdateRecord](docs/RpmUpdateRecord.md)
 - [RpmUpdateRecordResponse](docs/RpmUpdateRecordResponse.md)
 - [SetLabel](docs/SetLabel.md)
 - [SetLabelResponse](docs/SetLabelResponse.md)
 - [SkipTypesEnum](docs/SkipTypesEnum.md)
 - [SyncPolicyEnum](docs/SyncPolicyEnum.md)
 - [TaskGroupOperationResponse](docs/TaskGroupOperationResponse.md)
 - [UnsetLabel](docs/UnsetLabel.md)
 - [UnsetLabelResponse](docs/UnsetLabelResponse.md)
 - [VariantResponse](docs/VariantResponse.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## cookieAuth

- **Type**: API key
- **API key parameter name**: sessionid
- **Location**: 


## Author

pulp-list@redhat.com

