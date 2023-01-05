# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.properties import Properties
from mergedapi.models.types_compute_resources import TypesComputeResources
from mergedapi.models.types_network_resources import TypesNetworkResources


class ResourcesServiceProfile2(object):

    """Implementation of the 'resources_service_profile2' model.

    Information about the resource requirements and service characteristics of
    an edge application. The `maxLatencyMs` and `clientType` parameters are
    both required in the request body. **Note:** The `maxLatencyMs` value must
    be submitted in multiples of 5. Does not include serviceProfileId

    Attributes:
        client_type (ClientTypeEnum): The category of application client.
        ecsp_filter (string): identity of the preferred Edge Computing Service
            Provider
        client_schedule (string): The expected operation schedule of the
            application client (e.g. time windows)
        client_service_area (string): The expected location(s) (e.g. route) of
            the hosting UE during the Client's operation schedule.
        network_resources (TypesNetworkResources): Network resources of a
            service profile
        compute_resources (TypesComputeResources): Compute resources of a
            service profile
        properties (Properties): Additional service support information for
            the MEC platform.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "client_type": 'clientType',
        "ecsp_filter": 'ecspFilter',
        "client_schedule": 'clientSchedule',
        "client_service_area": 'clientServiceArea',
        "network_resources": 'networkResources',
        "compute_resources": 'computeResources',
        "properties": 'properties'
    }

    _optionals = [
        'ecsp_filter',
        'client_schedule',
        'client_service_area',
        'network_resources',
        'compute_resources',
        'properties',
    ]

    def __init__(self,
                 client_type=None,
                 ecsp_filter=APIHelper.SKIP,
                 client_schedule=APIHelper.SKIP,
                 client_service_area=APIHelper.SKIP,
                 network_resources=APIHelper.SKIP,
                 compute_resources=APIHelper.SKIP,
                 properties=APIHelper.SKIP):
        """Constructor for the ResourcesServiceProfile2 class"""

        # Initialize members of the class
        self.client_type = client_type 
        if ecsp_filter is not APIHelper.SKIP:
            self.ecsp_filter = ecsp_filter 
        if client_schedule is not APIHelper.SKIP:
            self.client_schedule = client_schedule 
        if client_service_area is not APIHelper.SKIP:
            self.client_service_area = client_service_area 
        if network_resources is not APIHelper.SKIP:
            self.network_resources = network_resources 
        if compute_resources is not APIHelper.SKIP:
            self.compute_resources = compute_resources 
        if properties is not APIHelper.SKIP:
            self.properties = properties 

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

        client_type = dictionary.get("clientType") if dictionary.get("clientType") else None
        ecsp_filter = dictionary.get("ecspFilter") if dictionary.get("ecspFilter") else APIHelper.SKIP
        client_schedule = dictionary.get("clientSchedule") if dictionary.get("clientSchedule") else APIHelper.SKIP
        client_service_area = dictionary.get("clientServiceArea") if dictionary.get("clientServiceArea") else APIHelper.SKIP
        network_resources = TypesNetworkResources.from_dictionary(dictionary.get('networkResources')) if 'networkResources' in dictionary.keys() else APIHelper.SKIP
        compute_resources = TypesComputeResources.from_dictionary(dictionary.get('computeResources')) if 'computeResources' in dictionary.keys() else APIHelper.SKIP
        properties = Properties.from_dictionary(dictionary.get('properties')) if 'properties' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(client_type,
                   ecsp_filter,
                   client_schedule,
                   client_service_area,
                   network_resources,
                   compute_resources,
                   properties)
