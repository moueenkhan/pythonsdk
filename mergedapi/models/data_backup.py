# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.access_key import AccessKey
from mergedapi.models.role import Role


class DataBackup(object):

    """Implementation of the 'DataBackup' model.

    TODO: type model description here.

    Attributes:
        provider (DataBackupProviderEnum): credential provider
        access_key (AccessKey): TODO: type description here.
        role (Role): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "provider": 'provider',
        "access_key": 'accessKey',
        "role": 'role'
    }

    _optionals = [
        'provider',
        'access_key',
        'role',
    ]

    def __init__(self,
                 provider=APIHelper.SKIP,
                 access_key=APIHelper.SKIP,
                 role=APIHelper.SKIP):
        """Constructor for the DataBackup class"""

        # Initialize members of the class
        if provider is not APIHelper.SKIP:
            self.provider = provider 
        if access_key is not APIHelper.SKIP:
            self.access_key = access_key 
        if role is not APIHelper.SKIP:
            self.role = role 

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

        provider = dictionary.get("provider") if dictionary.get("provider") else APIHelper.SKIP
        access_key = AccessKey.from_dictionary(dictionary.get('accessKey')) if 'accessKey' in dictionary.keys() else APIHelper.SKIP
        role = Role.from_dictionary(dictionary.get('role')) if 'role' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(provider,
                   access_key,
                   role)
