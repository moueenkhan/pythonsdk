# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class DeleteServiceProfile(object):

    """Implementation of the 'DeleteServiceProfile' model.

    Response on successful deletion of service profile

    Attributes:
        status (string): TODO: type description here.
        message (string): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "message": 'message'
    }

    _optionals = [
        'status',
        'message',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 message=APIHelper.SKIP):
        """Constructor for the DeleteServiceProfile class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        if message is not APIHelper.SKIP:
            self.message = message 

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

        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   message)
