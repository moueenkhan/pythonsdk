# -*- coding: utf-8 -*-

"""
mergedapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from deprecation import deprecated
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
from mergedapi.models.get_cancel_list import GetCancelList
from mergedapi.models.create_cancel_list_response import CreateCancelListResponse
from mergedapi.models.success_response_1 import SuccessResponse1
from mergedapi.exceptions.error_exception import ErrorException


class LicenseCancellationCandidateDevicesListController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(LicenseCancellationCandidateDevicesListController, self).__init__(config)

    @deprecated()
    def get_license_cancellation_candidate_devices_list(self,
                                                        account,
                                                        start_index=None):
        """Does a GET request to /licenses/{account}/cancel.

        The license cancel endpoint allows user to list registered license
        cancellation candidate devices.

        Args:
            account (string): Account identifier
            start_index (string, optional): Start index to retrieve

        Returns:
            GetCancelList: Response from the API. A list of license
                cancellation candidate devices

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT7)
            .path('/licenses/{account}/cancel')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('startIndex')
                         .value(start_index))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetCancelList.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    @deprecated()
    def create_license_cancellation_candidate_devices_list(self,
                                                           account,
                                                           body):
        """Does a POST request to /licenses/{account}/cancel.

        The license cancel endpoint allows user to create a list of license
        cancellation candidate devices.

        Args:
            account (string): Account identifier
            body (CreateCancelList): license cancellation candidate devices

        Returns:
            CreateCancelListResponse: Response from the API. Return a created
                license cancellation device list.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT7)
            .path('/licenses/{account}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
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
            .deserialize_into(CreateCancelListResponse.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    @deprecated()
    def delete_candidate_devices_list(self,
                                      account):
        """Does a DELETE request to /licenses/{account}/cancel.

        This endpoint allows user to delete a created cancel candidate device
        list.

        Args:
            account (string): Account identifier

        Returns:
            SuccessResponse1: Response from the API. Return delete result.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT7)
            .path('/licenses/{account}/cancel')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SuccessResponse1.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()
