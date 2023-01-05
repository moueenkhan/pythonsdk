# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.device_filter_without_account import DeviceFilterWithoutAccount
from mergedapi.models.device_id import DeviceId


class DeviceSuspensionStatusRequest(object):

    """Implementation of the 'DeviceSuspensionStatusRequest' model.

    Request to return service suspension information about one or more
    devices.

    Attributes:
        device_ids (list of DeviceId): The devices that you want to include in
            the request, specified by device identifier. You only need to
            provide one identifier per device.
        filter (DeviceFilterWithoutAccount): Filter for devices without
            account.
        account_name (string): The name of a billing account.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_ids": 'deviceIds',
        "filter": 'filter',
        "account_name": 'accountName'
    }

    _optionals = [
        'device_ids',
        'filter',
        'account_name',
    ]

    def __init__(self,
                 device_ids=APIHelper.SKIP,
                 filter=APIHelper.SKIP,
                 account_name=APIHelper.SKIP):
        """Constructor for the DeviceSuspensionStatusRequest class"""

        # Initialize members of the class
        if device_ids is not APIHelper.SKIP:
            self.device_ids = device_ids 
        if filter is not APIHelper.SKIP:
            self.filter = filter 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 

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

        device_ids = None
        if dictionary.get('deviceIds') is not None:
            device_ids = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        else:
            device_ids = APIHelper.SKIP
        filter = DeviceFilterWithoutAccount.from_dictionary(dictionary.get('filter')) if 'filter' in dictionary.keys() else APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_ids,
                   filter,
                   account_name)
