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


class DestinyItemSocketEntryDefinition(object):
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
        'socket_type_hash': 'int',
        'single_initial_item_hash': 'int',
        'reusable_plug_items': 'list[DestinyItemSocketEntryPlugItemDefinition]',
        'prevent_initialization_on_vendor_purchase': 'bool',
        'hide_perks_in_item_tooltip': 'bool',
        'plug_sources': 'SocketPlugSources',
        'reusable_plug_set_hash': 'int',
        'randomized_plug_items': 'list[DestinyItemSocketEntryPlugItemRandomizedDefinition]',
        'default_visible': 'bool'
    }

    attribute_map = {
        'socket_type_hash': 'socketTypeHash',
        'single_initial_item_hash': 'singleInitialItemHash',
        'reusable_plug_items': 'reusablePlugItems',
        'prevent_initialization_on_vendor_purchase': 'preventInitializationOnVendorPurchase',
        'hide_perks_in_item_tooltip': 'hidePerksInItemTooltip',
        'plug_sources': 'plugSources',
        'reusable_plug_set_hash': 'reusablePlugSetHash',
        'randomized_plug_items': 'randomizedPlugItems',
        'default_visible': 'defaultVisible'
    }

    def __init__(self, socket_type_hash=None, single_initial_item_hash=None, reusable_plug_items=None, prevent_initialization_on_vendor_purchase=None, hide_perks_in_item_tooltip=None, plug_sources=None, reusable_plug_set_hash=None, randomized_plug_items=None, default_visible=None):  # noqa: E501
        """DestinyItemSocketEntryDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._socket_type_hash = None
        self._single_initial_item_hash = None
        self._reusable_plug_items = None
        self._prevent_initialization_on_vendor_purchase = None
        self._hide_perks_in_item_tooltip = None
        self._plug_sources = None
        self._reusable_plug_set_hash = None
        self._randomized_plug_items = None
        self._default_visible = None
        self.discriminator = None

        if socket_type_hash is not None:
            self.socket_type_hash = socket_type_hash
        if single_initial_item_hash is not None:
            self.single_initial_item_hash = single_initial_item_hash
        if reusable_plug_items is not None:
            self.reusable_plug_items = reusable_plug_items
        if prevent_initialization_on_vendor_purchase is not None:
            self.prevent_initialization_on_vendor_purchase = prevent_initialization_on_vendor_purchase
        if hide_perks_in_item_tooltip is not None:
            self.hide_perks_in_item_tooltip = hide_perks_in_item_tooltip
        if plug_sources is not None:
            self.plug_sources = plug_sources
        self.reusable_plug_set_hash = reusable_plug_set_hash
        if randomized_plug_items is not None:
            self.randomized_plug_items = randomized_plug_items
        if default_visible is not None:
            self.default_visible = default_visible

    @property
    def socket_type_hash(self):
        """Gets the socket_type_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501

        All sockets have a type, and this is the hash identifier for this particular type. Use it to look up the DestinySocketTypeDefinition: read there for more information on how socket types affect the behavior of the socket.  # noqa: E501

        :return: The socket_type_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._socket_type_hash

    @socket_type_hash.setter
    def socket_type_hash(self, socket_type_hash):
        """Sets the socket_type_hash of this DestinyItemSocketEntryDefinition.

        All sockets have a type, and this is the hash identifier for this particular type. Use it to look up the DestinySocketTypeDefinition: read there for more information on how socket types affect the behavior of the socket.  # noqa: E501

        :param socket_type_hash: The socket_type_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: int
        """

        self._socket_type_hash = socket_type_hash

    @property
    def single_initial_item_hash(self):
        """Gets the single_initial_item_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501

        If a valid hash, this is the hash identifier for the DestinyInventoryItemDefinition representing the Plug that will be initially inserted into the item on item creation. Otherwise, this Socket will either start without a plug inserted, or will have one randomly inserted.  # noqa: E501

        :return: The single_initial_item_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._single_initial_item_hash

    @single_initial_item_hash.setter
    def single_initial_item_hash(self, single_initial_item_hash):
        """Sets the single_initial_item_hash of this DestinyItemSocketEntryDefinition.

        If a valid hash, this is the hash identifier for the DestinyInventoryItemDefinition representing the Plug that will be initially inserted into the item on item creation. Otherwise, this Socket will either start without a plug inserted, or will have one randomly inserted.  # noqa: E501

        :param single_initial_item_hash: The single_initial_item_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: int
        """

        self._single_initial_item_hash = single_initial_item_hash

    @property
    def reusable_plug_items(self):
        """Gets the reusable_plug_items of this DestinyItemSocketEntryDefinition.  # noqa: E501

        This is a list of pre-determined plugs that can *always* be plugged into this socket, without the character having the plug in their inventory.  If this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs.  # noqa: E501

        :return: The reusable_plug_items of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: list[DestinyItemSocketEntryPlugItemDefinition]
        """
        return self._reusable_plug_items

    @reusable_plug_items.setter
    def reusable_plug_items(self, reusable_plug_items):
        """Sets the reusable_plug_items of this DestinyItemSocketEntryDefinition.

        This is a list of pre-determined plugs that can *always* be plugged into this socket, without the character having the plug in their inventory.  If this list is populated, you will not be allowed to plug an arbitrary item in the socket: you will only be able to choose from one of these reusable plugs.  # noqa: E501

        :param reusable_plug_items: The reusable_plug_items of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: list[DestinyItemSocketEntryPlugItemDefinition]
        """

        self._reusable_plug_items = reusable_plug_items

    @property
    def prevent_initialization_on_vendor_purchase(self):
        """Gets the prevent_initialization_on_vendor_purchase of this DestinyItemSocketEntryDefinition.  # noqa: E501

        If this is true, then the socket will not be initialized with a plug if the item is purchased from a Vendor.  Remember that Vendors are much more than conceptual vendors: they include \"Collection Kiosks\" and other entities. See DestinyVendorDefinition for more information.  # noqa: E501

        :return: The prevent_initialization_on_vendor_purchase of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._prevent_initialization_on_vendor_purchase

    @prevent_initialization_on_vendor_purchase.setter
    def prevent_initialization_on_vendor_purchase(self, prevent_initialization_on_vendor_purchase):
        """Sets the prevent_initialization_on_vendor_purchase of this DestinyItemSocketEntryDefinition.

        If this is true, then the socket will not be initialized with a plug if the item is purchased from a Vendor.  Remember that Vendors are much more than conceptual vendors: they include \"Collection Kiosks\" and other entities. See DestinyVendorDefinition for more information.  # noqa: E501

        :param prevent_initialization_on_vendor_purchase: The prevent_initialization_on_vendor_purchase of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: bool
        """

        self._prevent_initialization_on_vendor_purchase = prevent_initialization_on_vendor_purchase

    @property
    def hide_perks_in_item_tooltip(self):
        """Gets the hide_perks_in_item_tooltip of this DestinyItemSocketEntryDefinition.  # noqa: E501

        If this is true, the perks provided by this socket shouldn't be shown in the item's tooltip. This might be useful if it's providing a hidden bonus, or if the bonus is less important than other benefits on the item.  # noqa: E501

        :return: The hide_perks_in_item_tooltip of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._hide_perks_in_item_tooltip

    @hide_perks_in_item_tooltip.setter
    def hide_perks_in_item_tooltip(self, hide_perks_in_item_tooltip):
        """Sets the hide_perks_in_item_tooltip of this DestinyItemSocketEntryDefinition.

        If this is true, the perks provided by this socket shouldn't be shown in the item's tooltip. This might be useful if it's providing a hidden bonus, or if the bonus is less important than other benefits on the item.  # noqa: E501

        :param hide_perks_in_item_tooltip: The hide_perks_in_item_tooltip of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: bool
        """

        self._hide_perks_in_item_tooltip = hide_perks_in_item_tooltip

    @property
    def plug_sources(self):
        """Gets the plug_sources of this DestinyItemSocketEntryDefinition.  # noqa: E501

        Indicates where you should go to get plugs for this socket. This will affect how you populate your UI, as well as what plugs are valid for this socket. It's an alternative to having to check for the existence of certain properties (reusablePlugItems for example) to infer where plugs should come from.  # noqa: E501

        :return: The plug_sources of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: SocketPlugSources
        """
        return self._plug_sources

    @plug_sources.setter
    def plug_sources(self, plug_sources):
        """Sets the plug_sources of this DestinyItemSocketEntryDefinition.

        Indicates where you should go to get plugs for this socket. This will affect how you populate your UI, as well as what plugs are valid for this socket. It's an alternative to having to check for the existence of certain properties (reusablePlugItems for example) to infer where plugs should come from.  # noqa: E501

        :param plug_sources: The plug_sources of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: SocketPlugSources
        """

        self._plug_sources = plug_sources

    @property
    def reusable_plug_set_hash(self):
        """Gets the reusable_plug_set_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501

        If this socket's plugs come from a reusable DestinyPlugSetDefinition, this is the identifier for that set. We added this concept to reduce some major duplication that's going to come from sockets as replacements for what was once implemented as large sets of items and kiosks (like Emotes).  # noqa: E501

        :return: The reusable_plug_set_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: int
        """
        return self._reusable_plug_set_hash

    @reusable_plug_set_hash.setter
    def reusable_plug_set_hash(self, reusable_plug_set_hash):
        """Sets the reusable_plug_set_hash of this DestinyItemSocketEntryDefinition.

        If this socket's plugs come from a reusable DestinyPlugSetDefinition, this is the identifier for that set. We added this concept to reduce some major duplication that's going to come from sockets as replacements for what was once implemented as large sets of items and kiosks (like Emotes).  # noqa: E501

        :param reusable_plug_set_hash: The reusable_plug_set_hash of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: int
        """

        self._reusable_plug_set_hash = reusable_plug_set_hash

    @property
    def randomized_plug_items(self):
        """Gets the randomized_plug_items of this DestinyItemSocketEntryDefinition.  # noqa: E501

        As of Forsaken, item sockets can have randomized plugs. If this is populated, the live data will return a subset of plugs from this list that are active and able to be inserted into the socket just like a reusable plug.  # noqa: E501

        :return: The randomized_plug_items of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: list[DestinyItemSocketEntryPlugItemRandomizedDefinition]
        """
        return self._randomized_plug_items

    @randomized_plug_items.setter
    def randomized_plug_items(self, randomized_plug_items):
        """Sets the randomized_plug_items of this DestinyItemSocketEntryDefinition.

        As of Forsaken, item sockets can have randomized plugs. If this is populated, the live data will return a subset of plugs from this list that are active and able to be inserted into the socket just like a reusable plug.  # noqa: E501

        :param randomized_plug_items: The randomized_plug_items of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: list[DestinyItemSocketEntryPlugItemRandomizedDefinition]
        """

        self._randomized_plug_items = randomized_plug_items

    @property
    def default_visible(self):
        """Gets the default_visible of this DestinyItemSocketEntryDefinition.  # noqa: E501

        If true, then this socket is visible in the item's \"default\" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see.  # noqa: E501

        :return: The default_visible of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._default_visible

    @default_visible.setter
    def default_visible(self, default_visible):
        """Sets the default_visible of this DestinyItemSocketEntryDefinition.

        If true, then this socket is visible in the item's \"default\" state. If you have an instance, you should always check the runtime state, as that can override this visibility setting: but if you're looking at the item on a conceptual level, this property can be useful for hiding data such as legacy sockets - which remain defined on items for infrastructure purposes, but can be confusing for users to see.  # noqa: E501

        :param default_visible: The default_visible of this DestinyItemSocketEntryDefinition.  # noqa: E501
        :type: bool
        """

        self._default_visible = default_visible

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
        if not isinstance(other, DestinyItemSocketEntryDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
