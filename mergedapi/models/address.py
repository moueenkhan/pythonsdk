# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class Address(object):

    """Implementation of the 'Address' model.

    The customer address for the line’s primary place of use, for line usage
    taxation.

    Attributes:
        address_line_1 (string): The street address for the line’s primary
            place of use. This must be a physical address for taxation; it
            cannot be a P.O. box.
        address_line_2 (string): Optional additional street address
            information.
        city (string): The city for the line’s primary place of use.
        state (string): The state for the line’s primary place of use.
        zip (string): The ZIP code for the line’s primary place of use.
        zip_4 (string): The ZIP+4 for the line’s primary place of use.
        country (string): Either “US” or “USA” for the country of the line’s
            primary place of use.
        phone (string): A phone number where the customer can be reached.
        phone_type (string): A single letter to indicate the customer phone
            type.
        email_address (string): An email address for the customer.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_line_1": 'addressLine1',
        "city": 'city',
        "state": 'state',
        "zip": 'zip',
        "country": 'country',
        "address_line_2": 'addressLine2',
        "zip_4": 'zip4',
        "phone": 'phone',
        "phone_type": 'phoneType',
        "email_address": 'emailAddress'
    }

    _optionals = [
        'address_line_2',
        'zip_4',
        'phone',
        'phone_type',
        'email_address',
    ]

    def __init__(self,
                 address_line_1=None,
                 city=None,
                 state=None,
                 zip=None,
                 country=None,
                 address_line_2=APIHelper.SKIP,
                 zip_4=APIHelper.SKIP,
                 phone=APIHelper.SKIP,
                 phone_type=APIHelper.SKIP,
                 email_address=APIHelper.SKIP):
        """Constructor for the Address class"""

        # Initialize members of the class
        self.address_line_1 = address_line_1 
        if address_line_2 is not APIHelper.SKIP:
            self.address_line_2 = address_line_2 
        self.city = city 
        self.state = state 
        self.zip = zip 
        if zip_4 is not APIHelper.SKIP:
            self.zip_4 = zip_4 
        self.country = country 
        if phone is not APIHelper.SKIP:
            self.phone = phone 
        if phone_type is not APIHelper.SKIP:
            self.phone_type = phone_type 
        if email_address is not APIHelper.SKIP:
            self.email_address = email_address 

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

        address_line_1 = dictionary.get("addressLine1") if dictionary.get("addressLine1") else None
        city = dictionary.get("city") if dictionary.get("city") else None
        state = dictionary.get("state") if dictionary.get("state") else None
        zip = dictionary.get("zip") if dictionary.get("zip") else None
        country = dictionary.get("country") if dictionary.get("country") else None
        address_line_2 = dictionary.get("addressLine2") if dictionary.get("addressLine2") else APIHelper.SKIP
        zip_4 = dictionary.get("zip4") if dictionary.get("zip4") else APIHelper.SKIP
        phone = dictionary.get("phone") if dictionary.get("phone") else APIHelper.SKIP
        phone_type = dictionary.get("phoneType") if dictionary.get("phoneType") else APIHelper.SKIP
        email_address = dictionary.get("emailAddress") if dictionary.get("emailAddress") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_line_1,
                   city,
                   state,
                   zip,
                   country,
                   address_line_2,
                   zip_4,
                   phone,
                   phone_type,
                   email_address)
