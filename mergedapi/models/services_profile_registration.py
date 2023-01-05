# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.access_intents import AccessIntents
from mergedapi.models.deployment_location import DeploymentLocation
from mergedapi.models.linked_service_instance import LinkedServiceInstance
from mergedapi.models.placement_intents import PlacementIntents


class ServicesProfileRegistration(object):

    """Implementation of the 'ServicesProfileRegistration' model.

    TODO: type model description here.

    Attributes:
        id (uuid|string): Provide Service Profile Id
        name (string): Provide name for Service Profile
        service_name (string): TODO: type description here.
        service_version (string): TODO: type description here.
        current_version (string): TODO: type description here.
        version (string): TODO: type description here.
        state (StateEnum): TODO: type description here.
        customer_id (string): TODO: type description here.
        created_by (string): TODO: type description here.
        created_at (string): TODO: type description here.
        last_updated_by (string): TODO: type description here.
        last_updated_at (string): TODO: type description here.
        linked_service_instances (list of LinkedServiceInstance): TODO: type
            description here.
        access_intents (AccessIntents): TODO: type description here.
        placement_intents (PlacementIntents): TODO: type description here.
        deployment_locations (list of DeploymentLocation): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "name": 'name',
        "service_name": 'serviceName',
        "service_version": 'serviceVersion',
        "current_version": 'currentVersion',
        "version": 'version',
        "state": 'state',
        "customer_id": 'customerID',
        "created_by": 'createdBy',
        "created_at": 'createdAt',
        "last_updated_by": 'lastUpdatedBy',
        "last_updated_at": 'lastUpdatedAt',
        "linked_service_instances": 'linkedServiceInstances',
        "access_intents": 'accessIntents',
        "placement_intents": 'placementIntents',
        "deployment_locations": 'deploymentLocations'
    }

    _optionals = [
        'id',
        'name',
        'service_name',
        'service_version',
        'current_version',
        'version',
        'state',
        'customer_id',
        'created_by',
        'created_at',
        'last_updated_by',
        'last_updated_at',
        'linked_service_instances',
        'access_intents',
        'placement_intents',
        'deployment_locations',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 service_name=APIHelper.SKIP,
                 service_version=APIHelper.SKIP,
                 current_version=APIHelper.SKIP,
                 version=APIHelper.SKIP,
                 state=APIHelper.SKIP,
                 customer_id=APIHelper.SKIP,
                 created_by=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 last_updated_by=APIHelper.SKIP,
                 last_updated_at=APIHelper.SKIP,
                 linked_service_instances=APIHelper.SKIP,
                 access_intents=APIHelper.SKIP,
                 placement_intents=APIHelper.SKIP,
                 deployment_locations=APIHelper.SKIP):
        """Constructor for the ServicesProfileRegistration class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if name is not APIHelper.SKIP:
            self.name = name 
        if service_name is not APIHelper.SKIP:
            self.service_name = service_name 
        if service_version is not APIHelper.SKIP:
            self.service_version = service_version 
        if current_version is not APIHelper.SKIP:
            self.current_version = current_version 
        if version is not APIHelper.SKIP:
            self.version = version 
        if state is not APIHelper.SKIP:
            self.state = state 
        if customer_id is not APIHelper.SKIP:
            self.customer_id = customer_id 
        if created_by is not APIHelper.SKIP:
            self.created_by = created_by 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if last_updated_by is not APIHelper.SKIP:
            self.last_updated_by = last_updated_by 
        if last_updated_at is not APIHelper.SKIP:
            self.last_updated_at = last_updated_at 
        if linked_service_instances is not APIHelper.SKIP:
            self.linked_service_instances = linked_service_instances 
        if access_intents is not APIHelper.SKIP:
            self.access_intents = access_intents 
        if placement_intents is not APIHelper.SKIP:
            self.placement_intents = placement_intents 
        if deployment_locations is not APIHelper.SKIP:
            self.deployment_locations = deployment_locations 

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

        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        service_name = dictionary.get("serviceName") if dictionary.get("serviceName") else APIHelper.SKIP
        service_version = dictionary.get("serviceVersion") if dictionary.get("serviceVersion") else APIHelper.SKIP
        current_version = dictionary.get("currentVersion") if dictionary.get("currentVersion") else APIHelper.SKIP
        version = dictionary.get("version") if dictionary.get("version") else APIHelper.SKIP
        state = dictionary.get("state") if dictionary.get("state") else APIHelper.SKIP
        customer_id = dictionary.get("customerID") if dictionary.get("customerID") else APIHelper.SKIP
        created_by = dictionary.get("createdBy") if dictionary.get("createdBy") else APIHelper.SKIP
        created_at = dictionary.get("createdAt") if dictionary.get("createdAt") else APIHelper.SKIP
        last_updated_by = dictionary.get("lastUpdatedBy") if dictionary.get("lastUpdatedBy") else APIHelper.SKIP
        last_updated_at = dictionary.get("lastUpdatedAt") if dictionary.get("lastUpdatedAt") else APIHelper.SKIP
        linked_service_instances = None
        if dictionary.get('linkedServiceInstances') is not None:
            linked_service_instances = [LinkedServiceInstance.from_dictionary(x) for x in dictionary.get('linkedServiceInstances')]
        else:
            linked_service_instances = APIHelper.SKIP
        access_intents = AccessIntents.from_dictionary(dictionary.get('accessIntents')) if 'accessIntents' in dictionary.keys() else APIHelper.SKIP
        placement_intents = PlacementIntents.from_dictionary(dictionary.get('placementIntents')) if 'placementIntents' in dictionary.keys() else APIHelper.SKIP
        deployment_locations = None
        if dictionary.get('deploymentLocations') is not None:
            deployment_locations = [DeploymentLocation.from_dictionary(x) for x in dictionary.get('deploymentLocations')]
        else:
            deployment_locations = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   name,
                   service_name,
                   service_version,
                   current_version,
                   version,
                   state,
                   customer_id,
                   created_by,
                   created_at,
                   last_updated_by,
                   last_updated_at,
                   linked_service_instances,
                   access_intents,
                   placement_intents,
                   deployment_locations)
