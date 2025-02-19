# coding: utf-8

"""
    Pulp 3 API

    Fetch, Upload, Organize, and Distribute Software Packages  # noqa: E501

    The version of the OpenAPI document: v3
    Contact: pulp-list@redhat.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from pulpcore.client.pulp_npm.configuration import Configuration


class NpmNpmRepositoryResponse(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'pulp_href': 'str',
        'prn': 'str',
        'pulp_created': 'datetime',
        'pulp_last_updated': 'datetime',
        'versions_href': 'str',
        'pulp_labels': 'dict(str, str)',
        'latest_version_href': 'str',
        'name': 'str',
        'description': 'str',
        'retain_repo_versions': 'int',
        'remote': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'prn': 'prn',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'versions_href': 'versions_href',
        'pulp_labels': 'pulp_labels',
        'latest_version_href': 'latest_version_href',
        'name': 'name',
        'description': 'description',
        'retain_repo_versions': 'retain_repo_versions',
        'remote': 'remote'
    }

    def __init__(self, pulp_href=None, prn=None, pulp_created=None, pulp_last_updated=None, versions_href=None, pulp_labels=None, latest_version_href=None, name=None, description=None, retain_repo_versions=None, remote=None, local_vars_configuration=None):  # noqa: E501
        """NpmNpmRepositoryResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._prn = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._versions_href = None
        self._pulp_labels = None
        self._latest_version_href = None
        self._name = None
        self._description = None
        self._retain_repo_versions = None
        self._remote = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if prn is not None:
            self.prn = prn
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        if versions_href is not None:
            self.versions_href = versions_href
        if pulp_labels is not None:
            self.pulp_labels = pulp_labels
        if latest_version_href is not None:
            self.latest_version_href = latest_version_href
        self.name = name
        self.description = description
        self.retain_repo_versions = retain_repo_versions
        self.remote = remote

    @property
    def pulp_href(self):
        """Gets the pulp_href of this NpmNpmRepositoryResponse.  # noqa: E501


        :return: The pulp_href of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this NpmNpmRepositoryResponse.


        :param pulp_href: The pulp_href of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def prn(self):
        """Gets the prn of this NpmNpmRepositoryResponse.  # noqa: E501

        The Pulp Resource Name (PRN).  # noqa: E501

        :return: The prn of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._prn

    @prn.setter
    def prn(self, prn):
        """Sets the prn of this NpmNpmRepositoryResponse.

        The Pulp Resource Name (PRN).  # noqa: E501

        :param prn: The prn of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._prn = prn

    @property
    def pulp_created(self):
        """Gets the pulp_created of this NpmNpmRepositoryResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this NpmNpmRepositoryResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this NpmNpmRepositoryResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this NpmNpmRepositoryResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def versions_href(self):
        """Gets the versions_href of this NpmNpmRepositoryResponse.  # noqa: E501


        :return: The versions_href of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._versions_href

    @versions_href.setter
    def versions_href(self, versions_href):
        """Sets the versions_href of this NpmNpmRepositoryResponse.


        :param versions_href: The versions_href of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._versions_href = versions_href

    @property
    def pulp_labels(self):
        """Gets the pulp_labels of this NpmNpmRepositoryResponse.  # noqa: E501


        :return: The pulp_labels of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._pulp_labels

    @pulp_labels.setter
    def pulp_labels(self, pulp_labels):
        """Sets the pulp_labels of this NpmNpmRepositoryResponse.


        :param pulp_labels: The pulp_labels of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._pulp_labels = pulp_labels

    @property
    def latest_version_href(self):
        """Gets the latest_version_href of this NpmNpmRepositoryResponse.  # noqa: E501


        :return: The latest_version_href of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._latest_version_href

    @latest_version_href.setter
    def latest_version_href(self, latest_version_href):
        """Sets the latest_version_href of this NpmNpmRepositoryResponse.


        :param latest_version_href: The latest_version_href of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._latest_version_href = latest_version_href

    @property
    def name(self):
        """Gets the name of this NpmNpmRepositoryResponse.  # noqa: E501

        A unique name for this repository.  # noqa: E501

        :return: The name of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NpmNpmRepositoryResponse.

        A unique name for this repository.  # noqa: E501

        :param name: The name of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this NpmNpmRepositoryResponse.  # noqa: E501

        An optional description.  # noqa: E501

        :return: The description of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NpmNpmRepositoryResponse.

        An optional description.  # noqa: E501

        :param description: The description of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def retain_repo_versions(self):
        """Gets the retain_repo_versions of this NpmNpmRepositoryResponse.  # noqa: E501

        Retain X versions of the repository. Default is null which retains all versions.  # noqa: E501

        :return: The retain_repo_versions of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: int
        """
        return self._retain_repo_versions

    @retain_repo_versions.setter
    def retain_repo_versions(self, retain_repo_versions):
        """Sets the retain_repo_versions of this NpmNpmRepositoryResponse.

        Retain X versions of the repository. Default is null which retains all versions.  # noqa: E501

        :param retain_repo_versions: The retain_repo_versions of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                retain_repo_versions is not None and retain_repo_versions < 1):  # noqa: E501
            raise ValueError("Invalid value for `retain_repo_versions`, must be a value greater than or equal to `1`")  # noqa: E501

        self._retain_repo_versions = retain_repo_versions

    @property
    def remote(self):
        """Gets the remote of this NpmNpmRepositoryResponse.  # noqa: E501

        An optional remote to use by default when syncing.  # noqa: E501

        :return: The remote of this NpmNpmRepositoryResponse.  # noqa: E501
        :rtype: str
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        """Sets the remote of this NpmNpmRepositoryResponse.

        An optional remote to use by default when syncing.  # noqa: E501

        :param remote: The remote of this NpmNpmRepositoryResponse.  # noqa: E501
        :type: str
        """

        self._remote = remote

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NpmNpmRepositoryResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NpmNpmRepositoryResponse):
            return True

        return self.to_dict() != other.to_dict()
