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


class SigningServiceResponse(object):
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
        'name': 'str',
        'public_key': 'str',
        'pubkey_fingerprint': 'str',
        'script': 'str'
    }

    attribute_map = {
        'pulp_href': 'pulp_href',
        'pulp_created': 'pulp_created',
        'pulp_last_updated': 'pulp_last_updated',
        'name': 'name',
        'public_key': 'public_key',
        'pubkey_fingerprint': 'pubkey_fingerprint',
        'script': 'script'
    }

    def __init__(self, pulp_href=None, pulp_created=None, pulp_last_updated=None, name=None, public_key=None, pubkey_fingerprint=None, script=None, local_vars_configuration=None):  # noqa: E501
        """SigningServiceResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pulp_href = None
        self._pulp_created = None
        self._pulp_last_updated = None
        self._name = None
        self._public_key = None
        self._pubkey_fingerprint = None
        self._script = None
        self.discriminator = None

        if pulp_href is not None:
            self.pulp_href = pulp_href
        if pulp_created is not None:
            self.pulp_created = pulp_created
        if pulp_last_updated is not None:
            self.pulp_last_updated = pulp_last_updated
        self.name = name
        self.public_key = public_key
        self.pubkey_fingerprint = pubkey_fingerprint
        self.script = script

    @property
    def pulp_href(self):
        """Gets the pulp_href of this SigningServiceResponse.  # noqa: E501


        :return: The pulp_href of this SigningServiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._pulp_href

    @pulp_href.setter
    def pulp_href(self, pulp_href):
        """Sets the pulp_href of this SigningServiceResponse.


        :param pulp_href: The pulp_href of this SigningServiceResponse.  # noqa: E501
        :type: str
        """

        self._pulp_href = pulp_href

    @property
    def pulp_created(self):
        """Gets the pulp_created of this SigningServiceResponse.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The pulp_created of this SigningServiceResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_created

    @pulp_created.setter
    def pulp_created(self, pulp_created):
        """Sets the pulp_created of this SigningServiceResponse.

        Timestamp of creation.  # noqa: E501

        :param pulp_created: The pulp_created of this SigningServiceResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_created = pulp_created

    @property
    def pulp_last_updated(self):
        """Gets the pulp_last_updated of this SigningServiceResponse.  # noqa: E501

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :return: The pulp_last_updated of this SigningServiceResponse.  # noqa: E501
        :rtype: datetime
        """
        return self._pulp_last_updated

    @pulp_last_updated.setter
    def pulp_last_updated(self, pulp_last_updated):
        """Sets the pulp_last_updated of this SigningServiceResponse.

        Timestamp of the last time this resource was updated. Note: for immutable resources - like content, repository versions, and publication - pulp_created and pulp_last_updated dates will be the same.  # noqa: E501

        :param pulp_last_updated: The pulp_last_updated of this SigningServiceResponse.  # noqa: E501
        :type: datetime
        """

        self._pulp_last_updated = pulp_last_updated

    @property
    def name(self):
        """Gets the name of this SigningServiceResponse.  # noqa: E501

        A unique name used to recognize a script.  # noqa: E501

        :return: The name of this SigningServiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SigningServiceResponse.

        A unique name used to recognize a script.  # noqa: E501

        :param name: The name of this SigningServiceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def public_key(self):
        """Gets the public_key of this SigningServiceResponse.  # noqa: E501

        The value of a public key used for the repository verification.  # noqa: E501

        :return: The public_key of this SigningServiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this SigningServiceResponse.

        The value of a public key used for the repository verification.  # noqa: E501

        :param public_key: The public_key of this SigningServiceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and public_key is None:  # noqa: E501
            raise ValueError("Invalid value for `public_key`, must not be `None`")  # noqa: E501

        self._public_key = public_key

    @property
    def pubkey_fingerprint(self):
        """Gets the pubkey_fingerprint of this SigningServiceResponse.  # noqa: E501

        The fingerprint of the public key.  # noqa: E501

        :return: The pubkey_fingerprint of this SigningServiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._pubkey_fingerprint

    @pubkey_fingerprint.setter
    def pubkey_fingerprint(self, pubkey_fingerprint):
        """Sets the pubkey_fingerprint of this SigningServiceResponse.

        The fingerprint of the public key.  # noqa: E501

        :param pubkey_fingerprint: The pubkey_fingerprint of this SigningServiceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and pubkey_fingerprint is None:  # noqa: E501
            raise ValueError("Invalid value for `pubkey_fingerprint`, must not be `None`")  # noqa: E501

        self._pubkey_fingerprint = pubkey_fingerprint

    @property
    def script(self):
        """Gets the script of this SigningServiceResponse.  # noqa: E501

        An absolute path to a script which is going to be used for the signing.  # noqa: E501

        :return: The script of this SigningServiceResponse.  # noqa: E501
        :rtype: str
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this SigningServiceResponse.

        An absolute path to a script which is going to be used for the signing.  # noqa: E501

        :param script: The script of this SigningServiceResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and script is None:  # noqa: E501
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script

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
        if not isinstance(other, SigningServiceResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SigningServiceResponse):
            return True

        return self.to_dict() != other.to_dict()
