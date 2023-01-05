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
from mergedapi.models.device_list_query_response import DeviceListQueryResponse
from mergedapi.models.upgrade_list_query_response import UpgradeListQueryResponse
from mergedapi.models.device_upgrade_history_query_response_item import DeviceUpgradeHistoryQueryResponseItem
from mergedapi.models.device_software_upgrade import DeviceSoftwareUpgrade
from mergedapi.models.campaign_history import CampaignHistory
from mergedapi.models.campaign_device import CampaignDevice
from mergedapi.models.campaign_history_1 import CampaignHistory1
from mergedapi.models.device_firmware_upgrade import DeviceFirmwareUpgrade
from mergedapi.models.campaign_device_1 import CampaignDevice1
from mergedapi.models.total_level import TotalLevel
from mergedapi.models.callback_response import CallbackResponse
from mergedapi.models.session_level import SessionLevel
from mergedapi.exceptions.error_exception import ErrorException
from mergedapi.exceptions.error_response_error_2_exception import ErrorResponseError2Exception


class ReportsController(BaseController):

    """A Controller to access Endpoints in the mergedapi API."""
    def __init__(self, config):
        super(ReportsController, self).__init__(config)

    def device_query_using_get(self,
                               account,
                               start_index):
        """Does a GET request to /devices/{account}/index/{startIndex}.

        Returns an array of all devices in the specified account. Each device
        object includes information needed for managing firmware, including
        the device make and model, MDN and IMEI, and current firmware
        version.

        Args:
            account (string): Account identifier in "##########-#####"
            start_index (string): Only return devices with IMEIs larger than
                this value. Use 0 for the first request. If `hasMoreData`=true
                in the response, use the `lastSeenDeviceId` value from the
                response as the startIndex in the next request.

        Returns:
            DeviceListQueryResponse: Response from the API. Device list

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT6)
            .path('/devices/{account}/index/{startIndex}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('startIndex')
                            .value(start_index)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeviceListQueryResponse.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def firmware_status_upgrade_request_using_get(self,
                                                  account,
                                                  upgrade_status,
                                                  start_index):
        """Does a GET request to /reports/{account}/status/{upgradeStatus}/index/{startIndex}.

        Returns a list of all upgrades with a specified status.

        Args:
            account (string): Account identifier in "##########-#####"
            upgrade_status (UpgradeStatusEnumListEnum): The status of the
                upgrades that you want to retrieve.
            start_index (string): The zero-based number of the first record to
                return. Set startIndex=0 for the first request. If
                `hasMoreFlag`=true in the response, use the
                `lastSeenUpgradeId` value from the response as the startIndex
                in the next request.

        Returns:
            UpgradeListQueryResponse: Response from the API. Upgrade
                information

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT6)
            .path('/reports/{account}/status/{upgradeStatus}/index/{startIndex}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('upgradeStatus')
                            .value(upgrade_status)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('startIndex')
                            .value(start_index)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(UpgradeListQueryResponse.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def device_upgrade_history_request_using_get(self,
                                                 account,
                                                 device_id):
        """Does a GET request to /reports/{account}/devices/{deviceId}.

        Returns the upgrade history of the specified device from the previous
        six months.

        Args:
            account (string): Account identifier in "##########-#####"
            device_id (string): The IMEI of the device.

        Returns:
            list of DeviceUpgradeHistoryQueryResponseItem: Response from the
                API. Device upgrade history

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT6)
            .path('/reports/{account}/devices/{deviceId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
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
            .deserialize_into(DeviceUpgradeHistoryQueryResponseItem.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def get_device_software_upgrade_history(self,
                                            account,
                                            device_id):
        """Does a GET request to /reports/{account}/devices/{deviceId}.

        The endpoint allows user to get software upgrade history of a device
        based on device IMEI.

        Args:
            account (string): Account identifier
            device_id (string): Device IMEI identifier

        Returns:
            list of DeviceSoftwareUpgrade: Response from the API. Return array
                of upgrades.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT7)
            .path('/reports/{account}/devices/{deviceId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
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
            .deserialize_into(DeviceSoftwareUpgrade.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def get_campaign_history_for_status(self,
                                        account,
                                        campaign_status,
                                        last_seen_campaign_id=None):
        """Does a GET request to /reports/{account}/campaigns.

        The report endpoint allows user to get campaign history of an account
        for specified status.

        Args:
            account (string): Account identifier
            campaign_status (string): Campaign status
            last_seen_campaign_id (string, optional): Last seen campaign Id

        Returns:
            CampaignHistory: Response from the API. Return array of campaign
                history.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT7)
            .path('/reports/{account}/campaigns')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('campaignStatus')
                         .value(campaign_status))
            .query_param(Parameter()
                         .key('lastSeenCampaignId')
                         .value(last_seen_campaign_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CampaignHistory.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def get_campaign_device_status(self,
                                   account,
                                   campaign_id,
                                   last_seen_device_id=None):
        """Does a GET request to /reports/{account}/campaigns/{campaignId}/devices.

        The report endpoint allows user to get the full list of device of a
        campaign.

        Args:
            account (string): Account identifier
            campaign_id (string): Campaign identifier
            last_seen_device_id (string, optional): Last seen device
                identifier

        Returns:
            CampaignDevice: Response from the API. Return array of campaign
                history.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT7)
            .path('/reports/{account}/campaigns/{campaignId}/devices')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('campaignId')
                            .value(campaign_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('lastSeenDeviceId')
                         .value(last_seen_device_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CampaignDevice.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def get_firmware_campaign_status(self,
                                     acc,
                                     campaign_status,
                                     last_seen_campaign_id=None):
        """Does a GET request to /reports/{acc}/firmware/campaigns.

        Retrieve a list of campaigns for an account that have a specified
        campaign status

        Args:
            acc (string): Account identifier
            campaign_status (string): Campaign status
            last_seen_campaign_id (string, optional): Last seen campaign Id

        Returns:
            CampaignHistory1: Response from the API. Return array of campaign
                history

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT8)
            .path('/reports/{acc}/firmware/campaigns')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('campaignStatus')
                         .value(campaign_status))
            .query_param(Parameter()
                         .key('lastSeenCampaignId')
                         .value(last_seen_campaign_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CampaignHistory1.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def get_device_campaign_history(self,
                                    acc,
                                    device_id):
        """Does a GET request to /reports/{acc}/devices/{deviceId}.

        Retrieve campaign history for a specific device

        Args:
            acc (string): Account identifier
            device_id (string): Device IMEI identifier

        Returns:
            list of DeviceFirmwareUpgrade: Response from the API. Returns an
                array of firmware upgrades

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT8)
            .path('/reports/{acc}/devices/{deviceId}')
            .http_method(HttpMethodEnum.GET)
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
            .deserialize_into(DeviceFirmwareUpgrade.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def get_a_campaign_device_status(self,
                                     acc,
                                     campaign_id,
                                     last_seen_device_id=None):
        """Does a GET request to /reports/{acc}/campaigns/{campaignId}/devices.

        Retrieve a list of all devices in a campaign and the status of each
        device

        Args:
            acc (string): Account identifier
            campaign_id (string): Campaign identifier
            last_seen_device_id (string, optional): Last seen device
                identifier

        Returns:
            CampaignDevice1: Response from the API. Returns an array of
                campaign history

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT8)
            .path('/reports/{acc}/campaigns/{campaignId}/devices')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('acc')
                            .value(acc)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('campaignId')
                            .value(campaign_id)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('lastSeenDeviceId')
                         .value(last_seen_device_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CampaignDevice1.from_dictionary)
            .local_error('400', 'Unexpected error', ErrorException)
        ).execute()

    def report_aggregate_post(self,
                              account_number,
                              imei,
                              start_date=None,
                              end_date=None,
                              device_group=None,
                              data_plan=None,
                              no_session_flag=None,
                              body=None):
        """Does a POST request to /report/aggregate.

        Calculate aggregated report per day with number of sessions and usage
        information. User will receive synchronous response for specified list
        of devices (Max 10) and date range (Max 180 days).

        Args:
            account_number (string): The unique identifier for the account
            imei (string): Number of devices returning usage info. Could be 0,
                1 or more. If 0 the query will return all devices belonging to
                customer.
            start_date (string, optional): Start date of session to include.
                If not specified information will be shown from the earliest
                available (180 days). ISO 8601 format.
            end_date (string, optional): End date of session to include. If
                not specified information will be shown to the latest
                available. ISO 8601 format.
            device_group (string, optional): User defined group name the
                devices are a member of.
            data_plan (string, optional): The data plan the devices beign
                queried belong to.
            no_session_flag (string, optional): filters on devices which
                return only "no sessions".
            body (AggregateSessionReportRequest, optional): Aggregated report
                request example

        Returns:
            TotalLevel: Response from the API. A successful response shows
                session and usage details for up to 10 devices.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/report/aggregate')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('accountNumber')
                          .value(account_number))
            .header_param(Parameter()
                          .key('imei')
                          .value(imei))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('startDate')
                          .value(start_date))
            .header_param(Parameter()
                          .key('endDate')
                          .value(end_date))
            .header_param(Parameter()
                          .key('deviceGroup')
                          .value(device_group))
            .header_param(Parameter()
                          .key('dataPlan')
                          .value(data_plan))
            .header_param(Parameter()
                          .key('noSessionFlag')
                          .value(no_session_flag))
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
            .deserialize_into(TotalLevel.from_dictionary)
            .local_error('400', 'Bad request.', ErrorResponseError2Exception)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', ErrorResponseError2Exception)
            .local_error('403', 'Forbidden request.', ErrorResponseError2Exception)
            .local_error('404', 'Bad request. Not found.', ErrorResponseError2Exception)
            .local_error('409', 'Bad request. Conflict state.', ErrorResponseError2Exception)
            .local_error('500', 'Internal Server Error.', ErrorResponseError2Exception)
        ).execute()

    def report_aggregate_post_async(self,
                                    x_portal_initiated,
                                    account_number,
                                    imei,
                                    start_date=None,
                                    end_date=None,
                                    device_group=None,
                                    data_plan=None,
                                    no_session_flag=None,
                                    body=None):
        """Does a POST request to /report/async/aggregate.

        Calculate aggregated report per day with number of sessions and usage
        information. User will receive an asynchronous callback for the
        specified list of devices (Max 10000) and date range (Max 180 days).

        Args:
            x_portal_initiated (bool): A flag for using a listener. Set to
                true or false.
            account_number (string): The unique identifier for the account
            imei (string): Number of devices returning usage info. Could be 0,
                1 or more. If 0 the query will return all devices belonging to
                customer.
            start_date (string, optional): Start date of session to include.
                If not specified information will be shown from the earliest
                available (180 days). ISO 8601 format.
            end_date (string, optional): End date of session to include. If
                not specified information will be shown to the latest
                available. ISO 8601 format.
            device_group (string, optional): User defined group name the
                devices are a member of.
            data_plan (string, optional): The data plan the devices beign
                queried belong to.
            no_session_flag (string, optional): filters on devices which
                return only "no sessions".
            body (AggregateSessionReportRequest, optional): Aggregated report
                request example

        Returns:
            CallbackResponse: Response from the API. A successful response
                shows the request is queued with a unique `txid` to identify
                the report data with.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/report/async/aggregate')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('X-Portal-Initiated')
                          .value(x_portal_initiated))
            .header_param(Parameter()
                          .key('accountNumber')
                          .value(account_number))
            .header_param(Parameter()
                          .key('imei')
                          .value(imei))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('startDate')
                          .value(start_date))
            .header_param(Parameter()
                          .key('endDate')
                          .value(end_date))
            .header_param(Parameter()
                          .key('deviceGroup')
                          .value(device_group))
            .header_param(Parameter()
                          .key('dataPlan')
                          .value(data_plan))
            .header_param(Parameter()
                          .key('noSessionFlag')
                          .value(no_session_flag))
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
            .deserialize_into(CallbackResponse.from_dictionary)
            .local_error('400', 'Bad request.', ErrorResponseError2Exception)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', ErrorResponseError2Exception)
            .local_error('403', 'Forbidden request.', ErrorResponseError2Exception)
            .local_error('404', 'Bad request. Not found.', ErrorResponseError2Exception)
            .local_error('409', 'Bad request. Conflict state.', ErrorResponseError2Exception)
            .local_error('500', 'Internal Server Error.', ErrorResponseError2Exception)
        ).execute()

    def report_session_post(self,
                            account_number,
                            imei,
                            start_date=None,
                            end_date=None,
                            duration_low=None,
                            duration_high=None,
                            body=None):
        """Does a POST request to /report/sessions.

        Detailed report of session duration and number of bytes transferred
        per day.

        Args:
            account_number (string): The unique identifier for the account
            imei (string): International Mobile Device Identifier. The unique
                identifier of the device.
            start_date (string, optional): Start date of session to include.
                If not specified information will be shown from the earliest
                available (180 days). ISO 8601 format.
            end_date (string, optional): End date of session to include. If
                not specified information will be shown to the latest
                available. ISO 8601 format.
            duration_low (int, optional): The Low value of session duration.
            duration_high (int, optional): The High value of session
                duration.
            body (SessionReportRequest, optional): Session report request
                example

        Returns:
            SessionLevel: Response from the API. A successful response
                includes the session information for an individual device.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT10)
            .path('/report/sessions')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('accountNumber')
                          .value(account_number))
            .header_param(Parameter()
                          .key('imei')
                          .value(imei))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .header_param(Parameter()
                          .key('startDate')
                          .value(start_date))
            .header_param(Parameter()
                          .key('endDate')
                          .value(end_date))
            .header_param(Parameter()
                          .key('durationLow')
                          .value(duration_low))
            .header_param(Parameter()
                          .key('durationHigh')
                          .value(duration_high))
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
            .deserialize_into(SessionLevel.from_dictionary)
            .local_error('400', 'Bad request.', ErrorResponseError2Exception)
            .local_error('401', 'Unauthorized request. Access token is missing or invalid.', ErrorResponseError2Exception)
            .local_error('403', 'Forbidden request.', ErrorResponseError2Exception)
            .local_error('404', 'Bad request. Not found.', ErrorResponseError2Exception)
            .local_error('409', 'Bad request. Conflict state.', ErrorResponseError2Exception)
            .local_error('500', 'Internal Server Error.', ErrorResponseError2Exception)
        ).execute()
