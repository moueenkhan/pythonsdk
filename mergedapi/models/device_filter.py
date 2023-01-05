# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.kv_pair import KvPair


class DeviceFilter(object):

    """Implementation of the 'DeviceFilter' model.

    Specify the kind of the device identifier, the type of match, and the
    string that you want to match.

    Attributes:
        account (string): The the billing account that the devices belong to.
        group_name (string): Only include devices that are in this device
            group.
        service_plan (string): Only include devices that have this service
            plan.
        custom_fields (list of KvPair): Custom field names and values, if you
            want to only include devices that have matching values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account": 'account',
        "group_name": 'groupName',
        "service_plan": 'servicePlan',
        "custom_fields": 'customFields'
    }

    _optionals = [
        'account',
        'group_name',
        'service_plan',
        'custom_fields',
    ]

    def __init__(self,
                 account=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP):
        """Constructor for the DeviceFilter class"""

        # Initialize members of the class
        if account is not APIHelper.SKIP:
            self.account = account 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 

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

        account = dictionary.get("account") if dictionary.get("account") else APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [KvPair.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        # Return an object of this model
        return cls(account,
                   group_name,
                   service_plan,
                   custom_fields)
