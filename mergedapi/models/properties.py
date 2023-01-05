# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.data import Data


class Properties(object):

    """Implementation of the 'properties' model.

    Additional service support information for the MEC platform.

    Attributes:
        mtype (string): Type of additional service support information for the
            MEC platform.
        data (Data): Data about additional service support information for the
            MEC platform.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mtype": 'type',
        "data": 'data'
    }

    _optionals = [
        'mtype',
        'data',
    ]

    def __init__(self,
                 mtype=APIHelper.SKIP,
                 data=APIHelper.SKIP):
        """Constructor for the Properties class"""

        # Initialize members of the class
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if data is not APIHelper.SKIP:
            self.data = data 

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

        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        data = Data.from_dictionary(dictionary.get('data')) if 'data' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mtype,
                   data)
