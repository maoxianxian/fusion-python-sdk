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
from fusion.models.resource_post import ResourcePost  # noqa: F401,E501

class VolumePost(ResourcePost):
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
        'size': 'int',
        'storage_class': 'str',
        'placement_group': 'str',
        'protection_policy': 'str',
        'source_volume_snapshot_link': 'str'
    }
    if hasattr(ResourcePost, "swagger_types"):
        swagger_types.update(ResourcePost.swagger_types)

    attribute_map = {
        'size': 'size',
        'storage_class': 'storage_class',
        'placement_group': 'placement_group',
        'protection_policy': 'protection_policy',
        'source_volume_snapshot_link': 'source_volume_snapshot_link'
    }
    if hasattr(ResourcePost, "attribute_map"):
        attribute_map.update(ResourcePost.attribute_map)

    def __init__(self, size=None, storage_class=None, placement_group=None, protection_policy=None, source_volume_snapshot_link=None, *args, **kwargs):  # noqa: E501
        """VolumePost - a model defined in Swagger"""  # noqa: E501
        self._size = None
        self._storage_class = None
        self._placement_group = None
        self._protection_policy = None
        self._source_volume_snapshot_link = None
        self.discriminator = None
        self.size = size
        self.storage_class = storage_class
        self.placement_group = placement_group
        if protection_policy is not None:
            self.protection_policy = protection_policy
        if source_volume_snapshot_link is not None:
            self.source_volume_snapshot_link = source_volume_snapshot_link
        ResourcePost.__init__(self, *args, **kwargs)

    @property
    def size(self):
        """Gets the size of this VolumePost.  # noqa: E501

        The size of the volume to provision  # noqa: E501

        :return: The size of this VolumePost.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumePost.

        The size of the volume to provision  # noqa: E501

        :param size: The size of this VolumePost.  # noqa: E501
        :type: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def storage_class(self):
        """Gets the storage_class of this VolumePost.  # noqa: E501

        The name of the Storage Class  # noqa: E501

        :return: The storage_class of this VolumePost.  # noqa: E501
        :rtype: str
        """
        return self._storage_class

    @storage_class.setter
    def storage_class(self, storage_class):
        """Sets the storage_class of this VolumePost.

        The name of the Storage Class  # noqa: E501

        :param storage_class: The storage_class of this VolumePost.  # noqa: E501
        :type: str
        """
        if storage_class is None:
            raise ValueError("Invalid value for `storage_class`, must not be `None`")  # noqa: E501

        self._storage_class = storage_class

    @property
    def placement_group(self):
        """Gets the placement_group of this VolumePost.  # noqa: E501

        The name of the Placement Group  # noqa: E501

        :return: The placement_group of this VolumePost.  # noqa: E501
        :rtype: str
        """
        return self._placement_group

    @placement_group.setter
    def placement_group(self, placement_group):
        """Sets the placement_group of this VolumePost.

        The name of the Placement Group  # noqa: E501

        :param placement_group: The placement_group of this VolumePost.  # noqa: E501
        :type: str
        """
        if placement_group is None:
            raise ValueError("Invalid value for `placement_group`, must not be `None`")  # noqa: E501

        self._placement_group = placement_group

    @property
    def protection_policy(self):
        """Gets the protection_policy of this VolumePost.  # noqa: E501

        The name of the Protection Policy  # noqa: E501

        :return: The protection_policy of this VolumePost.  # noqa: E501
        :rtype: str
        """
        return self._protection_policy

    @protection_policy.setter
    def protection_policy(self, protection_policy):
        """Sets the protection_policy of this VolumePost.

        The name of the Protection Policy  # noqa: E501

        :param protection_policy: The protection_policy of this VolumePost.  # noqa: E501
        :type: str
        """

        self._protection_policy = protection_policy

    @property
    def source_volume_snapshot_link(self):
        """Gets the source_volume_snapshot_link of this VolumePost.  # noqa: E501

        Unimplemented - The link to the volume snapshot to copy data from  # noqa: E501

        :return: The source_volume_snapshot_link of this VolumePost.  # noqa: E501
        :rtype: str
        """
        return self._source_volume_snapshot_link

    @source_volume_snapshot_link.setter
    def source_volume_snapshot_link(self, source_volume_snapshot_link):
        """Sets the source_volume_snapshot_link of this VolumePost.

        Unimplemented - The link to the volume snapshot to copy data from  # noqa: E501

        :param source_volume_snapshot_link: The source_volume_snapshot_link of this VolumePost.  # noqa: E501
        :type: str
        """

        self._source_volume_snapshot_link = source_volume_snapshot_link

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
        if issubclass(VolumePost, dict):
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
        if not isinstance(other, VolumePost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other