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


class DestinyTalentNodeStepWeaponPerformances(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__0 = "0"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__1 = "1"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__2 = "2"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__4 = "4"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__8 = "8"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__16 = "16"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__32 = "32"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__64 = "64"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__128 = "128"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__256 = "256"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__512 = "512"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__1024 = "1024"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__2048 = "2048"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__4096 = "4096"
    DESTINY_TALENT_NODE_STEP_WEAPON_PERFORMANCES__8191 = "8191"

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """DestinyTalentNodeStepWeaponPerformances - a model defined in OpenAPI"""  # noqa: E501
        self.discriminator = None

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
        if not isinstance(other, DestinyTalentNodeStepWeaponPerformances):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
