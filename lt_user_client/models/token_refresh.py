# coding: utf-8

"""
    Legaltext API

    API for Legaltext  # noqa: E501

    OpenAPI spec version: v1.1.1a0-oas3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TokenRefresh(object):
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
        'access': 'str'
    }

    attribute_map = {
        'access': 'access'
    }

    def __init__(self, access=None):  # noqa: E501
        """TokenRefresh - a model defined in Swagger"""  # noqa: E501
        self._access = None
        self.discriminator = None
        self.access = access

    @property
    def access(self):
        """Gets the access of this TokenRefresh.  # noqa: E501


        :return: The access of this TokenRefresh.  # noqa: E501
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this TokenRefresh.


        :param access: The access of this TokenRefresh.  # noqa: E501
        :type: str
        """
        if access is None:
            raise ValueError("Invalid value for `access`, must not be `None`")  # noqa: E501

        self._access = access

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
        if issubclass(TokenRefresh, dict):
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
        if not isinstance(other, TokenRefresh):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
