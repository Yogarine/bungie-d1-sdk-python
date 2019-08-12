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


class DestinyItemSetBlockEntryDefinition(object):
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
        'tracking_value': 'int',
        'item_hash': 'int'
    }

    attribute_map = {
        'tracking_value': 'trackingValue',
        'item_hash': 'itemHash'
    }

    def __init__(self, tracking_value=None, item_hash=None):  # noqa: E501
        """DestinyItemSetBlockEntryDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._tracking_value = None
        self._item_hash = None
        self.discriminator = None

        if tracking_value is not None:
            self.tracking_value = tracking_value
        if item_hash is not None:
            self.item_hash = item_hash

    @property
    def tracking_value(self):
        """Gets the tracking_value of this DestinyItemSetBlockEntryDefinition.  # noqa: E501

        Used for tracking which step a user reached. These values will be populated in the user's internal state, which we expose externally as a more usable DestinyQuestStatus object. If this item has been obtained, this value will be set in trackingUnlockValueHash.  # noqa: E501

        :return: The tracking_value of this DestinyItemSetBlockEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._tracking_value

    @tracking_value.setter
    def tracking_value(self, tracking_value):
        """Sets the tracking_value of this DestinyItemSetBlockEntryDefinition.

        Used for tracking which step a user reached. These values will be populated in the user's internal state, which we expose externally as a more usable DestinyQuestStatus object. If this item has been obtained, this value will be set in trackingUnlockValueHash.  # noqa: E501

        :param tracking_value: The tracking_value of this DestinyItemSetBlockEntryDefinition.  # noqa: E501
        :type: int
        """

        self._tracking_value = tracking_value

    @property
    def item_hash(self):
        """Gets the item_hash of this DestinyItemSetBlockEntryDefinition.  # noqa: E501

        This is the hash identifier for a DestinyInventoryItemDefinition representing this quest step.  # noqa: E501

        :return: The item_hash of this DestinyItemSetBlockEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """Sets the item_hash of this DestinyItemSetBlockEntryDefinition.

        This is the hash identifier for a DestinyInventoryItemDefinition representing this quest step.  # noqa: E501

        :param item_hash: The item_hash of this DestinyItemSetBlockEntryDefinition.  # noqa: E501
        :type: int
        """

        self._item_hash = item_hash

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
        if not isinstance(other, DestinyItemSetBlockEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other