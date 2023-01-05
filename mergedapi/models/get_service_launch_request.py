# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.service_launch_request_response import ServiceLaunchRequestResponse


class GetServiceLaunchRequest(object):

    """Implementation of the 'GetServiceLaunchRequest' model.

    TODO: type model description here.

    Attributes:
        count (int): TODO: type description here.
        next (string): TODO: type description here.
        previous (string): TODO: type description here.
        result_set (list of ServiceLaunchRequestResponse): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "count": 'count',
        "next": 'next',
        "previous": 'previous',
        "result_set": 'resultSet'
    }

    _optionals = [
        'count',
        'next',
        'previous',
        'result_set',
    ]

    def __init__(self,
                 count=APIHelper.SKIP,
                 next=APIHelper.SKIP,
                 previous=APIHelper.SKIP,
                 result_set=APIHelper.SKIP):
        """Constructor for the GetServiceLaunchRequest class"""

        # Initialize members of the class
        if count is not APIHelper.SKIP:
            self.count = count 
        if next is not APIHelper.SKIP:
            self.next = next 
        if previous is not APIHelper.SKIP:
            self.previous = previous 
        if result_set is not APIHelper.SKIP:
            self.result_set = result_set 

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

        count = dictionary.get("count") if dictionary.get("count") else APIHelper.SKIP
        next = dictionary.get("next") if dictionary.get("next") else APIHelper.SKIP
        previous = dictionary.get("previous") if dictionary.get("previous") else APIHelper.SKIP
        result_set = None
        if dictionary.get('resultSet') is not None:
            result_set = [ServiceLaunchRequestResponse.from_dictionary(x) for x in dictionary.get('resultSet')]
        else:
            result_set = APIHelper.SKIP
        # Return an object of this model
        return cls(count,
                   next,
                   previous,
                   result_set)
