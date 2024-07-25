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

from pulpcore.client.pulpcore.configuration import Configuration


class DistributionResponse(object):
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
        'pulp_created': 'datetime',
        'pulp_last_updated': 'datetime',
        'base_path': 'str',
        'base_url': 'str',
        'content_guard': 'str',
        'hidden': 'bool',
        'pulp_labels': 'dict(str, str)',
        'name': 'str',
        'repository': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'base_path': 'base_path',
        'base_url': 'base_url',
        'content_guard': 'content_guard',
        'hidden': 'hidden',
        'pulp_labels': 'pulp_labels',
        'name': 'name',
        'repository': 'repository'
    }

    def __init__(self, pulp_href=None, pulp_created=None, pulp_last_updated=None, base_path=None, base_url=None, content_guard=None, hidden=False, pulp_labels=None, name=None, repository=None, local_vars_configuration=None):  # noqa: E501
        """DistributionResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._base_path = None
        self._base_url = None
        self._content_guard = None
        self._hidden = None
        self._pulp_labels = None
        self._name = None
        self._repository = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        self.base_path = base_path
        if base_url is not None:
            self.base_url = base_url
        self.content_guard = content_guard
        if hidden is not None:
            self.hidden = hidden
        if pulp_labels is not None:
            self.pulp_labels = pulp_labels
        self.name = name
        self.repository = repository

    @property
    def pulp_href(self):
        """Gets the pulp_href of this DistributionResponse.  # noqa: E501


        :return: The pulp_href of this DistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this DistributionResponse.


        :param pulp_href: The pulp_href of this DistributionResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this DistributionResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this DistributionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this DistributionResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this DistributionResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this DistributionResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this DistributionResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this DistributionResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this DistributionResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def base_path(self):
        """Gets the base_path of this DistributionResponse.  # noqa: E501

        The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \"foo\" and \"foo/bar\")  # noqa: E501

        :return: The base_path of this DistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this DistributionResponse.

        The base (relative) path component of the published url. Avoid paths that                     overlap with other distribution base paths (e.g. \"foo\" and \"foo/bar\")  # noqa: E501

        :param base_path: The base_path of this DistributionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and base_path is None:  # noqa: E501
            raise ValueError("Invalid value for `base_path`, must not be `None`")  # noqa: E501

        self._base_path = base_path

    @property
    def base_url(self):
        """Gets the base_url of this DistributionResponse.  # noqa: E501

        The URL for accessing the publication as defined by this distribution.  # noqa: E501

        :return: The base_url of this DistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url):
        """Sets the base_url of this DistributionResponse.

        The URL for accessing the publication as defined by this distribution.  # noqa: E501

        :param base_url: The base_url of this DistributionResponse.  # noqa: E501
        :type: str
        """

        self._base_url = base_url

    @property
    def content_guard(self):
        """Gets the content_guard of this DistributionResponse.  # noqa: E501

        An optional content-guard.  # noqa: E501

        :return: The content_guard of this DistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._content_guard

    @content_guard.setter
    def content_guard(self, content_guard):
        """Sets the content_guard of this DistributionResponse.

        An optional content-guard.  # noqa: E501

        :param content_guard: The content_guard of this DistributionResponse.  # noqa: E501
        :type: str
        """

        self._content_guard = content_guard

    @property
    def hidden(self):
        """Gets the hidden of this DistributionResponse.  # noqa: E501

        Whether this distribution should be shown in the content app.  # noqa: E501

        :return: The hidden of this DistributionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this DistributionResponse.

        Whether this distribution should be shown in the content app.  # noqa: E501

        :param hidden: The hidden of this DistributionResponse.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def pulp_labels(self):
        """Gets the pulp_labels of this DistributionResponse.  # noqa: E501


        :return: The pulp_labels of this DistributionResponse.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._pulp_labels

    @pulp_labels.setter
    def pulp_labels(self, pulp_labels):
        """Sets the pulp_labels of this DistributionResponse.


        :param pulp_labels: The pulp_labels of this DistributionResponse.  # noqa: E501
        :type: dict(str, str)
        """

        self._pulp_labels = pulp_labels

    @property
    def name(self):
        """Gets the name of this DistributionResponse.  # noqa: E501

        A unique name. Ex, `rawhide` and `stable`.  # noqa: E501

        :return: The name of this DistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DistributionResponse.

        A unique name. Ex, `rawhide` and `stable`.  # noqa: E501

        :param name: The name of this DistributionResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def repository(self):
        """Gets the repository of this DistributionResponse.  # noqa: E501

        The latest RepositoryVersion for this Repository will be served.  # noqa: E501

        :return: The repository of this DistributionResponse.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this DistributionResponse.

        The latest RepositoryVersion for this Repository will be served.  # noqa: E501

        :param repository: The repository of this DistributionResponse.  # noqa: E501
        :type: str
        """

        self._repository = repository

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
        if not isinstance(other, DistributionResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DistributionResponse):
            return True

        return self.to_dict() != other.to_dict()
