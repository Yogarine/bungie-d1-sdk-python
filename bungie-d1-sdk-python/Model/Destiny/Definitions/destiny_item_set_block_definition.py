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


class DestinyItemSetBlockDefinition(object):
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
        'item_list': 'list[DestinyItemSetBlockEntryDefinition]',
        'require_ordered_set_item_add': 'bool',
        'set_is_featured': 'bool',
        'set_type': 'str'
    }

    attribute_map = {
        'item_list': 'itemList',
        'require_ordered_set_item_add': 'requireOrderedSetItemAdd',
        'set_is_featured': 'setIsFeatured',
        'set_type': 'setType'
    }

    def __init__(self, item_list=None, require_ordered_set_item_add=None, set_is_featured=None, set_type=None):  # noqa: E501
        """DestinyItemSetBlockDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._item_list = None
        self._require_ordered_set_item_add = None
        self._set_is_featured = None
        self._set_type = None
        self.discriminator = None

        if item_list is not None:
            self.item_list = item_list
        if require_ordered_set_item_add is not None:
            self.require_ordered_set_item_add = require_ordered_set_item_add
        if set_is_featured is not None:
            self.set_is_featured = set_is_featured
        if set_type is not None:
            self.set_type = set_type

    @property
    def item_list(self):
        """Gets the item_list of this DestinyItemSetBlockDefinition.  # noqa: E501

        A collection of hashes of set items, for items such as Quest Metadata items that possess this data.  # noqa: E501

        :return: The item_list of this DestinyItemSetBlockDefinition.  # noqa: E501
        :rtype: list[DestinyItemSetBlockEntryDefinition]
        """
        return self._item_list

    @item_list.setter
    def item_list(self, item_list):
        """Sets the item_list of this DestinyItemSetBlockDefinition.

        A collection of hashes of set items, for items such as Quest Metadata items that possess this data.  # noqa: E501

        :param item_list: The item_list of this DestinyItemSetBlockDefinition.  # noqa: E501
        :type: list[DestinyItemSetBlockEntryDefinition]
        """

        self._item_list = item_list

    @property
    def require_ordered_set_item_add(self):
        """Gets the require_ordered_set_item_add of this DestinyItemSetBlockDefinition.  # noqa: E501

        If true, items in the set can only be added in increasing order, and adding an item will remove any previous item. For Quests, this is by necessity true. Only one quest step is present at a time, and previous steps are removed as you advance in the quest.  # noqa: E501

        :return: The require_ordered_set_item_add of this DestinyItemSetBlockDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._require_ordered_set_item_add

    @require_ordered_set_item_add.setter
    def require_ordered_set_item_add(self, require_ordered_set_item_add):
        """Sets the require_ordered_set_item_add of this DestinyItemSetBlockDefinition.

        If true, items in the set can only be added in increasing order, and adding an item will remove any previous item. For Quests, this is by necessity true. Only one quest step is present at a time, and previous steps are removed as you advance in the quest.  # noqa: E501

        :param require_ordered_set_item_add: The require_ordered_set_item_add of this DestinyItemSetBlockDefinition.  # noqa: E501
        :type: bool
        """

        self._require_ordered_set_item_add = require_ordered_set_item_add

    @property
    def set_is_featured(self):
        """Gets the set_is_featured of this DestinyItemSetBlockDefinition.  # noqa: E501

        If true, the UI should treat this quest as \"featured\"  # noqa: E501

        :return: The set_is_featured of this DestinyItemSetBlockDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._set_is_featured

    @set_is_featured.setter
    def set_is_featured(self, set_is_featured):
        """Sets the set_is_featured of this DestinyItemSetBlockDefinition.

        If true, the UI should treat this quest as \"featured\"  # noqa: E501

        :param set_is_featured: The set_is_featured of this DestinyItemSetBlockDefinition.  # noqa: E501
        :type: bool
        """

        self._set_is_featured = set_is_featured

    @property
    def set_type(self):
        """Gets the set_type of this DestinyItemSetBlockDefinition.  # noqa: E501

        A string identifier we can use to attempt to identify the category of the Quest.  # noqa: E501

        :return: The set_type of this DestinyItemSetBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._set_type

    @set_type.setter
    def set_type(self, set_type):
        """Sets the set_type of this DestinyItemSetBlockDefinition.

        A string identifier we can use to attempt to identify the category of the Quest.  # noqa: E501

        :param set_type: The set_type of this DestinyItemSetBlockDefinition.  # noqa: E501
        :type: str
        """

        self._set_type = set_type

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
        if not isinstance(other, DestinyItemSetBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
