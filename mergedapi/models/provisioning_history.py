# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.kv_pair import KvPair


class ProvisioningHistory(object):

    """Implementation of the 'ProvisioningHistory' model.

    The provisioning history of a specified device during a specified time
    period.

    Attributes:
        occurred_at (string): The date and time when the provisioning event
            occured.
        status (string): The success or failure of the provisioning event.
        event_by (string): The user who performed the provisioning event.
        event_type (string): The provisioning
            action:Activate,Suspend,Restore,Deactivate,Device Move
        mdn (string): The MDN assigned to the device after the provisioning
            event.
        msisdn (string): The MSISDN assigned to the device after the
            provisioning event.
        service_plan (string): The service plan of the device after the
            provisioning event occurred.
        extended_attributes (list of KvPair): Any extended attributes for the
            event, as Key and Value pairs.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "occurred_at": 'occurredAt',
        "status": 'status',
        "event_by": 'eventBy',
        "event_type": 'eventType',
        "mdn": 'mdn',
        "msisdn": 'msisdn',
        "service_plan": 'servicePlan',
        "extended_attributes": 'extendedAttributes'
    }

    _optionals = [
        'occurred_at',
        'status',
        'event_by',
        'event_type',
        'mdn',
        'msisdn',
        'service_plan',
        'extended_attributes',
    ]

    def __init__(self,
                 occurred_at=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 event_by=APIHelper.SKIP,
                 event_type=APIHelper.SKIP,
                 mdn=APIHelper.SKIP,
                 msisdn=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 extended_attributes=APIHelper.SKIP):
        """Constructor for the ProvisioningHistory class"""

        # Initialize members of the class
        if occurred_at is not APIHelper.SKIP:
            self.occurred_at = occurred_at 
        if status is not APIHelper.SKIP:
            self.status = status 
        if event_by is not APIHelper.SKIP:
            self.event_by = event_by 
        if event_type is not APIHelper.SKIP:
            self.event_type = event_type 
        if mdn is not APIHelper.SKIP:
            self.mdn = mdn 
        if msisdn is not APIHelper.SKIP:
            self.msisdn = msisdn 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if extended_attributes is not APIHelper.SKIP:
            self.extended_attributes = extended_attributes 

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

        occurred_at = dictionary.get("occurredAt") if dictionary.get("occurredAt") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        event_by = dictionary.get("eventBy") if dictionary.get("eventBy") else APIHelper.SKIP
        event_type = dictionary.get("eventType") if dictionary.get("eventType") else APIHelper.SKIP
        mdn = dictionary.get("mdn") if dictionary.get("mdn") else APIHelper.SKIP
        msisdn = dictionary.get("msisdn") if dictionary.get("msisdn") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        extended_attributes = None
        if dictionary.get('extendedAttributes') is not None:
            extended_attributes = [KvPair.from_dictionary(x) for x in dictionary.get('extendedAttributes')]
        else:
            extended_attributes = APIHelper.SKIP
        # Return an object of this model
        return cls(occurred_at,
                   status,
                   event_by,
                   event_type,
                   mdn,
                   msisdn,
                   service_plan,
                   extended_attributes)
