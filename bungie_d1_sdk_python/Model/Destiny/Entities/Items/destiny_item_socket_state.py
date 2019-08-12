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


class DestinyItemSocketState(object):
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
        'plug_hash': 'int',
        'is_enabled': 'bool',
        'is_visible': 'bool',
        'enable_fail_indexes': 'list[int]',
        'reusable_plug_hashes': 'list[int]',
        'plug_objectives': 'list[DestinyObjectiveProgress]',
        'reusable_plugs': 'list[DestinyItemPlug]'
    }

    attribute_map = {
        'plug_hash': 'plugHash',
        'is_enabled': 'isEnabled',
        'is_visible': 'isVisible',
        'enable_fail_indexes': 'enableFailIndexes',
        'reusable_plug_hashes': 'reusablePlugHashes',
        'plug_objectives': 'plugObjectives',
        'reusable_plugs': 'reusablePlugs'
    }

    def __init__(self, plug_hash=None, is_enabled=None, is_visible=None, enable_fail_indexes=None, reusable_plug_hashes=None, plug_objectives=None, reusable_plugs=None):  # noqa: E501
        """DestinyItemSocketState - a model defined in OpenAPI"""  # noqa: E501

        self._plug_hash = None
        self._is_enabled = None
        self._is_visible = None
        self._enable_fail_indexes = None
        self._reusable_plug_hashes = None
        self._plug_objectives = None
        self._reusable_plugs = None
        self.discriminator = None

        self.plug_hash = plug_hash
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if is_visible is not None:
            self.is_visible = is_visible
        if enable_fail_indexes is not None:
            self.enable_fail_indexes = enable_fail_indexes
        if reusable_plug_hashes is not None:
            self.reusable_plug_hashes = reusable_plug_hashes
        if plug_objectives is not None:
            self.plug_objectives = plug_objectives
        if reusable_plugs is not None:
            self.reusable_plugs = reusable_plugs

    @property
    def plug_hash(self):
        """Gets the plug_hash of this DestinyItemSocketState.  # noqa: E501

        The currently active plug, if any.  Note that, because all plugs are statically defined, its effect on stats and perks can be statically determined using the plug item's definition. The stats and perks can be taken at face value on the plug item as the stats and perks it will provide to the user/item.  # noqa: E501

        :return: The plug_hash of this DestinyItemSocketState.  # noqa: E501
        :rtype: int
        """
        return self._plug_hash

    @plug_hash.setter
    def plug_hash(self, plug_hash):
        """Sets the plug_hash of this DestinyItemSocketState.

        The currently active plug, if any.  Note that, because all plugs are statically defined, its effect on stats and perks can be statically determined using the plug item's definition. The stats and perks can be taken at face value on the plug item as the stats and perks it will provide to the user/item.  # noqa: E501

        :param plug_hash: The plug_hash of this DestinyItemSocketState.  # noqa: E501
        :type: int
        """

        self._plug_hash = plug_hash

    @property
    def is_enabled(self):
        """Gets the is_enabled of this DestinyItemSocketState.  # noqa: E501

        Even if a plug is inserted, it doesn't mean it's enabled.  This flag indicates whether the plug is active and providing its benefits.  # noqa: E501

        :return: The is_enabled of this DestinyItemSocketState.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this DestinyItemSocketState.

        Even if a plug is inserted, it doesn't mean it's enabled.  This flag indicates whether the plug is active and providing its benefits.  # noqa: E501

        :param is_enabled: The is_enabled of this DestinyItemSocketState.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def is_visible(self):
        """Gets the is_visible of this DestinyItemSocketState.  # noqa: E501

        A plug may theoretically provide benefits but not be visible - for instance, some older items use a plug's damage type perk to modify their own damage type. These, though they are not visible, still affect the item. This field indicates that state.  An invisible plug, while it provides benefits if it is Enabled, cannot be directly modified by the user.  # noqa: E501

        :return: The is_visible of this DestinyItemSocketState.  # noqa: E501
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """Sets the is_visible of this DestinyItemSocketState.

        A plug may theoretically provide benefits but not be visible - for instance, some older items use a plug's damage type perk to modify their own damage type. These, though they are not visible, still affect the item. This field indicates that state.  An invisible plug, while it provides benefits if it is Enabled, cannot be directly modified by the user.  # noqa: E501

        :param is_visible: The is_visible of this DestinyItemSocketState.  # noqa: E501
        :type: bool
        """

        self._is_visible = is_visible

    @property
    def enable_fail_indexes(self):
        """Gets the enable_fail_indexes of this DestinyItemSocketState.  # noqa: E501

        If a plug is inserted but not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.  # noqa: E501

        :return: The enable_fail_indexes of this DestinyItemSocketState.  # noqa: E501
        :rtype: list[int]
        """
        return self._enable_fail_indexes

    @enable_fail_indexes.setter
    def enable_fail_indexes(self, enable_fail_indexes):
        """Sets the enable_fail_indexes of this DestinyItemSocketState.

        If a plug is inserted but not enabled, this will be populated with indexes into the plug item definition's plug.enabledRules property, so that you can show the reasons why it is not enabled.  # noqa: E501

        :param enable_fail_indexes: The enable_fail_indexes of this DestinyItemSocketState.  # noqa: E501
        :type: list[int]
        """

        self._enable_fail_indexes = enable_fail_indexes

    @property
    def reusable_plug_hashes(self):
        """Gets the reusable_plug_hashes of this DestinyItemSocketState.  # noqa: E501

        If the item supports reusable plugs, this is the list of plug item hashes that are currently allowed to be used for this socket. See the \"reusablePlugs\" property, which has rendered this obsolete, for more information.  # noqa: E501

        :return: The reusable_plug_hashes of this DestinyItemSocketState.  # noqa: E501
        :rtype: list[int]
        """
        return self._reusable_plug_hashes

    @reusable_plug_hashes.setter
    def reusable_plug_hashes(self, reusable_plug_hashes):
        """Sets the reusable_plug_hashes of this DestinyItemSocketState.

        If the item supports reusable plugs, this is the list of plug item hashes that are currently allowed to be used for this socket. See the \"reusablePlugs\" property, which has rendered this obsolete, for more information.  # noqa: E501

        :param reusable_plug_hashes: The reusable_plug_hashes of this DestinyItemSocketState.  # noqa: E501
        :type: list[int]
        """

        self._reusable_plug_hashes = reusable_plug_hashes

    @property
    def plug_objectives(self):
        """Gets the plug_objectives of this DestinyItemSocketState.  # noqa: E501

        Sometimes, Plugs may have objectives: generally, these are used for flavor and display purposes. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.  # noqa: E501

        :return: The plug_objectives of this DestinyItemSocketState.  # noqa: E501
        :rtype: list[DestinyObjectiveProgress]
        """
        return self._plug_objectives

    @plug_objectives.setter
    def plug_objectives(self, plug_objectives):
        """Sets the plug_objectives of this DestinyItemSocketState.

        Sometimes, Plugs may have objectives: generally, these are used for flavor and display purposes. For instance, a Plug might be tracking the number of PVP kills you have made. It will use the parent item's data about that tracking status to determine what to show, and will generally show it using the DestinyObjectiveDefinition's progressDescription property. Refer to the plug's itemHash and objective property for more information if you would like to display even more data.  # noqa: E501

        :param plug_objectives: The plug_objectives of this DestinyItemSocketState.  # noqa: E501
        :type: list[DestinyObjectiveProgress]
        """

        self._plug_objectives = plug_objectives

    @property
    def reusable_plugs(self):
        """Gets the reusable_plugs of this DestinyItemSocketState.  # noqa: E501

        If the item supports reusable plugs, this is the list of plugs that are allowed to be used for the socket, and any relevant information about whether they are \"enabled\", whether they are allowed to be inserted, and any other information such as objectives.  A Reusable Plug is a plug that you can always insert into this socket as long as its insertion rules are passed, regardless of whether or not you have the plug in your inventory. An example of it failing an insertion rule would be if it has an Objective that needs to be completed before it can be inserted, and that objective hasn't been completed yet.  In practice, a socket will *either* have reusable plugs *or* it will allow for plugs in your inventory to be inserted. See DestinyInventoryItemDefinition.socket for more info.  # noqa: E501

        :return: The reusable_plugs of this DestinyItemSocketState.  # noqa: E501
        :rtype: list[DestinyItemPlug]
        """
        return self._reusable_plugs

    @reusable_plugs.setter
    def reusable_plugs(self, reusable_plugs):
        """Sets the reusable_plugs of this DestinyItemSocketState.

        If the item supports reusable plugs, this is the list of plugs that are allowed to be used for the socket, and any relevant information about whether they are \"enabled\", whether they are allowed to be inserted, and any other information such as objectives.  A Reusable Plug is a plug that you can always insert into this socket as long as its insertion rules are passed, regardless of whether or not you have the plug in your inventory. An example of it failing an insertion rule would be if it has an Objective that needs to be completed before it can be inserted, and that objective hasn't been completed yet.  In practice, a socket will *either* have reusable plugs *or* it will allow for plugs in your inventory to be inserted. See DestinyInventoryItemDefinition.socket for more info.  # noqa: E501

        :param reusable_plugs: The reusable_plugs of this DestinyItemSocketState.  # noqa: E501
        :type: list[DestinyItemPlug]
        """

        self._reusable_plugs = reusable_plugs

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
        if not isinstance(other, DestinyItemSocketState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other