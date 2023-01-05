# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class ErrorResponse1(object):

    """Implementation of the 'ErrorResponse1' model.

    ErrorResponse attribute of a service.

    Attributes:
        code (string): Code of the error. eg: SDMS_000_000
        message (string): Brief description of the error in the form of a
            message.
        remedy_message (string): Suggestion on how to fix the issue.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "message": 'message',
        "remedy_message": 'remedyMessage'
    }

    _optionals = [
        'code',
        'message',
        'remedy_message',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 message=APIHelper.SKIP,
                 remedy_message=APIHelper.SKIP):
        """Constructor for the ErrorResponse1 class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if message is not APIHelper.SKIP:
            self.message = message 
        if remedy_message is not APIHelper.SKIP:
            self.remedy_message = remedy_message 

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

        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        remedy_message = dictionary.get("remedyMessage") if dictionary.get("remedyMessage") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   message,
                   remedy_message)
