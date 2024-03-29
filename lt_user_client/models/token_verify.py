# coding: utf-8

"""
    Snippets API

    Test description  # noqa: E501

    OpenAPI spec version: v1
    Contact: contact@snippets.local
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lt_user_client.configuration import Configuration


class TokenVerify(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'token': 'str'
    }

    attribute_map = {
        'token': 'token'
    }

    def __init__(self, token=None, _configuration=None):  # noqa: E501
        """TokenVerify - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._token = None
        self.discriminator = None

        self.token = token

    @property
    def token(self):
        """Gets the token of this TokenVerify.  # noqa: E501


        :return: The token of this TokenVerify.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenVerify.


        :param token: The token of this TokenVerify.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and token is None:
            raise ValueError("Invalid value for `token`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                token is not None and len(token) < 1):
            raise ValueError("Invalid value for `token`, length must be greater than or equal to `1`")  # noqa: E501

        self._token = token

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(TokenVerify, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TokenVerify):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TokenVerify):
            return True

        return self.to_dict() != other.to_dict()
