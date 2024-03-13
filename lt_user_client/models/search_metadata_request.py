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

class SearchMetadataRequest(object):
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
        'key': 'str',
        'value': 'str',
        'search_request': 'int'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'search_request': 'search_request'
    }

    def __init__(self, key=None, value=None, search_request=None):  # noqa: E501
        """SearchMetadataRequest - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._value = None
        self._search_request = None
        self.discriminator = None
        self.key = key
        self.value = value
        self.search_request = search_request

    @property
    def key(self):
        """Gets the key of this SearchMetadataRequest.  # noqa: E501


        :return: The key of this SearchMetadataRequest.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this SearchMetadataRequest.


        :param key: The key of this SearchMetadataRequest.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this SearchMetadataRequest.  # noqa: E501


        :return: The value of this SearchMetadataRequest.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SearchMetadataRequest.


        :param value: The value of this SearchMetadataRequest.  # noqa: E501
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def search_request(self):
        """Gets the search_request of this SearchMetadataRequest.  # noqa: E501


        :return: The search_request of this SearchMetadataRequest.  # noqa: E501
        :rtype: int
        """
        return self._search_request

    @search_request.setter
    def search_request(self, search_request):
        """Sets the search_request of this SearchMetadataRequest.


        :param search_request: The search_request of this SearchMetadataRequest.  # noqa: E501
        :type: int
        """
        if search_request is None:
            raise ValueError("Invalid value for `search_request`, must not be `None`")  # noqa: E501

        self._search_request = search_request

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
        if issubclass(SearchMetadataRequest, dict):
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
        if not isinstance(other, SearchMetadataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other