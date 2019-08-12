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


class DestinyItemQualityBlockDefinition(object):
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
        'item_levels': 'list[int]',
        'quality_level': 'int',
        'infusion_category_name': 'str',
        'infusion_category_hash': 'int',
        'infusion_category_hashes': 'list[int]',
        'progression_level_requirement_hash': 'int'
    }

    attribute_map = {
        'item_levels': 'itemLevels',
        'quality_level': 'qualityLevel',
        'infusion_category_name': 'infusionCategoryName',
        'infusion_category_hash': 'infusionCategoryHash',
        'infusion_category_hashes': 'infusionCategoryHashes',
        'progression_level_requirement_hash': 'progressionLevelRequirementHash'
    }

    def __init__(self, item_levels=None, quality_level=None, infusion_category_name=None, infusion_category_hash=None, infusion_category_hashes=None, progression_level_requirement_hash=None):  # noqa: E501
        """DestinyItemQualityBlockDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._item_levels = None
        self._quality_level = None
        self._infusion_category_name = None
        self._infusion_category_hash = None
        self._infusion_category_hashes = None
        self._progression_level_requirement_hash = None
        self.discriminator = None

        if item_levels is not None:
            self.item_levels = item_levels
        if quality_level is not None:
            self.quality_level = quality_level
        if infusion_category_name is not None:
            self.infusion_category_name = infusion_category_name
        if infusion_category_hash is not None:
            self.infusion_category_hash = infusion_category_hash
        if infusion_category_hashes is not None:
            self.infusion_category_hashes = infusion_category_hashes
        if progression_level_requirement_hash is not None:
            self.progression_level_requirement_hash = progression_level_requirement_hash

    @property
    def item_levels(self):
        """Gets the item_levels of this DestinyItemQualityBlockDefinition.  # noqa: E501

        The \"base\" defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item.  In practice, not only was that never done in Destiny 1, but now this isn't even populated at all. When it's not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result.  # noqa: E501

        :return: The item_levels of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._item_levels

    @item_levels.setter
    def item_levels(self, item_levels):
        """Sets the item_levels of this DestinyItemQualityBlockDefinition.

        The \"base\" defined level of an item. This is a list because, in theory, each Expansion could define its own base level for an item.  In practice, not only was that never done in Destiny 1, but now this isn't even populated at all. When it's not populated, the level at which it spawns has to be inferred by Reward information, of which BNet receives an imperfect view and will only be reliable on instanced data as a result.  # noqa: E501

        :param item_levels: The item_levels of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :type: list[int]
        """

        self._item_levels = item_levels

    @property
    def quality_level(self):
        """Gets the quality_level of this DestinyItemQualityBlockDefinition.  # noqa: E501

        qualityLevel is used in combination with the item's level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does.  # noqa: E501

        :return: The quality_level of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._quality_level

    @quality_level.setter
    def quality_level(self, quality_level):
        """Sets the quality_level of this DestinyItemQualityBlockDefinition.

        qualityLevel is used in combination with the item's level to calculate stats like Attack and Defense. It plays a role in that calculation, but not nearly as large as itemLevel does.  # noqa: E501

        :param quality_level: The quality_level of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :type: int
        """

        self._quality_level = quality_level

    @property
    def infusion_category_name(self):
        """Gets the infusion_category_name of this DestinyItemQualityBlockDefinition.  # noqa: E501

        The string identifier for this item's \"infusability\", if any.   Items that match the same infusionCategoryName are allowed to infuse with each other.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.  # noqa: E501

        :return: The infusion_category_name of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :rtype: str
        """
        return self._infusion_category_name

    @infusion_category_name.setter
    def infusion_category_name(self, infusion_category_name):
        """Sets the infusion_category_name of this DestinyItemQualityBlockDefinition.

        The string identifier for this item's \"infusability\", if any.   Items that match the same infusionCategoryName are allowed to infuse with each other.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.  # noqa: E501

        :param infusion_category_name: The infusion_category_name of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :type: str
        """

        self._infusion_category_name = infusion_category_name

    @property
    def infusion_category_hash(self):
        """Gets the infusion_category_hash of this DestinyItemQualityBlockDefinition.  # noqa: E501

        The hash identifier for the infusion. It does not map to a Definition entity.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.  # noqa: E501

        :return: The infusion_category_hash of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._infusion_category_hash

    @infusion_category_hash.setter
    def infusion_category_hash(self, infusion_category_hash):
        """Sets the infusion_category_hash of this DestinyItemQualityBlockDefinition.

        The hash identifier for the infusion. It does not map to a Definition entity.  DEPRECATED: Items can now have multiple infusion categories. Please use infusionCategoryHashes instead.  # noqa: E501

        :param infusion_category_hash: The infusion_category_hash of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :type: int
        """

        self._infusion_category_hash = infusion_category_hash

    @property
    def infusion_category_hashes(self):
        """Gets the infusion_category_hashes of this DestinyItemQualityBlockDefinition.  # noqa: E501

        If any one of these hashes matches any value in another item's infusionCategoryHashes, the two can infuse with each other.  # noqa: E501

        :return: The infusion_category_hashes of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :rtype: list[int]
        """
        return self._infusion_category_hashes

    @infusion_category_hashes.setter
    def infusion_category_hashes(self, infusion_category_hashes):
        """Sets the infusion_category_hashes of this DestinyItemQualityBlockDefinition.

        If any one of these hashes matches any value in another item's infusionCategoryHashes, the two can infuse with each other.  # noqa: E501

        :param infusion_category_hashes: The infusion_category_hashes of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :type: list[int]
        """

        self._infusion_category_hashes = infusion_category_hashes

    @property
    def progression_level_requirement_hash(self):
        """Gets the progression_level_requirement_hash of this DestinyItemQualityBlockDefinition.  # noqa: E501

        An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition.  # noqa: E501

        :return: The progression_level_requirement_hash of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :rtype: int
        """
        return self._progression_level_requirement_hash

    @progression_level_requirement_hash.setter
    def progression_level_requirement_hash(self, progression_level_requirement_hash):
        """Sets the progression_level_requirement_hash of this DestinyItemQualityBlockDefinition.

        An item can refer to pre-set level requirements. They are defined in DestinyProgressionLevelRequirementDefinition, and you can use this hash to find the appropriate definition.  # noqa: E501

        :param progression_level_requirement_hash: The progression_level_requirement_hash of this DestinyItemQualityBlockDefinition.  # noqa: E501
        :type: int
        """

        self._progression_level_requirement_hash = progression_level_requirement_hash

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
        if not isinstance(other, DestinyItemQualityBlockDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
