# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class CallbackRegistrationResponse(object):

    """Implementation of the 'CallbackRegistrationResponse' model.

    TODO: type model description here.

    Attributes:
        account (string): The name of the account that registered the callback
            URL
        name (CallbackServiceNameEnum): The name of the callback service.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account": 'account',
        "name": 'name'
    }

    _optionals = [
        'account',
        'name',
    ]

    def __init__(self,
                 account=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the CallbackRegistrationResponse class"""

        # Initialize members of the class
        if account is not APIHelper.SKIP:
            self.account = account 
        if name is not APIHelper.SKIP:
            self.name = name 

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
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        # Return an object of this model
        return cls(account,
                   name)
