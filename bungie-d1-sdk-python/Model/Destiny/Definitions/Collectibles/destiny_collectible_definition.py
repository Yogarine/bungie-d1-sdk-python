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


class DestinyCollectibleDefinition(object):
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
        'display_properties': 'DestinyDisplayPropertiesDefinition',
        'scope': 'DestinyScope',
        'source_string': 'str',
        'source_hash': 'int',
        'item_hash': 'int',
        'acquisition_info': 'DestinyCollectibleAcquisitionBlock',
        'state_info': 'DestinyCollectibleStateBlock',
        'presentation_info': 'DestinyPresentationChildBlock',
        'hash': 'int',
        'index': 'int',
        'redacted': 'bool'
    }

    attribute_map = {
        'display_properties': 'displayProperties',
        'scope': 'scope',
        'source_string': 'sourceString',
        'source_hash': 'sourceHash',
        'item_hash': 'itemHash',
        'acquisition_info': 'acquisitionInfo',
        'state_info': 'stateInfo',
        'presentation_info': 'presentationInfo',
        'hash': 'hash',
        'index': 'index',
        'redacted': 'redacted'
    }

    def __init__(self, display_properties=None, scope=None, source_string=None, source_hash=None, item_hash=None, acquisition_info=None, state_info=None, presentation_info=None, hash=None, index=None, redacted=None):  # noqa: E501
        """DestinyCollectibleDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._display_properties = None
        self._scope = None
        self._source_string = None
        self._source_hash = None
        self._item_hash = None
        self._acquisition_info = None
        self._state_info = None
        self._presentation_info = None
        self._hash = None
        self._index = None
        self._redacted = None
        self.discriminator = None

        if display_properties is not None:
            self.display_properties = display_properties
        if scope is not None:
            self.scope = scope
        if source_string is not None:
            self.source_string = source_string
        self.source_hash = source_hash
        if item_hash is not None:
            self.item_hash = item_hash
        if acquisition_info is not None:
            self.acquisition_info = acquisition_info
        if state_info is not None:
            self.state_info = state_info
        if presentation_info is not None:
            self.presentation_info = presentation_info
        if hash is not None:
            self.hash = hash
        if index is not None:
            self.index = index
        if redacted is not None:
            self.redacted = redacted

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyCollectibleDefinition.  # noqa: E501


        :return: The display_properties of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyCollectibleDefinition.


        :param display_properties: The display_properties of this DestinyCollectibleDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def scope(self):
        """Gets the scope of this DestinyCollectibleDefinition.  # noqa: E501

        Indicates whether this Collectible's state is determined on a per-character or on an account-wide basis.  # noqa: E501

        :return: The scope of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: DestinyScope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DestinyCollectibleDefinition.

        Indicates whether this Collectible's state is determined on a per-character or on an account-wide basis.  # noqa: E501

        :param scope: The scope of this DestinyCollectibleDefinition.  # noqa: E501
        :type: DestinyScope
        """

        self._scope = scope

    @property
    def source_string(self):
        """Gets the source_string of this DestinyCollectibleDefinition.  # noqa: E501

        A human readable string for a hint about how to acquire the item.  # noqa: E501

        :return: The source_string of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: str
        """
        return self._source_string

    @source_string.setter
    def source_string(self, source_string):
        """Sets the source_string of this DestinyCollectibleDefinition.

        A human readable string for a hint about how to acquire the item.  # noqa: E501

        :param source_string: The source_string of this DestinyCollectibleDefinition.  # noqa: E501
        :type: str
        """

        self._source_string = source_string

    @property
    def source_hash(self):
        """Gets the source_hash of this DestinyCollectibleDefinition.  # noqa: E501

        This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources.  I can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though.  This hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data.  # noqa: E501

        :return: The source_hash of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: int
        """
        return self._source_hash

    @source_hash.setter
    def source_hash(self, source_hash):
        """Sets the source_hash of this DestinyCollectibleDefinition.

        This is a hash identifier we are building on the BNet side in an attempt to let people group collectibles by similar sources.  I can't promise that it's going to be 100% accurate, but if the designers were consistent in assigning the same source strings to items with the same sources, it *ought to* be. No promises though.  This hash also doesn't relate to an actual definition, just to note: we've got nothing useful other than the source string for this data.  # noqa: E501

        :param source_hash: The source_hash of this DestinyCollectibleDefinition.  # noqa: E501
        :type: int
        """

        self._source_hash = source_hash

    @property
    def item_hash(self):
        """Gets the item_hash of this DestinyCollectibleDefinition.  # noqa: E501


        :return: The item_hash of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: int
        """
        return self._item_hash

    @item_hash.setter
    def item_hash(self, item_hash):
        """Sets the item_hash of this DestinyCollectibleDefinition.


        :param item_hash: The item_hash of this DestinyCollectibleDefinition.  # noqa: E501
        :type: int
        """

        self._item_hash = item_hash

    @property
    def acquisition_info(self):
        """Gets the acquisition_info of this DestinyCollectibleDefinition.  # noqa: E501


        :return: The acquisition_info of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: DestinyCollectibleAcquisitionBlock
        """
        return self._acquisition_info

    @acquisition_info.setter
    def acquisition_info(self, acquisition_info):
        """Sets the acquisition_info of this DestinyCollectibleDefinition.


        :param acquisition_info: The acquisition_info of this DestinyCollectibleDefinition.  # noqa: E501
        :type: DestinyCollectibleAcquisitionBlock
        """

        self._acquisition_info = acquisition_info

    @property
    def state_info(self):
        """Gets the state_info of this DestinyCollectibleDefinition.  # noqa: E501


        :return: The state_info of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: DestinyCollectibleStateBlock
        """
        return self._state_info

    @state_info.setter
    def state_info(self, state_info):
        """Sets the state_info of this DestinyCollectibleDefinition.


        :param state_info: The state_info of this DestinyCollectibleDefinition.  # noqa: E501
        :type: DestinyCollectibleStateBlock
        """

        self._state_info = state_info

    @property
    def presentation_info(self):
        """Gets the presentation_info of this DestinyCollectibleDefinition.  # noqa: E501


        :return: The presentation_info of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: DestinyPresentationChildBlock
        """
        return self._presentation_info

    @presentation_info.setter
    def presentation_info(self, presentation_info):
        """Sets the presentation_info of this DestinyCollectibleDefinition.


        :param presentation_info: The presentation_info of this DestinyCollectibleDefinition.  # noqa: E501
        :type: DestinyPresentationChildBlock
        """

        self._presentation_info = presentation_info

    @property
    def hash(self):
        """Gets the hash of this DestinyCollectibleDefinition.  # noqa: E501

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :return: The hash of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: int
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this DestinyCollectibleDefinition.

        The unique identifier for this entity. Guaranteed to be unique for the type of entity, but not globally.  When entities refer to each other in Destiny content, it is this hash that they are referring to.  # noqa: E501

        :param hash: The hash of this DestinyCollectibleDefinition.  # noqa: E501
        :type: int
        """

        self._hash = hash

    @property
    def index(self):
        """Gets the index of this DestinyCollectibleDefinition.  # noqa: E501

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :return: The index of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this DestinyCollectibleDefinition.

        The index of the entity as it was found in the investment tables.  # noqa: E501

        :param index: The index of this DestinyCollectibleDefinition.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def redacted(self):
        """Gets the redacted of this DestinyCollectibleDefinition.  # noqa: E501

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :return: The redacted of this DestinyCollectibleDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._redacted

    @redacted.setter
    def redacted(self, redacted):
        """Sets the redacted of this DestinyCollectibleDefinition.

        If this is true, then there is an entity with this identifier/type combination, but BNet is not yet allowed to show it. Sorry!  # noqa: E501

        :param redacted: The redacted of this DestinyCollectibleDefinition.  # noqa: E501
        :type: bool
        """

        self._redacted = redacted

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
        if not isinstance(other, DestinyCollectibleDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
