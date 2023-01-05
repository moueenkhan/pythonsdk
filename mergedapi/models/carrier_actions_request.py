# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.device_list import DeviceList
from mergedapi.models.kv_pair import KvPair


class CarrierActionsRequest(object):

    """Implementation of the 'CarrierActionsRequest' model.

    Request for a Carrier Actions

    Attributes:
        account_name (string): The name of a billing account.
        custom_fields (list of KvPair): Custom field names and values, if you
            want to only include devices that have matching values.
        devices (list of DeviceList): The devices for which you want to
            restore service, specified by device identifier.
        group_name (string): The name of a device group, if you want to
            restore service for all devices in that group.
        service_plan (string): The name of a service plan, if you want to only
            include devices that have that service plan.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "custom_fields": 'customFields',
        "devices": 'devices',
        "group_name": 'groupName',
        "service_plan": 'servicePlan'
    }

    _optionals = [
        'account_name',
        'custom_fields',
        'devices',
        'group_name',
        'service_plan',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 devices=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP):
        """Constructor for the CarrierActionsRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if devices is not APIHelper.SKIP:
            self.devices = devices 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary

        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [KvPair.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        devices = None
        if dictionary.get('devices') is not None:
            devices = [DeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        else:
            devices = APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   custom_fields,
                   devices,
                   group_name,
                   service_plan)
