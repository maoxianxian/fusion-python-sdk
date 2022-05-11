# coding: utf-8

"""
    Pure Fusion API

    Pure Fusion is fully API-driven. Most APIs which change the system (POST, PATCH, DELETE) return an Operation in status \"Pending\" or \"Running\". You can poll (GET) the operation to check its status, waiting for it to change to \"Succeeded\" or \"Failed\".   # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Session(object):
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
        'availability_zone': 'AvailabilityZone',
        'protocol': 'str',
        'iscsi': 'SessionIscsi'
    }

    attribute_map = {
        'availability_zone': 'availability_zone',
        'protocol': 'protocol',
        'iscsi': 'iscsi'
    }

    def __init__(self, availability_zone=None, protocol=None, iscsi=None):  # noqa: E501
        """Session - a model defined in Swagger"""  # noqa: E501
        self._availability_zone = None
        self._protocol = None
        self._iscsi = None
        self.discriminator = None
        if availability_zone is not None:
            self.availability_zone = availability_zone
        if protocol is not None:
            self.protocol = protocol
        if iscsi is not None:
            self.iscsi = iscsi

    @property
    def availability_zone(self):
        """Gets the availability_zone of this Session.  # noqa: E501


        :return: The availability_zone of this Session.  # noqa: E501
        :rtype: AvailabilityZone
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this Session.


        :param availability_zone: The availability_zone of this Session.  # noqa: E501
        :type: AvailabilityZone
        """

        self._availability_zone = availability_zone

    @property
    def protocol(self):
        """Gets the protocol of this Session.  # noqa: E501

        Protocol name for the session.  # noqa: E501

        :return: The protocol of this Session.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Session.

        Protocol name for the session.  # noqa: E501

        :param protocol: The protocol of this Session.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def iscsi(self):
        """Gets the iscsi of this Session.  # noqa: E501


        :return: The iscsi of this Session.  # noqa: E501
        :rtype: SessionIscsi
        """
        return self._iscsi

    @iscsi.setter
    def iscsi(self, iscsi):
        """Sets the iscsi of this Session.


        :param iscsi: The iscsi of this Session.  # noqa: E501
        :type: SessionIscsi
        """

        self._iscsi = iscsi

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
        if issubclass(Session, dict):
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
        if not isinstance(other, Session):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other