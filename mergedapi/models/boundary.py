# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class Boundary(object):

    """Implementation of the 'boundary' model.

    Deployment boundary of a service.

    Attributes:
        csp (CspEnum): Cloud service provider ex: AWS_PUBLIC_CLOUD, AWS_WL,
            AWS_OUTPOST, AZURE_EDGE, AZURE_PUBLIC_CLOUD.
        region (string): Boundary region ex: US East (Ohio)
        zone_id (list of string): Zones listed under a specific region

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "csp": 'csp',
        "region": 'region',
        "zone_id": 'zoneId'
    }

    _optionals = [
        'csp',
        'region',
        'zone_id',
    ]

    def __init__(self,
                 csp='AWS_WL',
                 region=APIHelper.SKIP,
                 zone_id=APIHelper.SKIP):
        """Constructor for the Boundary class"""

        # Initialize members of the class
        self.csp = csp 
        if region is not APIHelper.SKIP:
            self.region = region 
        if zone_id is not APIHelper.SKIP:
            self.zone_id = zone_id 

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

        csp = dictionary.get("csp") if dictionary.get("csp") else 'AWS_WL'
        region = dictionary.get("region") if dictionary.get("region") else APIHelper.SKIP
        zone_id = dictionary.get("zoneId") if dictionary.get("zoneId") else APIHelper.SKIP
        # Return an object of this model
        return cls(csp,
                   region,
                   zone_id)
