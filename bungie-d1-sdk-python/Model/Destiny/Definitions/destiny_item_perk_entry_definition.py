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


class DestinyItemPerkEntryDefinition(object):
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
        'requirement_display_string': 'str',
        'perk_hash': 'int',
        'perk_visibility': 'ItemPerkVisibility'
    }

    attribute_map = {
        'requirement_display_string': 'requirementDisplayString',
        'perk_hash': 'perkHash',
        'perk_visibility': 'perkVisibility'
    }

    def __init__(self, requirement_display_string=None, perk_hash=None, perk_visibility=None):  # noqa: E501
        """DestinyItemPerkEntryDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._requirement_display_string = None
        self._perk_hash = None
        self._perk_visibility = None
        self.discriminator = None

        if requirement_display_string is not None:
            self.requirement_display_string = requirement_display_string
        if perk_hash is not None:
            self.perk_hash = perk_hash
        if perk_visibility is not None:
            self.perk_visibility = perk_visibility

    @property
    def requirement_display_string(self):
        """Gets the requirement_display_string of this DestinyItemPerkEntryDefinition.  # noqa: E501

        If this perk is not active, this is the string to show for why it's not providing its benefits.  # noqa: E501

        :return: The requirement_display_string of this DestinyItemPerkEntryDefinition.  # noqa: E501
        :rtype: str
        """
        return self._requirement_display_string

    @requirement_display_string.setter
    def requirement_display_string(self, requirement_display_string):
        """Sets the requirement_display_string of this DestinyItemPerkEntryDefinition.

        If this perk is not active, this is the string to show for why it's not providing its benefits.  # noqa: E501

        :param requirement_display_string: The requirement_display_string of this DestinyItemPerkEntryDefinition.  # noqa: E501
        :type: str
        """

        self._requirement_display_string = requirement_display_string

    @property
    def perk_hash(self):
        """Gets the perk_hash of this DestinyItemPerkEntryDefinition.  # noqa: E501

        A hash identifier for the DestinySandboxPerkDefinition being provided on the item.  # noqa: E501

        :return: The perk_hash of this DestinyItemPerkEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._perk_hash

    @perk_hash.setter
    def perk_hash(self, perk_hash):
        """Sets the perk_hash of this DestinyItemPerkEntryDefinition.

        A hash identifier for the DestinySandboxPerkDefinition being provided on the item.  # noqa: E501

        :param perk_hash: The perk_hash of this DestinyItemPerkEntryDefinition.  # noqa: E501
        :type: int
        """

        self._perk_hash = perk_hash

    @property
    def perk_visibility(self):
        """Gets the perk_visibility of this DestinyItemPerkEntryDefinition.  # noqa: E501

        Indicates whether this perk should be shown, or if it should be shown disabled.  # noqa: E501

        :return: The perk_visibility of this DestinyItemPerkEntryDefinition.  # noqa: E501
        :rtype: ItemPerkVisibility
        """
        return self._perk_visibility

    @perk_visibility.setter
    def perk_visibility(self, perk_visibility):
        """Sets the perk_visibility of this DestinyItemPerkEntryDefinition.

        Indicates whether this perk should be shown, or if it should be shown disabled.  # noqa: E501

        :param perk_visibility: The perk_visibility of this DestinyItemPerkEntryDefinition.  # noqa: E501
        :type: ItemPerkVisibility
        """

        self._perk_visibility = perk_visibility

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
        if not isinstance(other, DestinyItemPerkEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other