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
from mergedapi.models.get_service_endpoints_response import GetServiceEndpointsResponse
from mergedapi.exceptions.types_error_exception import TypesErrorException


class ServiceEndpointDiscoveryController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(ServiceEndpointDiscoveryController, self).__init__(config)

    def get_service_endpoints(self,
                              region=None,
                              subscriber_density=None,
                              ue_identity_type=None,
                              ue_identity=None,
                              service_endpoints_ids=None):
        """Does a GET request to /serviceendpoints.

        Returns a list of optimal Service Endpoints that client devices can
        connect to. **Note:** If a query is sent with all of the parameters,
        it will fail with a "400" error. You can search based on the following
        parameter combinations - Region plus Service Endpoints IDs and
        Subscriber density (density is optional but recommended), Region plus
        Service Endpoints IDs and UEIdentity(Including UEIdentity Type) and
        Service Endpoints IDs plus UEIdentity(Including UEIdentity Type).

        Args:
            region (string, optional): MEC region name. Current valid values
                are US_WEST_2 and US_EAST_1.
            subscriber_density (int, optional): Minimum number of 4G/5G
                subscribers per square kilometer.
            ue_identity_type (TypesUEIdentityTypeEnum, optional): Type of User
                Equipment identifier used in `UEIdentity`.
            ue_identity (string, optional): The identifier value for User
                Equipment. The type of identifier is defined by the
                'UEIdentityType' parameter. The`IPAddress`format can be IPv4
                or IPv6.
            service_endpoints_ids (string, optional): A system-defined string
                identifier representing one or more registered Service
                Endpoints.

        Returns:
            GetServiceEndpointsResponse: Response from the API. An array of
                optimal Service Endpoint IDs for clients to connect to

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/serviceendpoints')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('region')
                         .value(region))
            .query_param(Parameter()
                         .key('subscriberDensity')
                         .value(subscriber_density))
            .query_param(Parameter()
                         .key('UEIdentityType')
                         .value(ue_identity_type))
            .query_param(Parameter()
                         .key('UEIdentity')
                         .value(ue_identity))
            .query_param(Parameter()
                         .key('serviceEndpointsIds')
                         .value(service_endpoints_ids))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetServiceEndpointsResponse.from_dictionary)
            .local_error('400', 'HTTP 400 Bad Request', TypesErrorException)
            .local_error('401', 'HTTP 401 Unauthorized', TypesErrorException)
        ).execute()
