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
from mergedapi.models.performance_api_response import PerformanceApiResponse
from mergedapi.exceptions.error_response_error_exception import ErrorResponseErrorException


class M5gMECPerformanceAPIController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(M5gMECPerformanceAPIController, self).__init__(config)

    def get_mecplatforms_using_post(self,
                                    body=None):
        """Does a POST request to /performance/device/network/metrics.

        Query the most recent data for Key Performance Indicators (KPIs) like
        network availability, MEC hostnames and more.

        Args:
            body (PerformanceApiRequest, optional): TODO: type description
                here.

        Returns:
            PerformanceApiResponse: Response from the API. The most recent
                data for different KPIs

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT1)
            .path('/performance/device/network/metrics')
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
            .deserialize_into(PerformanceApiResponse.from_dictionary)
            .local_error('400', 'Bad Request', ErrorResponseErrorException)
            .local_error('401', 'Unauthorized', ErrorResponseErrorException)
            .local_error('403', 'Forbidden', ErrorResponseErrorException)
            .local_error('404', 'Resource Not Found', ErrorResponseErrorException)
            .local_error('405', 'Method Not Allowed', ErrorResponseErrorException)
            .local_error('503', 'Service Unavailable', ErrorResponseErrorException)
        ).execute()
