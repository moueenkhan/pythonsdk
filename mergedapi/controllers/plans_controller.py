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
from mergedapi.models.service_plan_response import ServicePlanResponse
from mergedapi.exceptions.rest_error_response_exception import RestErrorResponseException


class PlansController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(PlansController, self).__init__(config)

    def get_service_plan_list_using_get(self,
                                        aname):
        """Does a GET request to /plans/{aname}.

        Returns a list of all data service plans that are associated with a
        specified billing account. When you send a request to
        /devices/actions/activate to activate a line of service you must
        specify the code for one of the service plans associated with your
        account.

        Args:
            aname (string): Account name

        Returns:
            list of ServicePlanResponse: Response from the API. The list of
                service plans associated with the account.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT9)
            .path('/plans/{aname}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('aname')
                            .value(aname)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ServicePlanResponse.from_dictionary)
            .local_error('400', 'Error Response', RestErrorResponseException)
        ).execute()
