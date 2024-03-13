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

class PatchedSearchRequest(object):
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
        'metadata': 'list[SearchMetadataRequest]',
        'query': 'str'
    }

    attribute_map = {
        'metadata': 'metadata',
        'query': 'query'
    }

    def __init__(self, metadata=None, query=None):  # noqa: E501
        """PatchedSearchRequest - a model defined in Swagger"""  # noqa: E501
        self._metadata = None
        self._query = None
        self.discriminator = None
        if metadata is not None:
            self.metadata = metadata
        if query is not None:
            self.query = query

    @property
    def metadata(self):
        """Gets the metadata of this PatchedSearchRequest.  # noqa: E501


        :return: The metadata of this PatchedSearchRequest.  # noqa: E501
        :rtype: list[SearchMetadataRequest]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this PatchedSearchRequest.


        :param metadata: The metadata of this PatchedSearchRequest.  # noqa: E501
        :type: list[SearchMetadataRequest]
        """

        self._metadata = metadata

    @property
    def query(self):
        """Gets the query of this PatchedSearchRequest.  # noqa: E501


        :return: The query of this PatchedSearchRequest.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this PatchedSearchRequest.


        :param query: The query of this PatchedSearchRequest.  # noqa: E501
        :type: str
        """

        self._query = query

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
        if issubclass(PatchedSearchRequest, dict):
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
        if not isinstance(other, PatchedSearchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
