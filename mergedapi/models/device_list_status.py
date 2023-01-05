# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from mergedapi.api_helper import APIHelper
from mergedapi.models.software_info import SoftwareInfo


class DeviceListStatus(object):

    """Implementation of the 'DeviceListStatus' model.

    Device information

    Attributes:
        device_id (string): Device IMEI
        request_status (string): Success or failure
        result_reason (string): Result reason
        mdn (string): MDN
        model (string): Device model
        make (string): Device make
        firmware (string): Device firmware version
        fota_eligible (string): Device fota capable LWM2M, OMD-DM, HTTP or
            NONE
        status (string): Device status
        license_assigned (bool): License assigned device
        protocol (DevicesProtocolEnum): Firmware protocol. Valid values
            include: LWM2M, OMADM, HTTP.
        software_list (list of SoftwareInfo): List of sofware
        file_list (list of SoftwareInfo): List of files
        create_time (datetime): The date and time of when the device is
            created
        status_time (datetime): The date and time of when the device firmware
            or software is updated
        update_time (datetime): The date and time of when the device is
            updated
        refresh_time (datetime): The date and time of when the device is
            refreshed
        last_connection_time (datetime): The date and time of when the device
            reachability is checked

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_id": 'deviceId',
        "request_status": 'requestStatus',
        "result_reason": 'resultReason',
        "mdn": 'mdn',
        "model": 'model',
        "make": 'make',
        "firmware": 'firmware',
        "fota_eligible": 'fotaEligible',
        "status": 'status',
        "license_assigned": 'licenseAssigned',
        "protocol": 'protocol',
        "software_list": 'softwareList',
        "file_list": 'fileList',
        "create_time": 'createTime',
        "status_time": 'statusTime',
        "update_time": 'updateTime',
        "refresh_time": 'refreshTime',
        "last_connection_time": 'lastConnectionTime'
    }

    _optionals = [
        'request_status',
        'result_reason',
        'mdn',
        'model',
        'make',
        'firmware',
        'fota_eligible',
        'status',
        'license_assigned',
        'protocol',
        'software_list',
        'file_list',
        'create_time',
        'status_time',
        'update_time',
        'refresh_time',
        'last_connection_time',
    ]

    def __init__(self,
                 device_id=None,
                 request_status=APIHelper.SKIP,
                 result_reason=APIHelper.SKIP,
                 mdn=APIHelper.SKIP,
                 model=APIHelper.SKIP,
                 make=APIHelper.SKIP,
                 firmware=APIHelper.SKIP,
                 fota_eligible=APIHelper.SKIP,
                 status=APIHelper.SKIP,
                 license_assigned=APIHelper.SKIP,
                 protocol='LWM2M',
                 software_list=APIHelper.SKIP,
                 file_list=APIHelper.SKIP,
                 create_time=APIHelper.SKIP,
                 status_time=APIHelper.SKIP,
                 update_time=APIHelper.SKIP,
                 refresh_time=APIHelper.SKIP,
                 last_connection_time=APIHelper.SKIP):
        """Constructor for the DeviceListStatus class"""

        # Initialize members of the class
        self.device_id = device_id 
        if request_status is not APIHelper.SKIP:
            self.request_status = request_status 
        if result_reason is not APIHelper.SKIP:
            self.result_reason = result_reason 
        if mdn is not APIHelper.SKIP:
            self.mdn = mdn 
        if model is not APIHelper.SKIP:
            self.model = model 
        if make is not APIHelper.SKIP:
            self.make = make 
        if firmware is not APIHelper.SKIP:
            self.firmware = firmware 
        if fota_eligible is not APIHelper.SKIP:
            self.fota_eligible = fota_eligible 
        if status is not APIHelper.SKIP:
            self.status = status 
        if license_assigned is not APIHelper.SKIP:
            self.license_assigned = license_assigned 
        self.protocol = protocol 
        if software_list is not APIHelper.SKIP:
            self.software_list = software_list 
        if file_list is not APIHelper.SKIP:
            self.file_list = file_list 
        if create_time is not APIHelper.SKIP:
            self.create_time = APIHelper.RFC3339DateTime(create_time) if create_time else None 
        if status_time is not APIHelper.SKIP:
            self.status_time = APIHelper.RFC3339DateTime(status_time) if status_time else None 
        if update_time is not APIHelper.SKIP:
            self.update_time = APIHelper.RFC3339DateTime(update_time) if update_time else None 
        if refresh_time is not APIHelper.SKIP:
            self.refresh_time = APIHelper.RFC3339DateTime(refresh_time) if refresh_time else None 
        if last_connection_time is not APIHelper.SKIP:
            self.last_connection_time = APIHelper.RFC3339DateTime(last_connection_time) if last_connection_time else None 

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

        device_id = dictionary.get("deviceId") if dictionary.get("deviceId") else None
        request_status = dictionary.get("requestStatus") if dictionary.get("requestStatus") else APIHelper.SKIP
        result_reason = dictionary.get("resultReason") if dictionary.get("resultReason") else APIHelper.SKIP
        mdn = dictionary.get("mdn") if dictionary.get("mdn") else APIHelper.SKIP
        model = dictionary.get("model") if dictionary.get("model") else APIHelper.SKIP
        make = dictionary.get("make") if dictionary.get("make") else APIHelper.SKIP
        firmware = dictionary.get("firmware") if dictionary.get("firmware") else APIHelper.SKIP
        fota_eligible = dictionary.get("fotaEligible") if dictionary.get("fotaEligible") else APIHelper.SKIP
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        license_assigned = dictionary.get("licenseAssigned") if "licenseAssigned" in dictionary.keys() else APIHelper.SKIP
        protocol = dictionary.get("protocol") if dictionary.get("protocol") else 'LWM2M'
        software_list = None
        if dictionary.get('softwareList') is not None:
            software_list = [SoftwareInfo.from_dictionary(x) for x in dictionary.get('softwareList')]
        else:
            software_list = APIHelper.SKIP
        file_list = None
        if dictionary.get('fileList') is not None:
            file_list = [SoftwareInfo.from_dictionary(x) for x in dictionary.get('fileList')]
        else:
            file_list = APIHelper.SKIP
        create_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("createTime")).datetime if dictionary.get("createTime") else APIHelper.SKIP
        status_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("statusTime")).datetime if dictionary.get("statusTime") else APIHelper.SKIP
        update_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("updateTime")).datetime if dictionary.get("updateTime") else APIHelper.SKIP
        refresh_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("refreshTime")).datetime if dictionary.get("refreshTime") else APIHelper.SKIP
        last_connection_time = APIHelper.RFC3339DateTime.from_value(dictionary.get("lastConnectionTime")).datetime if dictionary.get("lastConnectionTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(device_id,
                   request_status,
                   result_reason,
                   mdn,
                   model,
                   make,
                   firmware,
                   fota_eligible,
                   status,
                   license_assigned,
                   protocol,
                   software_list,
                   file_list,
                   create_time,
                   status_time,
                   update_time,
                   refresh_time,
                   last_connection_time)
