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


class DestinyProgression(object):
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
        'progression_hash': 'int',
        'daily_progress': 'int',
        'daily_limit': 'int',
        'weekly_progress': 'int',
        'weekly_limit': 'int',
        'current_progress': 'int',
        'level': 'int',
        'level_cap': 'int',
        'step_index': 'int',
        'progress_to_next_level': 'int',
        'next_level_at': 'int'
    }

    attribute_map = {
        'progression_hash': 'progressionHash',
        'daily_progress': 'dailyProgress',
        'daily_limit': 'dailyLimit',
        'weekly_progress': 'weeklyProgress',
        'weekly_limit': 'weeklyLimit',
        'current_progress': 'currentProgress',
        'level': 'level',
        'level_cap': 'levelCap',
        'step_index': 'stepIndex',
        'progress_to_next_level': 'progressToNextLevel',
        'next_level_at': 'nextLevelAt'
    }

    def __init__(self, progression_hash=None, daily_progress=None, daily_limit=None, weekly_progress=None, weekly_limit=None, current_progress=None, level=None, level_cap=None, step_index=None, progress_to_next_level=None, next_level_at=None):  # noqa: E501
        """DestinyProgression - a model defined in OpenAPI"""  # noqa: E501

        self._progression_hash = None
        self._daily_progress = None
        self._daily_limit = None
        self._weekly_progress = None
        self._weekly_limit = None
        self._current_progress = None
        self._level = None
        self._level_cap = None
        self._step_index = None
        self._progress_to_next_level = None
        self._next_level_at = None
        self.discriminator = None

        if progression_hash is not None:
            self.progression_hash = progression_hash
        if daily_progress is not None:
            self.daily_progress = daily_progress
        if daily_limit is not None:
            self.daily_limit = daily_limit
        if weekly_progress is not None:
            self.weekly_progress = weekly_progress
        if weekly_limit is not None:
            self.weekly_limit = weekly_limit
        if current_progress is not None:
            self.current_progress = current_progress
        if level is not None:
            self.level = level
        if level_cap is not None:
            self.level_cap = level_cap
        if step_index is not None:
            self.step_index = step_index
        if progress_to_next_level is not None:
            self.progress_to_next_level = progress_to_next_level
        if next_level_at is not None:
            self.next_level_at = next_level_at

    @property
    def progression_hash(self):
        """Gets the progression_hash of this DestinyProgression.  # noqa: E501

        The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.  # noqa: E501

        :return: The progression_hash of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._progression_hash

    @progression_hash.setter
    def progression_hash(self, progression_hash):
        """Sets the progression_hash of this DestinyProgression.

        The hash identifier of the Progression in question. Use it to look up the DestinyProgressionDefinition in static data.  # noqa: E501

        :param progression_hash: The progression_hash of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._progression_hash = progression_hash

    @property
    def daily_progress(self):
        """Gets the daily_progress of this DestinyProgression.  # noqa: E501

        The amount of progress earned today for this progression.  # noqa: E501

        :return: The daily_progress of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._daily_progress

    @daily_progress.setter
    def daily_progress(self, daily_progress):
        """Sets the daily_progress of this DestinyProgression.

        The amount of progress earned today for this progression.  # noqa: E501

        :param daily_progress: The daily_progress of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._daily_progress = daily_progress

    @property
    def daily_limit(self):
        """Gets the daily_limit of this DestinyProgression.  # noqa: E501

        If this progression has a daily limit, this is that limit.  # noqa: E501

        :return: The daily_limit of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._daily_limit

    @daily_limit.setter
    def daily_limit(self, daily_limit):
        """Sets the daily_limit of this DestinyProgression.

        If this progression has a daily limit, this is that limit.  # noqa: E501

        :param daily_limit: The daily_limit of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._daily_limit = daily_limit

    @property
    def weekly_progress(self):
        """Gets the weekly_progress of this DestinyProgression.  # noqa: E501

        The amount of progress earned toward this progression in the current week.  # noqa: E501

        :return: The weekly_progress of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._weekly_progress

    @weekly_progress.setter
    def weekly_progress(self, weekly_progress):
        """Sets the weekly_progress of this DestinyProgression.

        The amount of progress earned toward this progression in the current week.  # noqa: E501

        :param weekly_progress: The weekly_progress of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._weekly_progress = weekly_progress

    @property
    def weekly_limit(self):
        """Gets the weekly_limit of this DestinyProgression.  # noqa: E501

        If this progression has a weekly limit, this is that limit.  # noqa: E501

        :return: The weekly_limit of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._weekly_limit

    @weekly_limit.setter
    def weekly_limit(self, weekly_limit):
        """Sets the weekly_limit of this DestinyProgression.

        If this progression has a weekly limit, this is that limit.  # noqa: E501

        :param weekly_limit: The weekly_limit of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._weekly_limit = weekly_limit

    @property
    def current_progress(self):
        """Gets the current_progress of this DestinyProgression.  # noqa: E501

        This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)  # noqa: E501

        :return: The current_progress of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._current_progress

    @current_progress.setter
    def current_progress(self, current_progress):
        """Sets the current_progress of this DestinyProgression.

        This is the total amount of progress obtained overall for this progression (for instance, the total amount of Character Level experience earned)  # noqa: E501

        :param current_progress: The current_progress of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._current_progress = current_progress

    @property
    def level(self):
        """Gets the level of this DestinyProgression.  # noqa: E501

        This is the level of the progression (for instance, the Character Level).  # noqa: E501

        :return: The level of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this DestinyProgression.

        This is the level of the progression (for instance, the Character Level).  # noqa: E501

        :param level: The level of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._level = level

    @property
    def level_cap(self):
        """Gets the level_cap of this DestinyProgression.  # noqa: E501

        This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)  # noqa: E501

        :return: The level_cap of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._level_cap

    @level_cap.setter
    def level_cap(self, level_cap):
        """Sets the level_cap of this DestinyProgression.

        This is the maximum possible level you can achieve for this progression (for example, the maximum character level obtainable)  # noqa: E501

        :param level_cap: The level_cap of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._level_cap = level_cap

    @property
    def step_index(self):
        """Gets the step_index of this DestinyProgression.  # noqa: E501

        Progressions define their levels in \"steps\". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the \"steps\" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)  # noqa: E501

        :return: The step_index of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._step_index

    @step_index.setter
    def step_index(self, step_index):
        """Sets the step_index of this DestinyProgression.

        Progressions define their levels in \"steps\". Since the last step may be repeatable, the user may be at a higher level than the actual Step achieved in the progression. Not necessarily useful, but potentially interesting for those cruising the API. Relate this to the \"steps\" property of the DestinyProgression to see which step the user is on, if you care about that. (Note that this is Content Version dependent since it refers to indexes.)  # noqa: E501

        :param step_index: The step_index of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._step_index = step_index

    @property
    def progress_to_next_level(self):
        """Gets the progress_to_next_level of this DestinyProgression.  # noqa: E501

        The amount of progression (i.e. \"Experience\") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.  # noqa: E501

        :return: The progress_to_next_level of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._progress_to_next_level

    @progress_to_next_level.setter
    def progress_to_next_level(self, progress_to_next_level):
        """Sets the progress_to_next_level of this DestinyProgression.

        The amount of progression (i.e. \"Experience\") needed to reach the next level of this Progression. Jeez, progression is such an overloaded word.  # noqa: E501

        :param progress_to_next_level: The progress_to_next_level of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._progress_to_next_level = progress_to_next_level

    @property
    def next_level_at(self):
        """Gets the next_level_at of this DestinyProgression.  # noqa: E501

        The total amount of progression (i.e. \"Experience\") needed in order to reach the next level.  # noqa: E501

        :return: The next_level_at of this DestinyProgression.  # noqa: E501
        :rtype: int
        """
        return self._next_level_at

    @next_level_at.setter
    def next_level_at(self, next_level_at):
        """Sets the next_level_at of this DestinyProgression.

        The total amount of progression (i.e. \"Experience\") needed in order to reach the next level.  # noqa: E501

        :param next_level_at: The next_level_at of this DestinyProgression.  # noqa: E501
        :type: int
        """

        self._next_level_at = next_level_at

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
        if not isinstance(other, DestinyProgression):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
