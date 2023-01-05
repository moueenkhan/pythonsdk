# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class ClusterInfraProvision(object):

    """Implementation of the 'ClusterInfraProvision' model.

    TODO: type model description here.

    Attributes:
        cluster_id (string): TODO: type description here.
        provision_id (string): TODO: type description here.
        created_at (string): TODO: type description here.
        modified_at (string): TODO: type description here.
        organization_id (string): TODO: type description here.
        partner_id (string): TODO: type description here.
        mtype (string): TODO: type description here.
        running_state (string): TODO: type description here.
        running_status (string): TODO: type description here.
        id (string): TODO: type description here.
        status (string): TODO: type description here.
        total_steps (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "cluster_id": 'cluster_id',
        "provision_id": 'provision_id',
        "created_at": 'created_at',
        "modified_at": 'modified_at',
        "organization_id": 'organization_id',
        "partner_id": 'partner_id',
        "mtype": 'type',
        "running_state": 'running_state',
        "running_status": 'running_status',
        "id": 'id',
        "status": 'status',
        "total_steps": 'total_steps'
    }

    _optionals = [
        'cluster_id',
        'provision_id',
        'created_at',
        'modified_at',
        'organization_id',
        'partner_id',
        'mtype',
        'running_state',
        'running_status',
        'id',
        'status',
        'total_steps',
    ]

    def __init__(self,
                 cluster_id=APIHelper.SKIP,
                 provision_id=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 modified_at=APIHelper.SKIP,
                 organization_id=APIHelper.SKIP,
                 partner_id=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 running_state=APIHelper.SKIP,
                 running_status=APIHelper.SKIP,
                 id=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 total_steps=APIHelper.SKIP):
        """Constructor for the ClusterInfraProvision class"""

        # Initialize members of the class
        if cluster_id is not APIHelper.SKIP:
            self.cluster_id = cluster_id 
        if provision_id is not APIHelper.SKIP:
            self.provision_id = provision_id 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if modified_at is not APIHelper.SKIP:
            self.modified_at = modified_at 
        if organization_id is not APIHelper.SKIP:
            self.organization_id = organization_id 
        if partner_id is not APIHelper.SKIP:
            self.partner_id = partner_id 
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if running_state is not APIHelper.SKIP:
            self.running_state = running_state 
        if running_status is not APIHelper.SKIP:
            self.running_status = running_status 
        if id is not APIHelper.SKIP:
            self.id = id 
        if status is not APIHelper.SKIP:
            self.status = status 
        if total_steps is not APIHelper.SKIP:
            self.total_steps = total_steps 

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

        cluster_id = dictionary.get("cluster_id") if dictionary.get("cluster_id") else APIHelper.SKIP
        provision_id = dictionary.get("provision_id") if dictionary.get("provision_id") else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        modified_at = dictionary.get("modified_at") if dictionary.get("modified_at") else APIHelper.SKIP
        organization_id = dictionary.get("organization_id") if dictionary.get("organization_id") else APIHelper.SKIP
        partner_id = dictionary.get("partner_id") if dictionary.get("partner_id") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        running_state = dictionary.get("running_state") if dictionary.get("running_state") else APIHelper.SKIP
        running_status = dictionary.get("running_status") if dictionary.get("running_status") else APIHelper.SKIP
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        total_steps = dictionary.get("total_steps") if dictionary.get("total_steps") else APIHelper.SKIP
        # Return an object of this model
        return cls(cluster_id,
                   provision_id,
                   created_at,
                   modified_at,
                   organization_id,
                   partner_id,
                   mtype,
                   running_state,
                   running_status,
                   id,
                   status,
                   total_steps)
