# coding: utf-8

"""
    Unofficial Bungie.net API for Destiny 1

    These are legacy endpoints for Destiny 1 that are no longer supported officially by Bungie.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: lowlines89@gmail.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class DestinyRecordTitleBlock(object):
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
        'has_title': 'bool',
        'titles_by_gender': 'dict(str, str)',
        'titles_by_gender_hash': 'dict(str, str)'
    }

    attribute_map = {
        'has_title': 'hasTitle',
        'titles_by_gender': 'titlesByGender',
        'titles_by_gender_hash': 'titlesByGenderHash'
    }

    def __init__(self, has_title=None, titles_by_gender=None, titles_by_gender_hash=None):  # noqa: E501
        """DestinyRecordTitleBlock - a model defined in OpenAPI"""  # noqa: E501

        self._has_title = None
        self._titles_by_gender = None
        self._titles_by_gender_hash = None
        self.discriminator = None

        if has_title is not None:
            self.has_title = has_title
        if titles_by_gender is not None:
            self.titles_by_gender = titles_by_gender
        if titles_by_gender_hash is not None:
            self.titles_by_gender_hash = titles_by_gender_hash

    @property
    def has_title(self):
        """Gets the has_title of this DestinyRecordTitleBlock.  # noqa: E501


        :return: The has_title of this DestinyRecordTitleBlock.  # noqa: E501
        :rtype: bool
        """
        return self._has_title

    @has_title.setter
    def has_title(self, has_title):
        """Sets the has_title of this DestinyRecordTitleBlock.


        :param has_title: The has_title of this DestinyRecordTitleBlock.  # noqa: E501
        :type: bool
        """

        self._has_title = has_title

    @property
    def titles_by_gender(self):
        """Gets the titles_by_gender of this DestinyRecordTitleBlock.  # noqa: E501


        :return: The titles_by_gender of this DestinyRecordTitleBlock.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._titles_by_gender

    @titles_by_gender.setter
    def titles_by_gender(self, titles_by_gender):
        """Sets the titles_by_gender of this DestinyRecordTitleBlock.


        :param titles_by_gender: The titles_by_gender of this DestinyRecordTitleBlock.  # noqa: E501
        :type: dict(str, str)
        """

        self._titles_by_gender = titles_by_gender

    @property
    def titles_by_gender_hash(self):
        """Gets the titles_by_gender_hash of this DestinyRecordTitleBlock.  # noqa: E501

        For those who prefer to use the definitions.  # noqa: E501

        :return: The titles_by_gender_hash of this DestinyRecordTitleBlock.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._titles_by_gender_hash

    @titles_by_gender_hash.setter
    def titles_by_gender_hash(self, titles_by_gender_hash):
        """Sets the titles_by_gender_hash of this DestinyRecordTitleBlock.

        For those who prefer to use the definitions.  # noqa: E501

        :param titles_by_gender_hash: The titles_by_gender_hash of this DestinyRecordTitleBlock.  # noqa: E501
        :type: dict(str, str)
        """

        self._titles_by_gender_hash = titles_by_gender_hash

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
        if not isinstance(other, DestinyRecordTitleBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
