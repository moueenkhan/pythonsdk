# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from mergedapi.api_helper import APIHelper
from mergedapi.configuration import Server
from mergedapi.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from mergedapi.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from mergedapi.models.firmware_package import FirmwarePackage
from mergedapi.models.device_firmware_list import DeviceFirmwareList
from mergedapi.models.update_device_firmware_version_resp import UpdateDeviceFirmwareVersionResp
from mergedapi.exceptions.error_exception import ErrorException


class FirmwareController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(FirmwareController, self).__init__(config)

    def list_of_available_firmware(self,
                                   acc,
                                   protocol):
        """Does a GET request to /firmware/{acc}.

        This endpoint allows user to list the firmware of an account

        Args:
            acc (string): Account identifier
            protocol (FirmwareProtocolEnum): Filter to retrieve a specific
                protocol type used

        Returns:
            list of FirmwarePackage: Response from the API. Returns an array
                of firmware objects.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT8)
            .path('/firmware/{acc}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('protocol')
                         .value(protocol))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FirmwarePackage.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def synchronize_device_firmware(self,
                                    acc,
                                    body):
        """Does a PUT request to /firmware/{acc}/devices.

        Synchronize ThingSpace with the FOTA server for up to 100 devices

        Args:
            acc (string): Account identifier
            body (LicensesAssignedRemovedRequest): DeviceIds to get firmware
                info synchronously

        Returns:
            DeviceFirmwareList: Response from the API. Returns Device Firmware
                Information

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT8)
            .path('/firmware/{acc}/devices')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceFirmwareList.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def report_device_firmware(self,
                               acc,
                               device_id):
        """Does a PUT request to /firmware/{acc}/async/{deviceId}.

        Ask a device to report its firmware version asynchronously

        Args:
            acc (string): Account identifier
            device_id (string): Device identifier

        Returns:
            UpdateDeviceFirmwareVersionResp: Response from the API. Device
                firmware version update request

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT8)
            .path('/firmware/{acc}/async/{deviceId}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('deviceId')
                            .value(device_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UpdateDeviceFirmwareVersionResp.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()
