# Reports

Status and history information

```python
reports_controller = client.reports
```

## Class Name

`ReportsController`

## Methods

* [Device Query Using GET](../../doc/controllers/reports.md#device-query-using-get)
* [Firmware Status Upgrade Request Using GET](../../doc/controllers/reports.md#firmware-status-upgrade-request-using-get)
* [Device Upgrade History Request Using GET](../../doc/controllers/reports.md#device-upgrade-history-request-using-get)
* [Get Device Software Upgrade History](../../doc/controllers/reports.md#get-device-software-upgrade-history)
* [Get Campaign History for Status](../../doc/controllers/reports.md#get-campaign-history-for-status)
* [Get Campaign Device Status](../../doc/controllers/reports.md#get-campaign-device-status)
* [Get Firmware Campaign Status](../../doc/controllers/reports.md#get-firmware-campaign-status)
* [Get Device Campaign History](../../doc/controllers/reports.md#get-device-campaign-history)
* [Get a Campaign Device Status](../../doc/controllers/reports.md#get-a-campaign-device-status)
* [Report Aggregate Post](../../doc/controllers/reports.md#report-aggregate-post)
* [Report Aggregate Post Async](../../doc/controllers/reports.md#report-aggregate-post-async)
* [Report Session Post](../../doc/controllers/reports.md#report-session-post)


# Device Query Using GET

Returns an array of all devices in the specified account. Each device object includes information needed for managing firmware, including the device make and model, MDN and IMEI, and current firmware version.

```python
def device_query_using_get(self,
                          account,
                          start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `start_index` | `string` | Template, Required | Only return devices with IMEIs larger than this value. Use 0 for the first request. If `hasMoreData`=true in the response, use the `lastSeenDeviceId` value from the response as the startIndex in the next request. |

## Response Type

[`DeviceListQueryResponse`](../../doc/models/device-list-query-response.md)

## Example Usage

```python
account = '0242078689-00001'
start_index = 'startIndex4'

result = reports_controller.device_query_using_get(account, start_index)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078698-00001",
  "hasMoreData": true,
  "lastSeenDeviceId": 900000000001000,
  "deviceList": [
    {
      "deviceId": "900000000000001",
      "mdn": "0000040881",
      "model": "Model-A",
      "make": "Verizon",
      "firmware": "VerizonFirmwareVersion-01",
      "fotaEligible": true,
      "licenseAssigned": true,
      "upgradeTime": "2018-03-03T16:03:33.000Z"
    },
    {
      "deviceId": "900000000000999",
      "mdn": "0000041879",
      "model": "Model-A",
      "make": "Verizon",
      "firmware": "VerizonFirmwareVersion-01",
      "fotaEligible": true,
      "licenseAssigned": true,
      "upgradeTime": "2018-03-03T16:03:33.000Z"
    },
    {
      "deviceId": "900000000001000",
      "mdn": "0000041880",
      "model": "Model-A",
      "make": "Verizon",
      "firmware": "VerizonFirmwareVersion-01",
      "fotaEligible": true,
      "licenseAssigned": true,
      "upgradeTime": "2018-03-03T16:03:33.000Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Firmware Status Upgrade Request Using GET

Returns a list of all upgrades with a specified status.

```python
def firmware_status_upgrade_request_using_get(self,
                                             account,
                                             upgrade_status,
                                             start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `upgrade_status` | [`UpgradeStatusEnumListEnum`](../../doc/models/upgrade-status-enum-list-enum.md) | Template, Required | The status of the upgrades that you want to retrieve. |
| `start_index` | `string` | Template, Required | The zero-based number of the first record to return. Set startIndex=0 for the first request. If `hasMoreFlag`=true in the response, use the `lastSeenUpgradeId` value from the response as the startIndex in the next request. |

## Response Type

[`UpgradeListQueryResponse`](../../doc/models/upgrade-list-query-response.md)

## Example Usage

```python
account = '0242078689-00001'
upgrade_status = UpgradeStatusEnumListEnum.REQUESTPENDING
start_index = 'startIndex4'

result = reports_controller.firmware_status_upgrade_request_using_get(account, upgrade_status, start_index)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Device Upgrade History Request Using GET

Returns the upgrade history of the specified device from the previous six months.

```python
def device_upgrade_history_request_using_get(self,
                                            account,
                                            device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `device_id` | `string` | Template, Required | The IMEI of the device. |

## Response Type

[`List of DeviceUpgradeHistoryQueryResponseItem`](../../doc/models/device-upgrade-history-query-response-item.md)

## Example Usage

```python
account = '0242078689-00001'
device_id = '900000000000001'

result = reports_controller.device_upgrade_history_request_using_get(account, device_id)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "900000000000001",
    "id": "f574fbb8-b291-4cc7-bf22-4e3f27977558",
    "accountName": "0242078689-00001",
    "firmwareFrom": "VerizonFirmwareVersion-02",
    "firmwareTo": "VerizonFirmwareVersion-03",
    "startDate": "2018-03-05",
    "upgradeStartTime": "2018-03-05T19:07:21Z",
    "status": "UpgradeSuccess",
    "reason": "success"
  },
  {
    "deviceId": "900000000000001",
    "id": "5edade25-c06c-4b13-ba2a-fbb9ada93579",
    "accountName": "0242078689-00001",
    "firmwareFrom": "VerizonFirmwareVersion-01",
    "firmwareTo": "VerizonFirmwareVersion-02",
    "startDate": "2018-02-20",
    "upgradeStartTime": "2018-02-20T00:03:19Z",
    "status": "UpgradeSuccess",
    "reason": "success"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Device Software Upgrade History

The endpoint allows user to get software upgrade history of a device based on device IMEI.

```python
def get_device_software_upgrade_history(self,
                                       account,
                                       device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `device_id` | `string` | Template, Required | Device IMEI identifier |

## Response Type

[`List of DeviceSoftwareUpgrade`](../../doc/models/device-software-upgrade.md)

## Example Usage

```python
account = '0000123456-00001'
device_id = '990013907835573'

result = reports_controller.get_device_software_upgrade_history(account, device_id)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
    "accountName": "0402196254-00001",
    "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
    "startDate": "2018-03-05",
    "status": "UpgradeSuccess",
    "reason": "success"
  },
  {
    "deviceId": "990013907835573",
    "id": "50d5d639-aaca-3ca7-7713-958ac83b84ae",
    "accountName": "0402196254-00001",
    "softwareName": "VerizonSoftwareVersion-01",
    "startDate": "2018-02-20",
    "status": "UpgradeSuccess",
    "reason": "success"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Campaign History for Status

The report endpoint allows user to get campaign history of an account for specified status.

```python
def get_campaign_history_for_status(self,
                                   account,
                                   campaign_status,
                                   last_seen_campaign_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_status` | `string` | Query, Required | Campaign status |
| `last_seen_campaign_id` | `string` | Query, Optional | Last seen campaign Id |

## Response Type

[`CampaignHistory`](../../doc/models/campaign-history.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_status = 'campaignStatus6'
last_seen_campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

result = reports_controller.get_campaign_history_for_status(account, campaign_status, last_seen_campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "hasMoreData": true,
  "lastSeenCampaignId": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "campaignList": [
    {
      "accountName": "0402196254-00001",
      "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
      "campaignName": "FOTA_Verizon_Upgrade",
      "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
      "distributionType": "HTTP",
      "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
      "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
      "make": "Verizon",
      "model": "Model-A",
      "startDate": "2020-08-21",
      "endDate": "2020-08-22",
      "downloadAfterDate": "2020-08-21",
      "downloadTimeWindowList": [
        {
          "startTime": 20,
          "endTime": 21
        }
      ],
      "installAfterDate": "2020-08-21",
      "installTimeWindowList": [
        {
          "startTime": 22,
          "endTime": 23
        }
      ],
      "status": "CampaignEnded"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Campaign Device Status

The report endpoint allows user to get the full list of device of a campaign.

```python
def get_campaign_device_status(self,
                              account,
                              campaign_id,
                              last_seen_device_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Campaign identifier |
| `last_seen_device_id` | `string` | Query, Optional | Last seen device identifier |

## Response Type

[`CampaignDevice`](../../doc/models/campaign-device.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'
last_seen_device_id = '15-digit IMEI'

result = reports_controller.get_campaign_device_status(account, campaign_id, last_seen_device_id)
```

## Example Response *(as JSON)*

```json
{
  "totalDevice": 1148,
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradeSuccess",
      "resultReason": "DownloadInstallSucceeded"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradeSuccess",
      "resultReason": "DownloadInstallSucceeded"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradeSuccess",
      "resultReason": "DownloadInstallSucceeded"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Firmware Campaign Status

Retrieve a list of campaigns for an account that have a specified campaign status

```python
def get_firmware_campaign_status(self,
                                acc,
                                campaign_status,
                                last_seen_campaign_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `campaign_status` | `string` | Query, Required | Campaign status |
| `last_seen_campaign_id` | `string` | Query, Optional | Last seen campaign Id |

## Response Type

[`CampaignHistory1`](../../doc/models/campaign-history-1.md)

## Example Usage

```python
acc = '0000123456-00001'
campaign_status = 'campaignStatus6'

result = reports_controller.get_firmware_campaign_status(acc, campaign_status)
```

## Example Response *(as JSON)*

```json
{
  "hasMoreData": true,
  "lastSeenCampaignId": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "campaignList": [
    {
      "accountName": "0000123456-00001",
      "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
      "campaignName": "FOTA_Verizon_Upgrade",
      "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
      "distributionType": "HTTP",
      "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
      "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
      "make": "Verizon",
      "model": "Model-A",
      "status": "CampaignEnded",
      "startDate": "2020-08-21",
      "endDate": "2020-08-22",
      "campaignTimeWindowList": [
        {
          "startTime": 20,
          "endTime": 21
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Device Campaign History

Retrieve campaign history for a specific device

```python
def get_device_campaign_history(self,
                               acc,
                               device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `device_id` | `string` | Template, Required | Device IMEI identifier |

## Response Type

[`List of DeviceFirmwareUpgrade`](../../doc/models/device-firmware-upgrade.md)

## Example Usage

```python
acc = '0000123456-00001'
device_id = 'deviceId0'

result = reports_controller.get_device_campaign_history(acc, device_id)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "15-digit IMEI",
    "campaignId": "252d7ffc-7e35-11ec-931d-76f56843c393",
    "accountName": "0000123456-00001",
    "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10657_SR1.2.0.0-10512",
    "firmwareFrom": "SR1.2.0.0-10657",
    "firmwareTo": "SR1.2.0.0-10512",
    "startDate": "2022-01-25",
    "reportUpdatedTime": "2022-01-26 03:45:01.608 +0000 UTC",
    "status": "UpgradeSuccess",
    "reason": "Upgrade completed successfully"
  },
  {
    "deviceId": "15-digit IMEI",
    "campaignId": "8f5e9a4a-6ce2-11ec-ace7-3ea293843397",
    "accountName": "0000123456-00001",
    "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657",
    "firmwareFrom": "SR1.2.0.0-10512",
    "firmwareTo": "SR1.2.0.0-10657",
    "startDate": "2022-01-03",
    "reportUpdatedTime": "2022-01-04 02:45:00.67 +0000 UTC",
    "status": "UpgradeSuccess",
    "reason": "Upgrade completed successfully"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get a Campaign Device Status

Retrieve a list of all devices in a campaign and the status of each device

```python
def get_a_campaign_device_status(self,
                                acc,
                                campaign_id,
                                last_seen_device_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Campaign identifier |
| `last_seen_device_id` | `string` | Query, Optional | Last seen device identifier |

## Response Type

[`CampaignDevice1`](../../doc/models/campaign-device-1.md)

## Example Usage

```python
acc = '0000123456-00001'
campaign_id = 'campaignId0'

result = reports_controller.get_a_campaign_device_status(acc, campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "totalDevice": 2689,
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradePending",
      "resultReason": "Upgrade pending, the device upgrade is estimated to be scheduled for 06 Oct 22 18:05 UTC",
      "statusTime": "2022-10-05T21:05:27.129Z",
      "recentAttemptTime": "2022-10-05T21:05:01.19Z",
      "nextAttemptTime": "2022-10-06T18:35:00Z"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "UpgradePending",
      "resultReason": "Upgrade pending, the device upgrade is estimated to be scheduled for 06 Oct 22 18:05 UTC",
      "statusTime": "2022-10-05T21:05:27.129Z",
      "recentAttemptTime": "2022-10-05T21:05:01.19Z",
      "nextAttemptTime": "2022-10-06T18:35:00Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Report Aggregate Post

Calculate aggregated report per day with number of sessions and usage information. User will receive synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

```python
def report_aggregate_post(self,
                         account_number,
                         imei,
                         start_date=None,
                         end_date=None,
                         device_group=None,
                         data_plan=None,
                         no_session_flag=None,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Header, Required | The unique identifier for the account |
| `imei` | `string` | Header, Required | Number of devices returning usage info. Could be 0, 1 or more. If 0 the query will return all devices belonging to customer. |
| `start_date` | `string` | Header, Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). ISO 8601 format. |
| `end_date` | `string` | Header, Optional | End date of session to include. If not specified information will be shown to the latest available. ISO 8601 format. |
| `device_group` | `string` | Header, Optional | User defined group name the devices are a member of. |
| `data_plan` | `string` | Header, Optional | The data plan the devices beign queried belong to. |
| `no_session_flag` | `string` | Header, Optional | filters on devices which return only "no sessions". |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Optional | Aggregated report request example |

## Response Type

[`TotalLevel`](../../doc/models/total-level.md)

## Example Usage

```python
account_number = 'accountNumber2'
imei = 'imei6'

result = reports_controller.report_aggregate_post(account_number, imei)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 403 | Forbidden request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 404 | Bad request. Not found. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 409 | Bad request. Conflict state. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 500 | Internal Server Error. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Report Aggregate Post Async

Calculate aggregated report per day with number of sessions and usage information. User will receive an asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

```python
def report_aggregate_post_async(self,
                               x_portal_initiated,
                               account_number,
                               imei,
                               start_date=None,
                               end_date=None,
                               device_group=None,
                               data_plan=None,
                               no_session_flag=None,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_portal_initiated` | `bool` | Header, Required | A flag for using a listener. Set to true or false. |
| `account_number` | `string` | Header, Required | The unique identifier for the account |
| `imei` | `string` | Header, Required | Number of devices returning usage info. Could be 0, 1 or more. If 0 the query will return all devices belonging to customer. |
| `start_date` | `string` | Header, Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). ISO 8601 format. |
| `end_date` | `string` | Header, Optional | End date of session to include. If not specified information will be shown to the latest available. ISO 8601 format. |
| `device_group` | `string` | Header, Optional | User defined group name the devices are a member of. |
| `data_plan` | `string` | Header, Optional | The data plan the devices beign queried belong to. |
| `no_session_flag` | `string` | Header, Optional | filters on devices which return only "no sessions". |
| `body` | [`AggregateSessionReportRequest`](../../doc/models/aggregate-session-report-request.md) | Body, Optional | Aggregated report request example |

## Response Type

[`CallbackResponse`](../../doc/models/callback-response.md)

## Example Usage

```python
x_portal_initiated = False
account_number = 'accountNumber2'
imei = 'imei6'

result = reports_controller.report_aggregate_post_async(x_portal_initiated, account_number, imei)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 403 | Forbidden request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 404 | Bad request. Not found. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 409 | Bad request. Conflict state. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 500 | Internal Server Error. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Report Session Post

Detailed report of session duration and number of bytes transferred per day.

```python
def report_session_post(self,
                       account_number,
                       imei,
                       start_date=None,
                       end_date=None,
                       duration_low=None,
                       duration_high=None,
                       body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Header, Required | The unique identifier for the account |
| `imei` | `string` | Header, Required | International Mobile Device Identifier. The unique identifier of the device. |
| `start_date` | `string` | Header, Optional | Start date of session to include. If not specified information will be shown from the earliest available (180 days). ISO 8601 format. |
| `end_date` | `string` | Header, Optional | End date of session to include. If not specified information will be shown to the latest available. ISO 8601 format. |
| `duration_low` | `int` | Header, Optional | The Low value of session duration. |
| `duration_high` | `int` | Header, Optional | The High value of session duration. |
| `body` | [`SessionReportRequest`](../../doc/models/session-report-request.md) | Body, Optional | Session report request example |

## Response Type

[`SessionLevel`](../../doc/models/session-level.md)

## Example Usage

```python
account_number = 'accountNumber2'
imei = 'imei6'

result = reports_controller.report_session_post(account_number, imei)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 403 | Forbidden request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 404 | Bad request. Not found. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 409 | Bad request. Conflict state. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 500 | Internal Server Error. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |

