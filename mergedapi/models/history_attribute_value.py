# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class HistoryAttributeValue(object):

    """Implementation of the 'HistoryAttributeValue' model.

    Streaming RF parameter for which you want to retrieve history data.

    Attributes:
        name (string): Attribute identifier
        value (string): Attribute value
        created_on (datetime): Date and time the request was created.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "value": 'value',
        "created_on": 'createdOn'
    }

    _optionals = [
        'name',
        'value',
        'created_on',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 value=APIHelper.SKIP,
                 created_on=APIHelper.SKIP):
        """Constructor for the HistoryAttributeValue class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if value is not APIHelper.SKIP:
            self.value = value 
        if created_on is not APIHelper.SKIP:
            self.created_on = APIHelper.RFC3339DateTime(created_on) if created_on else None 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        value = dictionary.get("value") if dictionary.get("value") else APIHelper.SKIP
        created_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("createdOn")).datetime if dictionary.get("createdOn") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   value,
                   created_on)
