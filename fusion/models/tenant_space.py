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
from fusion.models.resource_metadata import ResourceMetadata  # noqa: F401,E501

class TenantSpace(ResourceMetadata):
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
        'tenant': 'TenantRef',
        'volumes_link': 'str',
        'snapshots_link': 'str',
        'placement_groups_link': 'str'
    }
    if hasattr(ResourceMetadata, "swagger_types"):
        swagger_types.update(ResourceMetadata.swagger_types)

    attribute_map = {
        'tenant': 'tenant',
        'volumes_link': 'volumes_link',
        'snapshots_link': 'snapshots_link',
        'placement_groups_link': 'placement_groups_link'
    }
    if hasattr(ResourceMetadata, "attribute_map"):
        attribute_map.update(ResourceMetadata.attribute_map)

    def __init__(self, tenant=None, volumes_link=None, snapshots_link=None, placement_groups_link=None, *args, **kwargs):  # noqa: E501
        """TenantSpace - a model defined in Swagger"""  # noqa: E501
        self._tenant = None
        self._volumes_link = None
        self._snapshots_link = None
        self._placement_groups_link = None
        self.discriminator = None
        if tenant is not None:
            self.tenant = tenant
        if volumes_link is not None:
            self.volumes_link = volumes_link
        if snapshots_link is not None:
            self.snapshots_link = snapshots_link
        if placement_groups_link is not None:
            self.placement_groups_link = placement_groups_link
        ResourceMetadata.__init__(self, *args, **kwargs)

    @property
    def tenant(self):
        """Gets the tenant of this TenantSpace.  # noqa: E501


        :return: The tenant of this TenantSpace.  # noqa: E501
        :rtype: TenantRef
        """
        return self._tenant

    @tenant.setter
    def tenant(self, tenant):
        """Sets the tenant of this TenantSpace.


        :param tenant: The tenant of this TenantSpace.  # noqa: E501
        :type: TenantRef
        """

        self._tenant = tenant

    @property
    def volumes_link(self):
        """Gets the volumes_link of this TenantSpace.  # noqa: E501


        :return: The volumes_link of this TenantSpace.  # noqa: E501
        :rtype: str
        """
        return self._volumes_link

    @volumes_link.setter
    def volumes_link(self, volumes_link):
        """Sets the volumes_link of this TenantSpace.


        :param volumes_link: The volumes_link of this TenantSpace.  # noqa: E501
        :type: str
        """

        self._volumes_link = volumes_link

    @property
    def snapshots_link(self):
        """Gets the snapshots_link of this TenantSpace.  # noqa: E501


        :return: The snapshots_link of this TenantSpace.  # noqa: E501
        :rtype: str
        """
        return self._snapshots_link

    @snapshots_link.setter
    def snapshots_link(self, snapshots_link):
        """Sets the snapshots_link of this TenantSpace.


        :param snapshots_link: The snapshots_link of this TenantSpace.  # noqa: E501
        :type: str
        """

        self._snapshots_link = snapshots_link

    @property
    def placement_groups_link(self):
        """Gets the placement_groups_link of this TenantSpace.  # noqa: E501


        :return: The placement_groups_link of this TenantSpace.  # noqa: E501
        :rtype: str
        """
        return self._placement_groups_link

    @placement_groups_link.setter
    def placement_groups_link(self, placement_groups_link):
        """Sets the placement_groups_link of this TenantSpace.


        :param placement_groups_link: The placement_groups_link of this TenantSpace.  # noqa: E501
        :type: str
        """

        self._placement_groups_link = placement_groups_link

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
        if issubclass(TenantSpace, dict):
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
        if not isinstance(other, TenantSpace):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other