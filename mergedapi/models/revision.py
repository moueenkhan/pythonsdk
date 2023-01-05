# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.additional_params import AdditionalParams


class Revision(object):

    """Implementation of the 'Revision' model.

    TODO: type model description here.

    Attributes:
        version (string): TODO: type description here.
        additional_params (list of AdditionalParams): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "version": 'version',
        "additional_params": 'additionalParams'
    }

    _optionals = [
        'additional_params',
    ]

    def __init__(self,
                 version=None,
                 additional_params=APIHelper.SKIP):
        """Constructor for the Revision class"""

        # Initialize members of the class
        self.version = version 
        if additional_params is not APIHelper.SKIP:
            self.additional_params = additional_params 

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

        version = dictionary.get("version") if dictionary.get("version") else None
        additional_params = None
        if dictionary.get('additionalParams') is not None:
            additional_params = [AdditionalParams.from_dictionary(x) for x in dictionary.get('additionalParams')]
        else:
            additional_params = APIHelper.SKIP
        # Return an object of this model
        return cls(version,
                   additional_params)
