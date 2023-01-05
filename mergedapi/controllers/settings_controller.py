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
from mergedapi.models.setting import Setting
from mergedapi.models.request_response_1 import RequestResponse1
from mergedapi.models.setings_response import SetingsResponse
from mergedapi.exceptions.error_exception import ErrorException
from mergedapi.exceptions.rest_error_response_error_1_exception import RestErrorResponseError1Exception


class SettingsController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(SettingsController, self).__init__(config)

    def get_diagnostics_settings(self,
                                 account_name,
                                 devices):
        """Does a GET request to /devices/settings.

        This endpoint retrieves diagnostics settings synchronously

        Args:
            account_name (string): Account identifier
            devices (string): Devices list format:
                [{"id":"{imei1}","kind":"imei"},{"id":"{imei2}","kind":"imei"}]
                
        Returns:
            list of Setting: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT4)
            .path('/devices/settings')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('accountName')
                         .value(account_name))
            .query_param(Parameter()
                         .key('devices')
                         .value(devices))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Setting.from_dictionary)
        ).execute()

    def set_anomaly_settings(self,
                             body):
        """Does a POST request to /v1/intelligence/anomaly/settings.

        Uses the subscribed account ID to activate Anomaly Detection and set
        threshold values.

        Args:
            body (SetAnomalyRequest): Settings Request

        Returns:
            RequestResponse1: Response from the API. Status of Request

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT11)
            .path('/v1/intelligence/anomaly/settings')
            .http_method(HttpMethodEnum.POST)
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
            .deserialize_into(RequestResponse1.from_dictionary)
        ).execute()

    def get_anomaly_settings(self,
                             account_name):
        """Does a GET request to /v1/intelligence/{accountName}/anomaly/settings.

        Retrieves the current Anomnaly Detection settings for an account.

        Args:
            account_name (string): The name of the subscribed account

        Returns:
            SetingsResponse: Response from the API. Retrieve the Settings for
                Anomaly Detection.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT11)
            .path('/v1/intelligence/{accountName}/anomaly/settings')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('accountName')
                            .value(account_name)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SetingsResponse.from_dictionary)
        ).execute()

    def reset_anomaly_settings(self,
                               account_name):
        """Does a PUT request to /v1/intelligence/{accountName}/anomaly/settings/reset.

        Resets the thresholds to Zero.

        Args:
            account_name (string): The name of the subscribed account

        Returns:
            RequestResponse1: Response from the API. Status of Request

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT11)
            .path('/v1/intelligence/{accountName}/anomaly/settings/reset')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('accountName')
                            .value(account_name)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(RequestResponse1.from_dictionary)
        ).execute()
