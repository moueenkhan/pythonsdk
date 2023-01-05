# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class DailyUsageItem(object):

    """Implementation of the 'DailyUsageItem' model.

    Contains only dates when device had sessions

    Attributes:
        start_time (string): Start date of session. ISO 8601 format.
        end_time (string): End date of session. ISO 8601 format.
        num_bytes (int): Amount of data transferred, measured in Bytes.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_time": 'startTime',
        "end_time": 'endTime',
        "num_bytes": 'numBytes'
    }

    _optionals = [
        'start_time',
        'end_time',
        'num_bytes',
    ]

    def __init__(self,
                 start_time=APIHelper.SKIP,
                 end_time=APIHelper.SKIP,
                 num_bytes=APIHelper.SKIP):
        """Constructor for the DailyUsageItem class"""

        # Initialize members of the class
        if start_time is not APIHelper.SKIP:
            self.start_time = start_time 
        if end_time is not APIHelper.SKIP:
            self.end_time = end_time 
        if num_bytes is not APIHelper.SKIP:
            self.num_bytes = num_bytes 

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

        start_time = dictionary.get("startTime") if dictionary.get("startTime") else APIHelper.SKIP
        end_time = dictionary.get("endTime") if dictionary.get("endTime") else APIHelper.SKIP
        num_bytes = dictionary.get("numBytes") if dictionary.get("numBytes") else APIHelper.SKIP
        # Return an object of this model
        return cls(start_time,
                   end_time,
                   num_bytes)
