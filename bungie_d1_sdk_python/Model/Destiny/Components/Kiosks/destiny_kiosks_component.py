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


class DestinyKiosksComponent(object):
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
        'kiosk_items': 'dict(str, list[DestinyKioskItem])'
    }

    attribute_map = {
        'kiosk_items': 'kioskItems'
    }

    def __init__(self, kiosk_items=None):  # noqa: E501
        """DestinyKiosksComponent - a model defined in OpenAPI"""  # noqa: E501

        self._kiosk_items = None
        self.discriminator = None

        if kiosk_items is not None:
            self.kiosk_items = kiosk_items

    @property
    def kiosk_items(self):
        """Gets the kiosk_items of this DestinyKiosksComponent.  # noqa: E501

        A dictionary keyed by the Kiosk Vendor's hash identifier (use it to look up the DestinyVendorDefinition for the relevant kiosk vendor), and whose value is a list of all the items that the user can \"see\" in the Kiosk, and any other interesting metadata.  # noqa: E501

        :return: The kiosk_items of this DestinyKiosksComponent.  # noqa: E501
        :rtype: dict(str, list[DestinyKioskItem])
        """
        return self._kiosk_items

    @kiosk_items.setter
    def kiosk_items(self, kiosk_items):
        """Sets the kiosk_items of this DestinyKiosksComponent.

        A dictionary keyed by the Kiosk Vendor's hash identifier (use it to look up the DestinyVendorDefinition for the relevant kiosk vendor), and whose value is a list of all the items that the user can \"see\" in the Kiosk, and any other interesting metadata.  # noqa: E501

        :param kiosk_items: The kiosk_items of this DestinyKiosksComponent.  # noqa: E501
        :type: dict(str, list[DestinyKioskItem])
        """

        self._kiosk_items = kiosk_items

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
        if not isinstance(other, DestinyKiosksComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other