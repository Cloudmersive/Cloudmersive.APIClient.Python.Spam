# coding: utf-8

"""
    spamapi

    Easily and directly scan and block spam security threats in input.  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class SpamDetectionResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'clean_result': 'bool'
    }

    attribute_map = {
        'clean_result': 'CleanResult'
    }

    def __init__(self, clean_result=None):  # noqa: E501
        """SpamDetectionResponse - a model defined in Swagger"""  # noqa: E501

        self._clean_result = None
        self.discriminator = None

        if clean_result is not None:
            self.clean_result = clean_result

    @property
    def clean_result(self):
        """Gets the clean_result of this SpamDetectionResponse.  # noqa: E501

        True if the result is not spam (clean), and false otherwise  # noqa: E501

        :return: The clean_result of this SpamDetectionResponse.  # noqa: E501
        :rtype: bool
        """
        return self._clean_result

    @clean_result.setter
    def clean_result(self, clean_result):
        """Sets the clean_result of this SpamDetectionResponse.

        True if the result is not spam (clean), and false otherwise  # noqa: E501

        :param clean_result: The clean_result of this SpamDetectionResponse.  # noqa: E501
        :type: bool
        """

        self._clean_result = clean_result

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(SpamDetectionResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, SpamDetectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
