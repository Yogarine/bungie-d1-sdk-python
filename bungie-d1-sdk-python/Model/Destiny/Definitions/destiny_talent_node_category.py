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


class DestinyTalentNodeCategory(object):
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
        'identifier': 'str',
        'is_lore_driven': 'bool',
        'display_properties': 'DestinyDisplayPropertiesDefinition',
        'node_hashes': 'list[int]'
    }

    attribute_map = {
        'identifier': 'identifier',
        'is_lore_driven': 'isLoreDriven',
        'display_properties': 'displayProperties',
        'node_hashes': 'nodeHashes'
    }

    def __init__(self, identifier=None, is_lore_driven=None, display_properties=None, node_hashes=None):  # noqa: E501
        """DestinyTalentNodeCategory - a model defined in OpenAPI"""  # noqa: E501

        self._identifier = None
        self._is_lore_driven = None
        self._display_properties = None
        self._node_hashes = None
        self.discriminator = None

        if identifier is not None:
            self.identifier = identifier
        if is_lore_driven is not None:
            self.is_lore_driven = is_lore_driven
        if display_properties is not None:
            self.display_properties = display_properties
        if node_hashes is not None:
            self.node_hashes = node_hashes

    @property
    def identifier(self):
        """Gets the identifier of this DestinyTalentNodeCategory.  # noqa: E501

        Mostly just for debug purposes, but if you find it useful you can have it. This is BNet's manually created identifier for this category.  # noqa: E501

        :return: The identifier of this DestinyTalentNodeCategory.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this DestinyTalentNodeCategory.

        Mostly just for debug purposes, but if you find it useful you can have it. This is BNet's manually created identifier for this category.  # noqa: E501

        :param identifier: The identifier of this DestinyTalentNodeCategory.  # noqa: E501
        :type: str
        """

        self._identifier = identifier

    @property
    def is_lore_driven(self):
        """Gets the is_lore_driven of this DestinyTalentNodeCategory.  # noqa: E501

        If true, we found the localized content in a related DestinyLoreDefinition instead of local BNet localization files. This is mostly for ease of my own future investigations.  # noqa: E501

        :return: The is_lore_driven of this DestinyTalentNodeCategory.  # noqa: E501
        :rtype: bool
        """
        return self._is_lore_driven

    @is_lore_driven.setter
    def is_lore_driven(self, is_lore_driven):
        """Sets the is_lore_driven of this DestinyTalentNodeCategory.

        If true, we found the localized content in a related DestinyLoreDefinition instead of local BNet localization files. This is mostly for ease of my own future investigations.  # noqa: E501

        :param is_lore_driven: The is_lore_driven of this DestinyTalentNodeCategory.  # noqa: E501
        :type: bool
        """

        self._is_lore_driven = is_lore_driven

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyTalentNodeCategory.  # noqa: E501

        Will contain at least the \"name\", which will be the title of the category. We will likely not have description and an icon yet, but I'm going to keep my options open.  # noqa: E501

        :return: The display_properties of this DestinyTalentNodeCategory.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyTalentNodeCategory.

        Will contain at least the \"name\", which will be the title of the category. We will likely not have description and an icon yet, but I'm going to keep my options open.  # noqa: E501

        :param display_properties: The display_properties of this DestinyTalentNodeCategory.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def node_hashes(self):
        """Gets the node_hashes of this DestinyTalentNodeCategory.  # noqa: E501

        The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition) in this Talent Grid that are part of this Category.  # noqa: E501

        :return: The node_hashes of this DestinyTalentNodeCategory.  # noqa: E501
        :rtype: list[int]
        """
        return self._node_hashes

    @node_hashes.setter
    def node_hashes(self, node_hashes):
        """Sets the node_hashes of this DestinyTalentNodeCategory.

        The set of all hash identifiers for Talent Nodes (DestinyTalentNodeDefinition) in this Talent Grid that are part of this Category.  # noqa: E501

        :param node_hashes: The node_hashes of this DestinyTalentNodeCategory.  # noqa: E501
        :type: list[int]
        """

        self._node_hashes = node_hashes

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
        if not isinstance(other, DestinyTalentNodeCategory):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
