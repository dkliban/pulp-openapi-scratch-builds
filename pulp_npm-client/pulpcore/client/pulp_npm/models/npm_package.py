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


class NpmPackage(object):
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
        'repository': 'str',
        'artifact': 'str',
        'relative_path': 'str',
        'file': 'file',
        'upload': 'str',
        'file_url': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'repository': 'repository',
        'artifact': 'artifact',
        'relative_path': 'relative_path',
        'file': 'file',
        'upload': 'upload',
        'file_url': 'file_url',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, repository=None, artifact=None, relative_path=None, file=None, upload=None, file_url=None, name=None, version=None, local_vars_configuration=None):  # noqa: E501
        """NpmPackage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._repository = None
        self._artifact = None
        self._relative_path = None
        self._file = None
        self._upload = None
        self._file_url = None
        self._name = None
        self._version = None
        self.discriminator = None

        if repository is not None:
            self.repository = repository
        if artifact is not None:
            self.artifact = artifact
        self.relative_path = relative_path
        if file is not None:
            self.file = file
        if upload is not None:
            self.upload = upload
        if file_url is not None:
            self.file_url = file_url
        self.name = name
        self.version = version

    @property
    def repository(self):
        """Gets the repository of this NpmPackage.  # noqa: E501

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :return: The repository of this NpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        """Sets the repository of this NpmPackage.

        A URI of a repository the new content unit should be associated with.  # noqa: E501

        :param repository: The repository of this NpmPackage.  # noqa: E501
        :type: str
        """

        self._repository = repository

    @property
    def artifact(self):
        """Gets the artifact of this NpmPackage.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this NpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this NpmPackage.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this NpmPackage.  # noqa: E501
        :type: str
        """

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this NpmPackage.  # noqa: E501


        :return: The relative_path of this NpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this NpmPackage.


        :param relative_path: The relative_path of this NpmPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and relative_path is None:  # noqa: E501
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                relative_path is not None and len(relative_path) < 1):
            raise ValueError("Invalid value for `relative_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def file(self):
        """Gets the file of this NpmPackage.  # noqa: E501

        An uploaded file that may be turned into the content unit.  # noqa: E501

        :return: The file of this NpmPackage.  # noqa: E501
        :rtype: file
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this NpmPackage.

        An uploaded file that may be turned into the content unit.  # noqa: E501

        :param file: The file of this NpmPackage.  # noqa: E501
        :type: file
        """

        self._file = file

    @property
    def upload(self):
        """Gets the upload of this NpmPackage.  # noqa: E501

        An uncommitted upload that may be turned into the content unit.  # noqa: E501

        :return: The upload of this NpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._upload

    @upload.setter
    def upload(self, upload):
        """Sets the upload of this NpmPackage.

        An uncommitted upload that may be turned into the content unit.  # noqa: E501

        :param upload: The upload of this NpmPackage.  # noqa: E501
        :type: str
        """

        self._upload = upload

    @property
    def file_url(self):
        """Gets the file_url of this NpmPackage.  # noqa: E501

        A url that Pulp can download and turn into the content unit.  # noqa: E501

        :return: The file_url of this NpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._file_url

    @file_url.setter
    def file_url(self, file_url):
        """Sets the file_url of this NpmPackage.

        A url that Pulp can download and turn into the content unit.  # noqa: E501

        :param file_url: The file_url of this NpmPackage.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                file_url is not None and len(file_url) < 1):
            raise ValueError("Invalid value for `file_url`, length must be greater than or equal to `1`")  # noqa: E501

        self._file_url = file_url

    @property
    def name(self):
        """Gets the name of this NpmPackage.  # noqa: E501


        :return: The name of this NpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NpmPackage.


        :param name: The name of this NpmPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this NpmPackage.  # noqa: E501


        :return: The version of this NpmPackage.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this NpmPackage.


        :param version: The version of this NpmPackage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                version is not None and len(version) < 1):
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

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
        if not isinstance(other, NpmPackage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NpmPackage):
            return True

        return self.to_dict() != other.to_dict()
