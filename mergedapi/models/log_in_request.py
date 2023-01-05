# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class LogInRequest(object):

    """Implementation of the 'LogInRequest' model.

    Request to initiate a Connectivity Management session and returns a VZ-M2M
    session token that is required in subsequent API requests.

    Attributes:
        username (string): The username for authentication.
        password (string): The password for authentication.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "username": 'username',
        "password": 'password'
    }

    _optionals = [
        'username',
        'password',
    ]

    def __init__(self,
                 username=APIHelper.SKIP,
                 password=APIHelper.SKIP):
        """Constructor for the LogInRequest class"""

        # Initialize members of the class
        if username is not APIHelper.SKIP:
            self.username = username 
        if password is not APIHelper.SKIP:
            self.password = password 

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

        username = dictionary.get("username") if dictionary.get("username") else APIHelper.SKIP
        password = dictionary.get("password") if dictionary.get("password") else APIHelper.SKIP
        # Return an object of this model
        return cls(username,
                   password)
