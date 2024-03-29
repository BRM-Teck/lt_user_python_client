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

class Search(object):
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
        'id': 'int',
        'metadata': 'list[SearchMetadata]',
        'query': 'str',
        'timestamp': 'datetime',
        'user': 'int',
        'site': 'int'
    }

    attribute_map = {
        'id': 'id',
        'metadata': 'metadata',
        'query': 'query',
        'timestamp': 'timestamp',
        'user': 'user',
        'site': 'site'
    }

    def __init__(self, id=None, metadata=None, query=None, timestamp=None, user=None, site=None):  # noqa: E501
        """Search - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._metadata = None
        self._query = None
        self._timestamp = None
        self._user = None
        self._site = None
        self.discriminator = None
        self.id = id
        self.metadata = metadata
        self.query = query
        self.timestamp = timestamp
        self.user = user
        self.site = site

    @property
    def id(self):
        """Gets the id of this Search.  # noqa: E501


        :return: The id of this Search.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Search.


        :param id: The id of this Search.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def metadata(self):
        """Gets the metadata of this Search.  # noqa: E501


        :return: The metadata of this Search.  # noqa: E501
        :rtype: list[SearchMetadata]
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Search.


        :param metadata: The metadata of this Search.  # noqa: E501
        :type: list[SearchMetadata]
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def query(self):
        """Gets the query of this Search.  # noqa: E501


        :return: The query of this Search.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this Search.


        :param query: The query of this Search.  # noqa: E501
        :type: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")  # noqa: E501

        self._query = query

    @property
    def timestamp(self):
        """Gets the timestamp of this Search.  # noqa: E501


        :return: The timestamp of this Search.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Search.


        :param timestamp: The timestamp of this Search.  # noqa: E501
        :type: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")  # noqa: E501

        self._timestamp = timestamp

    @property
    def user(self):
        """Gets the user of this Search.  # noqa: E501


        :return: The user of this Search.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Search.


        :param user: The user of this Search.  # noqa: E501
        :type: int
        """
        if user is None:
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def site(self):
        """Gets the site of this Search.  # noqa: E501


        :return: The site of this Search.  # noqa: E501
        :rtype: int
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this Search.


        :param site: The site of this Search.  # noqa: E501
        :type: int
        """
        if site is None:
            raise ValueError("Invalid value for `site`, must not be `None`")  # noqa: E501

        self._site = site

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
        if issubclass(Search, dict):
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
        if not isinstance(other, Search):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
