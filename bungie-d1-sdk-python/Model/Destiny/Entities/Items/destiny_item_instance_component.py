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


class DestinyItemInstanceComponent(object):
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
        'damage_type': 'DamageType',
        'damage_type_hash': 'int',
        'primary_stat': 'DestinyStat',
        'item_level': 'int',
        'quality': 'int',
        'is_equipped': 'bool',
        'can_equip': 'bool',
        'equip_required_level': 'int',
        'unlock_hashes_required_to_equip': 'list[int]',
        'cannot_equip_reason': 'EquipFailureReason'
    }

    attribute_map = {
        'damage_type': 'damageType',
        'damage_type_hash': 'damageTypeHash',
        'primary_stat': 'primaryStat',
        'item_level': 'itemLevel',
        'quality': 'quality',
        'is_equipped': 'isEquipped',
        'can_equip': 'canEquip',
        'equip_required_level': 'equipRequiredLevel',
        'unlock_hashes_required_to_equip': 'unlockHashesRequiredToEquip',
        'cannot_equip_reason': 'cannotEquipReason'
    }

    def __init__(self, damage_type=None, damage_type_hash=None, primary_stat=None, item_level=None, quality=None, is_equipped=None, can_equip=None, equip_required_level=None, unlock_hashes_required_to_equip=None, cannot_equip_reason=None):  # noqa: E501
        """DestinyItemInstanceComponent - a model defined in OpenAPI"""  # noqa: E501

        self._damage_type = None
        self._damage_type_hash = None
        self._primary_stat = None
        self._item_level = None
        self._quality = None
        self._is_equipped = None
        self._can_equip = None
        self._equip_required_level = None
        self._unlock_hashes_required_to_equip = None
        self._cannot_equip_reason = None
        self.discriminator = None

        if damage_type is not None:
            self.damage_type = damage_type
        self.damage_type_hash = damage_type_hash
        if primary_stat is not None:
            self.primary_stat = primary_stat
        if item_level is not None:
            self.item_level = item_level
        if quality is not None:
            self.quality = quality
        if is_equipped is not None:
            self.is_equipped = is_equipped
        if can_equip is not None:
            self.can_equip = can_equip
        if equip_required_level is not None:
            self.equip_required_level = equip_required_level
        if unlock_hashes_required_to_equip is not None:
            self.unlock_hashes_required_to_equip = unlock_hashes_required_to_equip
        if cannot_equip_reason is not None:
            self.cannot_equip_reason = cannot_equip_reason

    @property
    def damage_type(self):
        """Gets the damage_type of this DestinyItemInstanceComponent.  # noqa: E501

        If the item has a damage type, this is the item's current damage type.  # noqa: E501

        :return: The damage_type of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: DamageType
        """
        return self._damage_type

    @damage_type.setter
    def damage_type(self, damage_type):
        """Sets the damage_type of this DestinyItemInstanceComponent.

        If the item has a damage type, this is the item's current damage type.  # noqa: E501

        :param damage_type: The damage_type of this DestinyItemInstanceComponent.  # noqa: E501
        :type: DamageType
        """

        self._damage_type = damage_type

    @property
    def damage_type_hash(self):
        """Gets the damage_type_hash of this DestinyItemInstanceComponent.  # noqa: E501

        The current damage type's hash, so you can look up localized info and icons for it.  # noqa: E501

        :return: The damage_type_hash of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: int
        """
        return self._damage_type_hash

    @damage_type_hash.setter
    def damage_type_hash(self, damage_type_hash):
        """Sets the damage_type_hash of this DestinyItemInstanceComponent.

        The current damage type's hash, so you can look up localized info and icons for it.  # noqa: E501

        :param damage_type_hash: The damage_type_hash of this DestinyItemInstanceComponent.  # noqa: E501
        :type: int
        """

        self._damage_type_hash = damage_type_hash

    @property
    def primary_stat(self):
        """Gets the primary_stat of this DestinyItemInstanceComponent.  # noqa: E501

        The item stat that we consider to be \"primary\" for the item. For instance, this would be \"Attack\" for Weapons or \"Defense\" for armor.  # noqa: E501

        :return: The primary_stat of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: DestinyStat
        """
        return self._primary_stat

    @primary_stat.setter
    def primary_stat(self, primary_stat):
        """Sets the primary_stat of this DestinyItemInstanceComponent.

        The item stat that we consider to be \"primary\" for the item. For instance, this would be \"Attack\" for Weapons or \"Defense\" for armor.  # noqa: E501

        :param primary_stat: The primary_stat of this DestinyItemInstanceComponent.  # noqa: E501
        :type: DestinyStat
        """

        self._primary_stat = primary_stat

    @property
    def item_level(self):
        """Gets the item_level of this DestinyItemInstanceComponent.  # noqa: E501

        The Item's \"Level\" has the most significant bearing on its stats, such as Light and Power.  # noqa: E501

        :return: The item_level of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: int
        """
        return self._item_level

    @item_level.setter
    def item_level(self, item_level):
        """Sets the item_level of this DestinyItemInstanceComponent.

        The Item's \"Level\" has the most significant bearing on its stats, such as Light and Power.  # noqa: E501

        :param item_level: The item_level of this DestinyItemInstanceComponent.  # noqa: E501
        :type: int
        """

        self._item_level = item_level

    @property
    def quality(self):
        """Gets the quality of this DestinyItemInstanceComponent.  # noqa: E501

        The \"Quality\" of the item has a lesser - but still impactful - bearing on stats like Light and Power.  # noqa: E501

        :return: The quality of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: int
        """
        return self._quality

    @quality.setter
    def quality(self, quality):
        """Sets the quality of this DestinyItemInstanceComponent.

        The \"Quality\" of the item has a lesser - but still impactful - bearing on stats like Light and Power.  # noqa: E501

        :param quality: The quality of this DestinyItemInstanceComponent.  # noqa: E501
        :type: int
        """

        self._quality = quality

    @property
    def is_equipped(self):
        """Gets the is_equipped of this DestinyItemInstanceComponent.  # noqa: E501

        Is the item currently equipped on the given character?  # noqa: E501

        :return: The is_equipped of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: bool
        """
        return self._is_equipped

    @is_equipped.setter
    def is_equipped(self, is_equipped):
        """Sets the is_equipped of this DestinyItemInstanceComponent.

        Is the item currently equipped on the given character?  # noqa: E501

        :param is_equipped: The is_equipped of this DestinyItemInstanceComponent.  # noqa: E501
        :type: bool
        """

        self._is_equipped = is_equipped

    @property
    def can_equip(self):
        """Gets the can_equip of this DestinyItemInstanceComponent.  # noqa: E501

        If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details.  # noqa: E501

        :return: The can_equip of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: bool
        """
        return self._can_equip

    @can_equip.setter
    def can_equip(self, can_equip):
        """Sets the can_equip of this DestinyItemInstanceComponent.

        If this is an equippable item, you can check it here. There are permanent as well as transitory reasons why an item might not be able to be equipped: check cannotEquipReason for details.  # noqa: E501

        :param can_equip: The can_equip of this DestinyItemInstanceComponent.  # noqa: E501
        :type: bool
        """

        self._can_equip = can_equip

    @property
    def equip_required_level(self):
        """Gets the equip_required_level of this DestinyItemInstanceComponent.  # noqa: E501

        If the item cannot be equipped until you reach a certain level, that level will be reflected here.  # noqa: E501

        :return: The equip_required_level of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: int
        """
        return self._equip_required_level

    @equip_required_level.setter
    def equip_required_level(self, equip_required_level):
        """Sets the equip_required_level of this DestinyItemInstanceComponent.

        If the item cannot be equipped until you reach a certain level, that level will be reflected here.  # noqa: E501

        :param equip_required_level: The equip_required_level of this DestinyItemInstanceComponent.  # noqa: E501
        :type: int
        """

        self._equip_required_level = equip_required_level

    @property
    def unlock_hashes_required_to_equip(self):
        """Gets the unlock_hashes_required_to_equip of this DestinyItemInstanceComponent.  # noqa: E501

        Sometimes, there are limitations to equipping that are represented by character-level flags called \"unlocks\".  This is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes.  # noqa: E501

        :return: The unlock_hashes_required_to_equip of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: list[int]
        """
        return self._unlock_hashes_required_to_equip

    @unlock_hashes_required_to_equip.setter
    def unlock_hashes_required_to_equip(self, unlock_hashes_required_to_equip):
        """Sets the unlock_hashes_required_to_equip of this DestinyItemInstanceComponent.

        Sometimes, there are limitations to equipping that are represented by character-level flags called \"unlocks\".  This is a list of flags that they need in order to equip the item that the character has not met. Use these to look up the descriptions to show in your UI by looking up the relevant DestinyUnlockDefinitions for the hashes.  # noqa: E501

        :param unlock_hashes_required_to_equip: The unlock_hashes_required_to_equip of this DestinyItemInstanceComponent.  # noqa: E501
        :type: list[int]
        """

        self._unlock_hashes_required_to_equip = unlock_hashes_required_to_equip

    @property
    def cannot_equip_reason(self):
        """Gets the cannot_equip_reason of this DestinyItemInstanceComponent.  # noqa: E501

        If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn't equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel.  # noqa: E501

        :return: The cannot_equip_reason of this DestinyItemInstanceComponent.  # noqa: E501
        :rtype: EquipFailureReason
        """
        return self._cannot_equip_reason

    @cannot_equip_reason.setter
    def cannot_equip_reason(self, cannot_equip_reason):
        """Sets the cannot_equip_reason of this DestinyItemInstanceComponent.

        If you cannot equip the item, this is a flags enum that enumerates all of the reasons why you couldn't equip the item. You may need to refine your UI further by using unlockHashesRequiredToEquip and equipRequiredLevel.  # noqa: E501

        :param cannot_equip_reason: The cannot_equip_reason of this DestinyItemInstanceComponent.  # noqa: E501
        :type: EquipFailureReason
        """

        self._cannot_equip_reason = cannot_equip_reason

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
        if not isinstance(other, DestinyItemInstanceComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
