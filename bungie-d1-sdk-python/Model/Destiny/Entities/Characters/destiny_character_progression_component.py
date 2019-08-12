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


class DestinyCharacterProgressionComponent(object):
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
        'progressions': 'dict(str, DestinyProgression)',
        'factions': 'dict(str, DestinyFactionProgression)',
        'milestones': 'dict(str, DestinyMilestone)',
        'quests': 'list[DestinyQuestStatus]',
        'uninstanced_item_objectives': 'dict(str, list[DestinyObjectiveProgress])',
        'checklists': 'dict(str, dict(str, bool))'
    }

    attribute_map = {
        'progressions': 'progressions',
        'factions': 'factions',
        'milestones': 'milestones',
        'quests': 'quests',
        'uninstanced_item_objectives': 'uninstancedItemObjectives',
        'checklists': 'checklists'
    }

    def __init__(self, progressions=None, factions=None, milestones=None, quests=None, uninstanced_item_objectives=None, checklists=None):  # noqa: E501
        """DestinyCharacterProgressionComponent - a model defined in OpenAPI"""  # noqa: E501

        self._progressions = None
        self._factions = None
        self._milestones = None
        self._quests = None
        self._uninstanced_item_objectives = None
        self._checklists = None
        self.discriminator = None

        if progressions is not None:
            self.progressions = progressions
        if factions is not None:
            self.factions = factions
        if milestones is not None:
            self.milestones = milestones
        if quests is not None:
            self.quests = quests
        if uninstanced_item_objectives is not None:
            self.uninstanced_item_objectives = uninstanced_item_objectives
        if checklists is not None:
            self.checklists = checklists

    @property
    def progressions(self):
        """Gets the progressions of this DestinyCharacterProgressionComponent.  # noqa: E501

        A Dictionary of all known progressions for the Character, keyed by the Progression's hash.  Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.  # noqa: E501

        :return: The progressions of this DestinyCharacterProgressionComponent.  # noqa: E501
        :rtype: dict(str, DestinyProgression)
        """
        return self._progressions

    @progressions.setter
    def progressions(self, progressions):
        """Sets the progressions of this DestinyCharacterProgressionComponent.

        A Dictionary of all known progressions for the Character, keyed by the Progression's hash.  Not all progressions have user-facing data, but those who do will have that data contained in the DestinyProgressionDefinition.  # noqa: E501

        :param progressions: The progressions of this DestinyCharacterProgressionComponent.  # noqa: E501
        :type: dict(str, DestinyProgression)
        """

        self._progressions = progressions

    @property
    def factions(self):
        """Gets the factions of this DestinyCharacterProgressionComponent.  # noqa: E501

        A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction.  # noqa: E501

        :return: The factions of this DestinyCharacterProgressionComponent.  # noqa: E501
        :rtype: dict(str, DestinyFactionProgression)
        """
        return self._factions

    @factions.setter
    def factions(self, factions):
        """Sets the factions of this DestinyCharacterProgressionComponent.

        A dictionary of all known Factions, keyed by the Faction's hash. It contains data about this character's status with the faction.  # noqa: E501

        :param factions: The factions of this DestinyCharacterProgressionComponent.  # noqa: E501
        :type: dict(str, DestinyFactionProgression)
        """

        self._factions = factions

    @property
    def milestones(self):
        """Gets the milestones of this DestinyCharacterProgressionComponent.  # noqa: E501

        Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status.  # noqa: E501

        :return: The milestones of this DestinyCharacterProgressionComponent.  # noqa: E501
        :rtype: dict(str, DestinyMilestone)
        """
        return self._milestones

    @milestones.setter
    def milestones(self, milestones):
        """Sets the milestones of this DestinyCharacterProgressionComponent.

        Milestones are related to the simple progressions shown in the game, but return additional and hopefully helpful information for users about the specifics of the Milestone's status.  # noqa: E501

        :param milestones: The milestones of this DestinyCharacterProgressionComponent.  # noqa: E501
        :type: dict(str, DestinyMilestone)
        """

        self._milestones = milestones

    @property
    def quests(self):
        """Gets the quests of this DestinyCharacterProgressionComponent.  # noqa: E501

        If the user has any active quests, the quests' statuses will be returned here.  Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.  # noqa: E501

        :return: The quests of this DestinyCharacterProgressionComponent.  # noqa: E501
        :rtype: list[DestinyQuestStatus]
        """
        return self._quests

    @quests.setter
    def quests(self, quests):
        """Sets the quests of this DestinyCharacterProgressionComponent.

        If the user has any active quests, the quests' statuses will be returned here.  Note that quests have been largely supplanted by Milestones, but that doesn't mean that they won't make a comeback independent of milestones at some point.  # noqa: E501

        :param quests: The quests of this DestinyCharacterProgressionComponent.  # noqa: E501
        :type: list[DestinyQuestStatus]
        """

        self._quests = quests

    @property
    def uninstanced_item_objectives(self):
        """Gets the uninstanced_item_objectives of this DestinyCharacterProgressionComponent.  # noqa: E501

        Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items.   This dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.  # noqa: E501

        :return: The uninstanced_item_objectives of this DestinyCharacterProgressionComponent.  # noqa: E501
        :rtype: dict(str, list[DestinyObjectiveProgress])
        """
        return self._uninstanced_item_objectives

    @uninstanced_item_objectives.setter
    def uninstanced_item_objectives(self, uninstanced_item_objectives):
        """Sets the uninstanced_item_objectives of this DestinyCharacterProgressionComponent.

        Sometimes, you have items in your inventory that don't have instances, but still have Objective information. This provides you that objective information for uninstanced items.   This dictionary is keyed by the item's hash: which you can use to look up the name and description for the overall task(s) implied by the objective. The value is the list of objectives for this item, and their statuses.  # noqa: E501

        :param uninstanced_item_objectives: The uninstanced_item_objectives of this DestinyCharacterProgressionComponent.  # noqa: E501
        :type: dict(str, list[DestinyObjectiveProgress])
        """

        self._uninstanced_item_objectives = uninstanced_item_objectives

    @property
    def checklists(self):
        """Gets the checklists of this DestinyCharacterProgressionComponent.  # noqa: E501

        The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)  For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.  # noqa: E501

        :return: The checklists of this DestinyCharacterProgressionComponent.  # noqa: E501
        :rtype: dict(str, dict(str, bool))
        """
        return self._checklists

    @checklists.setter
    def checklists(self, checklists):
        """Sets the checklists of this DestinyCharacterProgressionComponent.

        The set of checklists that can be examined for this specific character, keyed by the hash identifier of the Checklist (DestinyChecklistDefinition)  For each checklist returned, its value is itself a Dictionary keyed by the checklist's hash identifier with the value being a boolean indicating if it's been discovered yet.  # noqa: E501

        :param checklists: The checklists of this DestinyCharacterProgressionComponent.  # noqa: E501
        :type: dict(str, dict(str, bool))
        """

        self._checklists = checklists

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
        if not isinstance(other, DestinyCharacterProgressionComponent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other