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

class DocumentRequest(object):
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
        'file': 'str',
        'title': 'str',
        'description': 'str',
        'display_html': 'str',
        'published': 'bool',
        'category': 'int',
        'document_type': 'int',
        'publisher': 'int',
        'related_documents': 'list[int]',
        'sites': 'list[int]'
    }

    attribute_map = {
        'file': 'file',
        'title': 'title',
        'description': 'description',
        'display_html': 'display_html',
        'published': 'published',
        'category': 'category',
        'document_type': 'document_type',
        'publisher': 'publisher',
        'related_documents': 'related_documents',
        'sites': 'sites'
    }

    def __init__(self, file=None, title=None, description=None, display_html=None, published=None, category=None, document_type=None, publisher=None, related_documents=None, sites=None):  # noqa: E501
        """DocumentRequest - a model defined in Swagger"""  # noqa: E501
        self._file = None
        self._title = None
        self._description = None
        self._display_html = None
        self._published = None
        self._category = None
        self._document_type = None
        self._publisher = None
        self._related_documents = None
        self._sites = None
        self.discriminator = None
        self.file = file
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        self.display_html = display_html
        if published is not None:
            self.published = published
        self.category = category
        if document_type is not None:
            self.document_type = document_type
        if publisher is not None:
            self.publisher = publisher
        if related_documents is not None:
            self.related_documents = related_documents
        self.sites = sites

    @property
    def file(self):
        """Gets the file of this DocumentRequest.  # noqa: E501


        :return: The file of this DocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this DocumentRequest.


        :param file: The file of this DocumentRequest.  # noqa: E501
        :type: str
        """
        if file is None:
            raise ValueError("Invalid value for `file`, must not be `None`")  # noqa: E501

        self._file = file

    @property
    def title(self):
        """Gets the title of this DocumentRequest.  # noqa: E501


        :return: The title of this DocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DocumentRequest.


        :param title: The title of this DocumentRequest.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this DocumentRequest.  # noqa: E501


        :return: The description of this DocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentRequest.


        :param description: The description of this DocumentRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def display_html(self):
        """Gets the display_html of this DocumentRequest.  # noqa: E501

        The HTML to display the document. Use the following placeholders: {title}, {description}, {file_url}  # noqa: E501

        :return: The display_html of this DocumentRequest.  # noqa: E501
        :rtype: str
        """
        return self._display_html

    @display_html.setter
    def display_html(self, display_html):
        """Sets the display_html of this DocumentRequest.

        The HTML to display the document. Use the following placeholders: {title}, {description}, {file_url}  # noqa: E501

        :param display_html: The display_html of this DocumentRequest.  # noqa: E501
        :type: str
        """
        if display_html is None:
            raise ValueError("Invalid value for `display_html`, must not be `None`")  # noqa: E501

        self._display_html = display_html

    @property
    def published(self):
        """Gets the published of this DocumentRequest.  # noqa: E501


        :return: The published of this DocumentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._published

    @published.setter
    def published(self, published):
        """Sets the published of this DocumentRequest.


        :param published: The published of this DocumentRequest.  # noqa: E501
        :type: bool
        """

        self._published = published

    @property
    def category(self):
        """Gets the category of this DocumentRequest.  # noqa: E501


        :return: The category of this DocumentRequest.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this DocumentRequest.


        :param category: The category of this DocumentRequest.  # noqa: E501
        :type: int
        """
        if category is None:
            raise ValueError("Invalid value for `category`, must not be `None`")  # noqa: E501

        self._category = category

    @property
    def document_type(self):
        """Gets the document_type of this DocumentRequest.  # noqa: E501


        :return: The document_type of this DocumentRequest.  # noqa: E501
        :rtype: int
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this DocumentRequest.


        :param document_type: The document_type of this DocumentRequest.  # noqa: E501
        :type: int
        """

        self._document_type = document_type

    @property
    def publisher(self):
        """Gets the publisher of this DocumentRequest.  # noqa: E501


        :return: The publisher of this DocumentRequest.  # noqa: E501
        :rtype: int
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this DocumentRequest.


        :param publisher: The publisher of this DocumentRequest.  # noqa: E501
        :type: int
        """

        self._publisher = publisher

    @property
    def related_documents(self):
        """Gets the related_documents of this DocumentRequest.  # noqa: E501


        :return: The related_documents of this DocumentRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._related_documents

    @related_documents.setter
    def related_documents(self, related_documents):
        """Sets the related_documents of this DocumentRequest.


        :param related_documents: The related_documents of this DocumentRequest.  # noqa: E501
        :type: list[int]
        """

        self._related_documents = related_documents

    @property
    def sites(self):
        """Gets the sites of this DocumentRequest.  # noqa: E501


        :return: The sites of this DocumentRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this DocumentRequest.


        :param sites: The sites of this DocumentRequest.  # noqa: E501
        :type: list[int]
        """
        if sites is None:
            raise ValueError("Invalid value for `sites`, must not be `None`")  # noqa: E501

        self._sites = sites

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
        if issubclass(DocumentRequest, dict):
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
        if not isinstance(other, DocumentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other