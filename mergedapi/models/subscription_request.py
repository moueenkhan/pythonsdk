# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class SubscriptionRequest(object):

    """Implementation of the 'SubscriptionRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (string): TODO: type description here.
        sku_number (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "sku_number": 'skuNumber'
    }

    _optionals = [
        'account_name',
        'sku_number',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 sku_number=APIHelper.SKIP):
        """Constructor for the SubscriptionRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if sku_number is not APIHelper.SKIP:
            self.sku_number = sku_number 

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
        sku_number = dictionary.get("skuNumber") if dictionary.get("skuNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   sku_number)
