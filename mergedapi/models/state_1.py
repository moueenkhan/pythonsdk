# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper


class State1(object):

    """Implementation of the 'State1' model.

    Each service includes custom states.

    Attributes:
        name (string): The name of the state.
        workflow_sequence_number (float): The workflow sequence number of this
            state.
        service_plans (list of string): The service plans that can be used to
            charge for services for devices in this state.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "workflow_sequence_number": 'workflowSequenceNumber',
        "service_plans": 'servicePlans'
    }

    _optionals = [
        'name',
        'workflow_sequence_number',
        'service_plans',
    ]

    def __init__(self,
                 name=APIHelper.SKIP,
                 workflow_sequence_number=APIHelper.SKIP,
                 service_plans=APIHelper.SKIP):
        """Constructor for the State1 class"""

        # Initialize members of the class
        if name is not APIHelper.SKIP:
            self.name = name 
        if workflow_sequence_number is not APIHelper.SKIP:
            self.workflow_sequence_number = workflow_sequence_number 
        if service_plans is not APIHelper.SKIP:
            self.service_plans = service_plans 

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

        name = dictionary.get("name") if dictionary.get("name") else APIHelper.SKIP
        workflow_sequence_number = dictionary.get("workflowSequenceNumber") if dictionary.get("workflowSequenceNumber") else APIHelper.SKIP
        service_plans = dictionary.get("servicePlans") if dictionary.get("servicePlans") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   workflow_sequence_number,
                   service_plans)
