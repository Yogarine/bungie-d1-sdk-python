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


class DestinyCollectibleAcquisitionBlock(object):
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
        'acquire_material_requirement_hash': 'int',
        'acquire_timestamp_unlock_value_hash': 'int'
    }

    attribute_map = {
        'acquire_material_requirement_hash': 'acquireMaterialRequirementHash',
        'acquire_timestamp_unlock_value_hash': 'acquireTimestampUnlockValueHash'
    }

    def __init__(self, acquire_material_requirement_hash=None, acquire_timestamp_unlock_value_hash=None):  # noqa: E501
        """DestinyCollectibleAcquisitionBlock - a model defined in OpenAPI"""  # noqa: E501

        self._acquire_material_requirement_hash = None
        self._acquire_timestamp_unlock_value_hash = None
        self.discriminator = None

        self.acquire_material_requirement_hash = acquire_material_requirement_hash
        self.acquire_timestamp_unlock_value_hash = acquire_timestamp_unlock_value_hash

    @property
    def acquire_material_requirement_hash(self):
        """Gets the acquire_material_requirement_hash of this DestinyCollectibleAcquisitionBlock.  # noqa: E501


        :return: The acquire_material_requirement_hash of this DestinyCollectibleAcquisitionBlock.  # noqa: E501
        :rtype: int
        """
        return self._acquire_material_requirement_hash

    @acquire_material_requirement_hash.setter
    def acquire_material_requirement_hash(self, acquire_material_requirement_hash):
        """Sets the acquire_material_requirement_hash of this DestinyCollectibleAcquisitionBlock.


        :param acquire_material_requirement_hash: The acquire_material_requirement_hash of this DestinyCollectibleAcquisitionBlock.  # noqa: E501
        :type: int
        """

        self._acquire_material_requirement_hash = acquire_material_requirement_hash

    @property
    def acquire_timestamp_unlock_value_hash(self):
        """Gets the acquire_timestamp_unlock_value_hash of this DestinyCollectibleAcquisitionBlock.  # noqa: E501


        :return: The acquire_timestamp_unlock_value_hash of this DestinyCollectibleAcquisitionBlock.  # noqa: E501
        :rtype: int
        """
        return self._acquire_timestamp_unlock_value_hash

    @acquire_timestamp_unlock_value_hash.setter
    def acquire_timestamp_unlock_value_hash(self, acquire_timestamp_unlock_value_hash):
        """Sets the acquire_timestamp_unlock_value_hash of this DestinyCollectibleAcquisitionBlock.


        :param acquire_timestamp_unlock_value_hash: The acquire_timestamp_unlock_value_hash of this DestinyCollectibleAcquisitionBlock.  # noqa: E501
        :type: int
        """

        self._acquire_timestamp_unlock_value_hash = acquire_timestamp_unlock_value_hash

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
        if not isinstance(other, DestinyCollectibleAcquisitionBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
