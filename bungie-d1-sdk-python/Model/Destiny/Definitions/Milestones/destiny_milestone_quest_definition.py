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


class DestinyMilestoneQuestDefinition(object):
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
        'quest_item_hash': 'int',
        'display_properties': 'DestinyDisplayPropertiesDefinition',
        'override_image': 'str',
        'quest_rewards': 'DestinyMilestoneQuestRewardsDefinition',
        'activities': 'dict(str, DestinyMilestoneActivityDefinition)',
        'destination_hash': 'int'
    }

    attribute_map = {
        'quest_item_hash': 'questItemHash',
        'display_properties': 'displayProperties',
        'override_image': 'overrideImage',
        'quest_rewards': 'questRewards',
        'activities': 'activities',
        'destination_hash': 'destinationHash'
    }

    def __init__(self, quest_item_hash=None, display_properties=None, override_image=None, quest_rewards=None, activities=None, destination_hash=None):  # noqa: E501
        """DestinyMilestoneQuestDefinition - a model defined in OpenAPI"""  # noqa: E501

        self._quest_item_hash = None
        self._display_properties = None
        self._override_image = None
        self._quest_rewards = None
        self._activities = None
        self._destination_hash = None
        self.discriminator = None

        if quest_item_hash is not None:
            self.quest_item_hash = quest_item_hash
        if display_properties is not None:
            self.display_properties = display_properties
        if override_image is not None:
            self.override_image = override_image
        if quest_rewards is not None:
            self.quest_rewards = quest_rewards
        if activities is not None:
            self.activities = activities
        self.destination_hash = destination_hash

    @property
    def quest_item_hash(self):
        """Gets the quest_item_hash of this DestinyMilestoneQuestDefinition.  # noqa: E501

        The item representing this Milestone quest. Use this hash to look up the DestinyInventoryItemDefinition for the quest to find its steps and human readable data.  # noqa: E501

        :return: The quest_item_hash of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :rtype: int
        """
        return self._quest_item_hash

    @quest_item_hash.setter
    def quest_item_hash(self, quest_item_hash):
        """Sets the quest_item_hash of this DestinyMilestoneQuestDefinition.

        The item representing this Milestone quest. Use this hash to look up the DestinyInventoryItemDefinition for the quest to find its steps and human readable data.  # noqa: E501

        :param quest_item_hash: The quest_item_hash of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :type: int
        """

        self._quest_item_hash = quest_item_hash

    @property
    def display_properties(self):
        """Gets the display_properties of this DestinyMilestoneQuestDefinition.  # noqa: E501

        The individual quests may have different definitions from the overall milestone: if there's a specific active quest, use these displayProperties instead of that of the overall DestinyMilestoneDefinition.  # noqa: E501

        :return: The display_properties of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :rtype: DestinyDisplayPropertiesDefinition
        """
        return self._display_properties

    @display_properties.setter
    def display_properties(self, display_properties):
        """Sets the display_properties of this DestinyMilestoneQuestDefinition.

        The individual quests may have different definitions from the overall milestone: if there's a specific active quest, use these displayProperties instead of that of the overall DestinyMilestoneDefinition.  # noqa: E501

        :param display_properties: The display_properties of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :type: DestinyDisplayPropertiesDefinition
        """

        self._display_properties = display_properties

    @property
    def override_image(self):
        """Gets the override_image of this DestinyMilestoneQuestDefinition.  # noqa: E501

        If populated, this image can be shown instead of the generic milestone's image when this quest is live, or it can be used to show a background image for the quest itself that differs from that of the Activity or the Milestone.  # noqa: E501

        :return: The override_image of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :rtype: str
        """
        return self._override_image

    @override_image.setter
    def override_image(self, override_image):
        """Sets the override_image of this DestinyMilestoneQuestDefinition.

        If populated, this image can be shown instead of the generic milestone's image when this quest is live, or it can be used to show a background image for the quest itself that differs from that of the Activity or the Milestone.  # noqa: E501

        :param override_image: The override_image of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :type: str
        """

        self._override_image = override_image

    @property
    def quest_rewards(self):
        """Gets the quest_rewards of this DestinyMilestoneQuestDefinition.  # noqa: E501

        The rewards you will get for completing this quest, as best as we could extract them from our data. Sometimes, it'll be a decent amount of data. Sometimes, it's going to be sucky. Sorry.  # noqa: E501

        :return: The quest_rewards of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :rtype: DestinyMilestoneQuestRewardsDefinition
        """
        return self._quest_rewards

    @quest_rewards.setter
    def quest_rewards(self, quest_rewards):
        """Sets the quest_rewards of this DestinyMilestoneQuestDefinition.

        The rewards you will get for completing this quest, as best as we could extract them from our data. Sometimes, it'll be a decent amount of data. Sometimes, it's going to be sucky. Sorry.  # noqa: E501

        :param quest_rewards: The quest_rewards of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :type: DestinyMilestoneQuestRewardsDefinition
        """

        self._quest_rewards = quest_rewards

    @property
    def activities(self):
        """Gets the activities of this DestinyMilestoneQuestDefinition.  # noqa: E501

        The full set of all possible \"conceptual activities\" that are related to this Milestone. Tiers or alternative modes of play within these conceptual activities will be defined as sub-entities. Keyed by the Conceptual Activity Hash. Use the key to look up DestinyActivityDefinition.  # noqa: E501

        :return: The activities of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :rtype: dict(str, DestinyMilestoneActivityDefinition)
        """
        return self._activities

    @activities.setter
    def activities(self, activities):
        """Sets the activities of this DestinyMilestoneQuestDefinition.

        The full set of all possible \"conceptual activities\" that are related to this Milestone. Tiers or alternative modes of play within these conceptual activities will be defined as sub-entities. Keyed by the Conceptual Activity Hash. Use the key to look up DestinyActivityDefinition.  # noqa: E501

        :param activities: The activities of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :type: dict(str, DestinyMilestoneActivityDefinition)
        """

        self._activities = activities

    @property
    def destination_hash(self):
        """Gets the destination_hash of this DestinyMilestoneQuestDefinition.  # noqa: E501

        Sometimes, a Milestone's quest is related to an entire Destination rather than a specific activity. In that situation, this will be the hash of that Destination. Hotspots are currently the only Milestones that expose this data, but that does not preclude this data from being returned for other Milestones in the future.  # noqa: E501

        :return: The destination_hash of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :rtype: int
        """
        return self._destination_hash

    @destination_hash.setter
    def destination_hash(self, destination_hash):
        """Sets the destination_hash of this DestinyMilestoneQuestDefinition.

        Sometimes, a Milestone's quest is related to an entire Destination rather than a specific activity. In that situation, this will be the hash of that Destination. Hotspots are currently the only Milestones that expose this data, but that does not preclude this data from being returned for other Milestones in the future.  # noqa: E501

        :param destination_hash: The destination_hash of this DestinyMilestoneQuestDefinition.  # noqa: E501
        :type: int
        """

        self._destination_hash = destination_hash

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
        if not isinstance(other, DestinyMilestoneQuestDefinition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
