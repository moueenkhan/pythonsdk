# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.connection_event import ConnectionEvent


class ConnectionHistoryResponse(object):

    """Implementation of the 'ConnectionHistoryResponse' model.

    Response containing the connection history. It is a list of Network
    Connection Events for a device.

    Attributes:
        connection_history (list of ConnectionEvent): Device connection
            events, sorted by the occurredAt timestamp, oldest first.
        has_more_data (bool): False for a status 200 response.True for a
            status 202 response, indicating that there is more data to be
            retrieved. Send another request, adjusting the earliest value in
            the request based on the occuredAt value for the last device in
            the current response.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "connection_history": 'connectionHistory',
        "has_more_data": 'hasMoreData'
    }

    _optionals = [
        'connection_history',
        'has_more_data',
    ]

    def __init__(self,
                 connection_history=APIHelper.SKIP,
                 has_more_data=APIHelper.SKIP):
        """Constructor for the ConnectionHistoryResponse class"""

        # Initialize members of the class
        if connection_history is not APIHelper.SKIP:
            self.connection_history = connection_history 
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 

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

        connection_history = None
        if dictionary.get('connectionHistory') is not None:
            connection_history = [ConnectionEvent.from_dictionary(x) for x in dictionary.get('connectionHistory')]
        else:
            connection_history = APIHelper.SKIP
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(connection_history,
                   has_more_data)
