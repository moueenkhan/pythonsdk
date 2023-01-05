# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class VendorInformation(object):

    """Implementation of the 'VendorInformation' model.

    TODO: type model description here.

    Attributes:
        id (string): ID of the vendor
        name (string): Name of the vendor
        primary_email (string): primaryEmail of the vendor
        secondary_email (string): secondaryEmail of the vendor
        contact_number (string): contactNumber of the vendor

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "primary_email": 'primaryEmail',
        "secondary_email": 'secondaryEmail',
        "contact_number": 'contactNumber'
    }

    _optionals = [
        'primary_email',
        'secondary_email',
        'contact_number',
    ]

    def __init__(self,
                 id=None,
                 name=None,
                 primary_email=APIHelper.SKIP,
                 secondary_email=APIHelper.SKIP,
                 contact_number=APIHelper.SKIP):
        """Constructor for the VendorInformation class"""

        # Initialize members of the class
        self.id = id 
        self.name = name 
        if primary_email is not APIHelper.SKIP:
            self.primary_email = primary_email 
        if secondary_email is not APIHelper.SKIP:
            self.secondary_email = secondary_email 
        if contact_number is not APIHelper.SKIP:
            self.contact_number = contact_number 

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

        id = dictionary.get("id") if dictionary.get("id") else None
        name = dictionary.get("name") if dictionary.get("name") else None
        primary_email = dictionary.get("primaryEmail") if dictionary.get("primaryEmail") else APIHelper.SKIP
        secondary_email = dictionary.get("secondaryEmail") if dictionary.get("secondaryEmail") else APIHelper.SKIP
        contact_number = dictionary.get("contactNumber") if dictionary.get("contactNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   primary_email,
                   secondary_email,
                   contact_number)
