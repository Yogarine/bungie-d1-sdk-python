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


class DestinyObjectiveDisplayProperties(object):
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
        'activity_hash': 'int',
        'display_on_item_preview_screen': 'bool'
    }

    attribute_map = {
        'activity_hash': 'activityHash',
        'display_on_item_preview_screen': 'displayOnItemPreviewScreen'
    }

    def __init__(self, activity_hash=None, display_on_item_preview_screen=None):  # noqa: E501
        """DestinyObjectiveDisplayProperties - a model defined in OpenAPI"""  # noqa: E501

        self._activity_hash = None
        self._display_on_item_preview_screen = None
        self.discriminator = None

        self.activity_hash = activity_hash
        if display_on_item_preview_screen is not None:
            self.display_on_item_preview_screen = display_on_item_preview_screen

    @property
    def activity_hash(self):
        """Gets the activity_hash of this DestinyObjectiveDisplayProperties.  # noqa: E501

        The activity associated with this objective in the context of this item, if any.  # noqa: E501

        :return: The activity_hash of this DestinyObjectiveDisplayProperties.  # noqa: E501
        :rtype: int
        """
        return self._activity_hash

    @activity_hash.setter
    def activity_hash(self, activity_hash):
        """Sets the activity_hash of this DestinyObjectiveDisplayProperties.

        The activity associated with this objective in the context of this item, if any.  # noqa: E501

        :param activity_hash: The activity_hash of this DestinyObjectiveDisplayProperties.  # noqa: E501
        :type: int
        """

        self._activity_hash = activity_hash

    @property
    def display_on_item_preview_screen(self):
        """Gets the display_on_item_preview_screen of this DestinyObjectiveDisplayProperties.  # noqa: E501

        If true, the game shows this objective on item preview screens.  # noqa: E501

        :return: The display_on_item_preview_screen of this DestinyObjectiveDisplayProperties.  # noqa: E501
        :rtype: bool
        """
        return self._display_on_item_preview_screen

    @display_on_item_preview_screen.setter
    def display_on_item_preview_screen(self, display_on_item_preview_screen):
        """Sets the display_on_item_preview_screen of this DestinyObjectiveDisplayProperties.

        If true, the game shows this objective on item preview screens.  # noqa: E501

        :param display_on_item_preview_screen: The display_on_item_preview_screen of this DestinyObjectiveDisplayProperties.  # noqa: E501
        :type: bool
        """

        self._display_on_item_preview_screen = display_on_item_preview_screen

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
        if not isinstance(other, DestinyObjectiveDisplayProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other