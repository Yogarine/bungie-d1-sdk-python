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


class DestinyItemTierTypeInfusionBlock(object):
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
        'base_quality_transfer_ratio': 'float',
        'minimum_quality_increment': 'int'
    }

    attribute_map = {
        'base_quality_transfer_ratio': 'baseQualityTransferRatio',
        'minimum_quality_increment': 'minimumQualityIncrement'
    }

    def __init__(self, base_quality_transfer_ratio=None, minimum_quality_increment=None):  # noqa: E501
        """DestinyItemTierTypeInfusionBlock - a model defined in OpenAPI"""  # noqa: E501

        self._base_quality_transfer_ratio = None
        self._minimum_quality_increment = None
        self.discriminator = None

        if base_quality_transfer_ratio is not None:
            self.base_quality_transfer_ratio = base_quality_transfer_ratio
        if minimum_quality_increment is not None:
            self.minimum_quality_increment = minimum_quality_increment

    @property
    def base_quality_transfer_ratio(self):
        """Gets the base_quality_transfer_ratio of this DestinyItemTierTypeInfusionBlock.  # noqa: E501

        The default portion of quality that will transfer from the infuser to the infusee item. (InfuserQuality - InfuseeQuality) * baseQualityTransferRatio = base quality transferred.  # noqa: E501

        :return: The base_quality_transfer_ratio of this DestinyItemTierTypeInfusionBlock.  # noqa: E501
        :rtype: float
        """
        return self._base_quality_transfer_ratio

    @base_quality_transfer_ratio.setter
    def base_quality_transfer_ratio(self, base_quality_transfer_ratio):
        """Sets the base_quality_transfer_ratio of this DestinyItemTierTypeInfusionBlock.

        The default portion of quality that will transfer from the infuser to the infusee item. (InfuserQuality - InfuseeQuality) * baseQualityTransferRatio = base quality transferred.  # noqa: E501

        :param base_quality_transfer_ratio: The base_quality_transfer_ratio of this DestinyItemTierTypeInfusionBlock.  # noqa: E501
        :type: float
        """

        self._base_quality_transfer_ratio = base_quality_transfer_ratio

    @property
    def minimum_quality_increment(self):
        """Gets the minimum_quality_increment of this DestinyItemTierTypeInfusionBlock.  # noqa: E501

        As long as InfuserQuality > InfuseeQuality, the amount of quality bestowed is guaranteed to be at least this value, even if the transferRatio would dictate that it should be less. The total amount of quality that ends up in the Infusee cannot exceed the Infuser's quality however (for instance, if you infuse a 300 item with a 301 item and the minimum quality increment is 10, the infused item will not end up with 310 quality)  # noqa: E501

        :return: The minimum_quality_increment of this DestinyItemTierTypeInfusionBlock.  # noqa: E501
        :rtype: int
        """
        return self._minimum_quality_increment

    @minimum_quality_increment.setter
    def minimum_quality_increment(self, minimum_quality_increment):
        """Sets the minimum_quality_increment of this DestinyItemTierTypeInfusionBlock.

        As long as InfuserQuality > InfuseeQuality, the amount of quality bestowed is guaranteed to be at least this value, even if the transferRatio would dictate that it should be less. The total amount of quality that ends up in the Infusee cannot exceed the Infuser's quality however (for instance, if you infuse a 300 item with a 301 item and the minimum quality increment is 10, the infused item will not end up with 310 quality)  # noqa: E501

        :param minimum_quality_increment: The minimum_quality_increment of this DestinyItemTierTypeInfusionBlock.  # noqa: E501
        :type: int
        """

        self._minimum_quality_increment = minimum_quality_increment

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
        if not isinstance(other, DestinyItemTierTypeInfusionBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
