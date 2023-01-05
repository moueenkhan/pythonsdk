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
from mergedapi.models.get_all_service_res import GetAllServiceRes
from mergedapi.models.service import Service
from mergedapi.models.delete_response import DeleteResponse
from mergedapi.models.current_status import CurrentStatus
from mergedapi.exceptions.error_response_error_1_exception import ErrorResponseError1Exception


class ServiceOnboardingController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(ServiceOnboardingController, self).__init__(config)

    def get_services(self,
                     account_name,
                     correlation_id=None,
                     name=None,
                     q=None,
                     limit=None,
                     off_set=None,
                     sort_key=None,
                     sort_dir=None,
                     details_flag=True):
        """Does a GET request to /v1/services.

        Fetch all organizational services in the platform

        Args:
            account_name (string): User account name.
            correlation_id (string, optional): TODO: type description here.
            name (string, optional): Name of the service whose information
                needs to be fetched.
            q (string, optional): Use the comma (:) character to separate
                multiple values eg
                type=myService:workloads.packageType=Helm,YAML:state=DRAFTED,VA
                LIDATION_COMPLETED
            limit (long|int, optional): number of items to return
            off_set (long|int, optional): Id of the last respose value in the
                previous list
            sort_key (string, optional): Sorts the response by an attribute.
                Default is created_at
            sort_dir (SortDirectionEnum, optional): Sorts the response. Use
                asc for ascending or desc for descending order. The default is
                desc.
            details_flag (bool, optional): Default as true. If it is true then
                it will return all details.

        Returns:
            GetAllServiceRes: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT2)
            .path('/v1/services')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('q')
                         .value(q))
            .query_param(Parameter()
                         .key('limit')
                         .value(limit))
            .query_param(Parameter()
                         .key('offSet')
                         .value(off_set))
            .query_param(Parameter()
                         .key('sortKey')
                         .value(sort_key))
            .query_param(Parameter()
                         .key('sortDir')
                         .value(sort_dir))
            .query_param(Parameter()
                         .key('detailsFlag')
                         .value(details_flag))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetAllServiceRes.from_dictionary)
            .local_error('400', 'Bad Request', ErrorResponseError1Exception)
            .local_error('401', 'Unauthorized', ErrorResponseError1Exception)
            .local_error('404', 'Not found', ErrorResponseError1Exception)
            .local_error('500', 'Internal Server Error', ErrorResponseError1Exception)
        ).execute()

    def register_service(self,
                         account_name,
                         body,
                         correlation_id=None):
        """Does a POST request to /v1/services.

        Create a new service with in user's organization

        Args:
            account_name (string): User account name.
            body (Service): body
            correlation_id (string, optional): TODO: type description here.

        Returns:
            Service: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT2)
            .path('/v1/services')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Service.from_dictionary)
            .local_error('400', 'Bad Request', ErrorResponseError1Exception)
            .local_error('401', 'Unauthorized', ErrorResponseError1Exception)
            .local_error('403', 'Forbidden', ErrorResponseError1Exception)
            .local_error('404', 'Not found', ErrorResponseError1Exception)
            .local_error('415', 'Unsupported media type', ErrorResponseError1Exception)
            .local_error('429', 'Too many requests', ErrorResponseError1Exception)
            .local_error('500', 'Internal Server Error', ErrorResponseError1Exception)
        ).execute()

    def get_service_details(self,
                            account_name,
                            service_name,
                            version,
                            correlation_id=None):
        """Does a GET request to /v1/services/{serviceName}/{version}.

        Fetch a service details with in user's organization using service name
        and version

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service whose information needs
                to be fetched.
            version (string): Version of service whose information needs to be
                fetched.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            Service: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT2)
            .path('/v1/services/{serviceName}/{version}')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Service.from_dictionary)
            .local_error('400', 'Bad Request', ErrorResponseError1Exception)
            .local_error('401', 'Unauthorized', ErrorResponseError1Exception)
            .local_error('404', 'Not found', ErrorResponseError1Exception)
            .local_error('500', 'Internal Server Error', ErrorResponseError1Exception)
        ).execute()

    def remove_user_service(self,
                            account_name,
                            service_name,
                            version,
                            correlation_id=None):
        """Does a DELETE request to /v1/services/{serviceName}/{version}.

        Remove a service from user's organization

        Args:
            account_name (string): User account name.
            service_name (string): Name of the service which is about to be
                deleted.
            version (string): Version of the service which is about to be
                deleted.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            DeleteResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT2)
            .path('/v1/services/{serviceName}/{version}')
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('serviceName')
                            .value(service_name)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('version')
                            .value(version)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeleteResponse.from_dictionary)
            .local_error('401', 'Unauthorized', ErrorResponseError1Exception)
            .local_error('404', 'Not found', ErrorResponseError1Exception)
            .local_error('500', 'Internal Server Error', ErrorResponseError1Exception)
        ).execute()

    def check_job_status(self,
                         account_name,
                         job_id,
                         correlation_id=None):
        """Does a GET request to /v1/services/{jobId}/status.

        Check current status of job for a service using job ID

        Args:
            account_name (string): User account name.
            job_id (string): Auto Generated Id of the job.
            correlation_id (string, optional): TODO: type description here.

        Returns:
            CurrentStatus: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT2)
            .path('/v1/services/{jobId}/status')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('AccountName')
                          .value(account_name))
            .template_param(Parameter()
                            .key('jobId')
                            .value(job_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('correlationId')
                          .value(correlation_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CurrentStatus.from_dictionary)
            .local_error('401', 'Unauthorized', ErrorResponseError1Exception)
            .local_error('404', 'Not found', ErrorResponseError1Exception)
            .local_error('500', 'Internal Server Error', ErrorResponseError1Exception)
        ).execute()
