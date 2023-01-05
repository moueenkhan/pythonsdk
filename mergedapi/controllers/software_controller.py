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
from mergedapi.models.software_package import SoftwarePackage
from mergedapi.exceptions.error_exception import ErrorException


class SoftwareController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(SoftwareController, self).__init__(config)

    def get_available_software_list(self,
                                    account,
                                    distribution_type=None):
        """Does a GET request to /software/{account}.

        This endpoint allows user to list a certain type of software of an
        account.

        Args:
            account (string): Account identifier
            distribution_type (string, optional): Filter distributionType to
                get specific type of software. Value is LWM2M, OMD-DM or HTTP

        Returns:
            list of SoftwarePackage: Response from the API. Return array of
                software.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT7)
            .path('/software/{account}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('distributionType')
                         .value(distribution_type))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SoftwarePackage.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()
