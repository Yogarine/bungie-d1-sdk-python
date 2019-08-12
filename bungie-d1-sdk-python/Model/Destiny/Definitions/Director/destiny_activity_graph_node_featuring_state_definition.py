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


class DestinyActivityGraphNodeFeaturingStateDefinition(object):
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
        'highlight_type': 'ActivityGraphNodeHighlightType'
    }

    attribute_map = {
        'highlight_type': 'highlightType'
    }

    def __init__(self, highlight_type=None):  # noqa: E501
        """DestinyActivityGraphNodeFeaturingStateDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._highlight_type = None
        self.discriminator = None

        if highlight_type is not None:
            self.highlight_type = highlight_type

    @property
    def highlight_type(self):
        """Gets the highlight_type of this DestinyActivityGraphNodeFeaturingStateDefinition.  # noqa: E501

        The node can be highlighted in a variety of ways - the game iterates through these and finds the first FeaturingState that is valid at the present moment given the Game, Account, and Character state, and renders the node in that state. See the ActivityGraphNodeHighlightType enum for possible values.  # noqa: E501

        :return: The highlight_type of this DestinyActivityGraphNodeFeaturingStateDefinition.  # noqa: E501
        :rtype: ActivityGraphNodeHighlightType
        """
        return self._highlight_type

    @highlight_type.setter
    def highlight_type(self, highlight_type):
        """Sets the highlight_type of this DestinyActivityGraphNodeFeaturingStateDefinition.

        The node can be highlighted in a variety of ways - the game iterates through these and finds the first FeaturingState that is valid at the present moment given the Game, Account, and Character state, and renders the node in that state. See the ActivityGraphNodeHighlightType enum for possible values.  # noqa: E501

        :param highlight_type: The highlight_type of this DestinyActivityGraphNodeFeaturingStateDefinition.  # noqa: E501
        :type: ActivityGraphNodeHighlightType
        """

        self._highlight_type = highlight_type

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
        if not isinstance(other, DestinyActivityGraphNodeFeaturingStateDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
