# Campaigns

Schedule, retreive or cancel scheduled FOTA campaigns

```python
campaigns_controller = client.campaigns
```

## Class Name

`CampaignsController`

## Methods

* [Schedule Software Upgrade](../../doc/controllers/campaigns.md#schedule-software-upgrade)
* [Get Software Upgrade Details](../../doc/controllers/campaigns.md#get-software-upgrade-details)
* [Update Software Upgrade](../../doc/controllers/campaigns.md#update-software-upgrade)
* [Cancel Scheduled Software Upgrade](../../doc/controllers/campaigns.md#cancel-scheduled-software-upgrade)
* [Change Campaign Dates and Time Windows](../../doc/controllers/campaigns.md#change-campaign-dates-and-time-windows)
* [Schedule a Firmware Upgrade](../../doc/controllers/campaigns.md#schedule-a-firmware-upgrade)
* [Add or Remove Devices](../../doc/controllers/campaigns.md#add-or-remove-devices)
* [Change Campaign Dates Time](../../doc/controllers/campaigns.md#change-campaign-dates-time)
* [Retrieve Campaign Level Information](../../doc/controllers/campaigns.md#retrieve-campaign-level-information)
* [Delete a Campaign](../../doc/controllers/campaigns.md#delete-a-campaign)


# Schedule Software Upgrade

This endpoint allows user to schedule a software upgrade.

```python
def schedule_software_upgrade(self,
                             account,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`CampaignSoftwareUpgrade`](../../doc/models/campaign-software-upgrade.md) | Body, Required | Software upgrade information |

## Response Type

[`CampaignSoftware`](../../doc/models/campaign-software.md)

## Example Usage

```python
account = '0000123456-00001'
body = CampaignSoftwareUpgrade()
body.campaign_name = 'FOTA_Verizon_Upgrade'
body.software_name = 'FOTA_Verizon_Model-A_02To03_HF'
body.software_from = 'FOTA_Verizon_Model-A_00To01_HF'
body.software_to = 'FOTA_Verizon_Model-A_02To03_HF'
body.distribution_type = 'HTTP'
body.start_date = dateutil.parser.parse('2020-08-21').date()
body.end_date = dateutil.parser.parse('2020-08-22').date()
body.download_after_date = dateutil.parser.parse('2020-08-21').date()
body.download_time_window_list = []

body.download_time_window_list.append(TimeWindow())
body.download_time_window_list[0].start_time = 20
body.download_time_window_list[0].end_time = 21

body.install_after_date = dateutil.parser.parse('2020-08-21').date()
body.install_time_window_list = []

body.install_time_window_list.append(TimeWindow())
body.install_time_window_list[0].start_time = 22
body.install_time_window_list[0].end_time = 23

body.device_list = ['990013907835573', '990013907884259']

result = campaigns_controller.schedule_software_upgrade(account, body)
```

## Example Response *(as JSON)*

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "make": "Verizon",
  "model": "Model-A",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
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
  "status": "CampaignRequestPending"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Software Upgrade Details

This endpoint allows user to get information of a software upgrade.

```python
def get_software_upgrade_details(self,
                                account,
                                campaign_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade identifier |

## Response Type

[`CampaignSoftware`](../../doc/models/campaign-software.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

result = campaigns_controller.get_software_upgrade_details(account, campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "make": "Verizon",
  "model": "Model-A",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
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
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Update Software Upgrade

This endpoint allows user to Add or Remove devices to an existing software upgrade.

```python
def update_software_upgrade(self,
                           account,
                           campaign_id,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade information |
| `body` | [`AddOrRemoveDeviceRequest`](../../doc/models/add-or-remove-device-request.md) | Body, Required | Add or remove device to existing software upgrade information |

## Response Type

[`AddOrRemoveDeviceResp`](../../doc/models/add-or-remove-device-resp.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'
body = AddOrRemoveDeviceRequest()
body.mtype = 'remove'
body.device_list = ['990013907884259', '990013907835573', '990013907833575']

result = campaigns_controller.update_software_upgrade(account, campaign_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Cancel Scheduled Software Upgrade

This endpoint allows user to cancel software upgrade. A software upgrade already started can not be cancelled.

```python
def cancel_scheduled_software_upgrade(self,
                                     account,
                                     campaign_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade information |

## Response Type

[`SuccessResponse1`](../../doc/models/success-response-1.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'

result = campaigns_controller.cancel_scheduled_software_upgrade(account, campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Change Campaign Dates and Time Windows

This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged should be also provided

```python
def change_campaign_dates_and_time_windows(self,
                                          account,
                                          campaign_id,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Software upgrade information |
| `body` | [`ChangeCampaignDatesRequest`](../../doc/models/change-campaign-dates-request.md) | Body, Required | New dates and time windows |

## Response Type

[`CampaignSoftware`](../../doc/models/campaign-software.md)

## Example Usage

```python
account = '0000123456-00001'
campaign_id = '60b5d639-ccdc-4db8-8824-069bd94c95bf'
body = ChangeCampaignDatesRequest()
body.start_date = dateutil.parser.parse('2020-08-21').date()
body.end_date = dateutil.parser.parse('2020-08-22').date()
body.download_after_date = dateutil.parser.parse('2020-08-21').date()
body.download_time_window_list = []

body.download_time_window_list.append(TimeWindow())
body.download_time_window_list[0].start_time = 3
body.download_time_window_list[0].end_time = 4

body.install_after_date = dateutil.parser.parse('2020-08-21').date()
body.install_time_window_list = []

body.install_time_window_list.append(TimeWindow())
body.install_time_window_list[0].start_time = 5
body.install_time_window_list[0].end_time = 6


result = campaigns_controller.change_campaign_dates_and_time_windows(account, campaign_id, body)
```

## Example Response *(as JSON)*

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "campaignName": "FOTA_Verizon_Upgrade",
  "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
  "distributionType": "HTTP",
  "make": "Verizon",
  "model": "Model-A",
  "softwareFrom": "FOTA_Verizon_Model-A_00To01_HF",
  "softwareTo": "FOTA_Verizon_Model-A_02To03_HF",
  "startDate": "2020-08-21",
  "endDate": "2020-08-22",
  "downloadAfterDate": "2020-08-21",
  "downloadTimeWindowList": [
    {
      "startTime": 3,
      "endTime": 4
    },
    {
      "startTime": 5,
      "endTime": 6
    }
  ],
  "installAfterDate": "2020-08-21",
  "installTimeWindowList": [
    {
      "startTime": 5,
      "endTime": 6
    },
    {
      "startTime": 6,
      "endTime": 7
    }
  ],
  "status": "RequestPending"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Schedule a Firmware Upgrade

This endpoint allows a user to schedule a firmware upgrade for a list of devices

```python
def schedule_a_firmware_upgrade(self,
                               acc,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `body` | [`CampaignFirmwareUpgrade`](../../doc/models/campaign-firmware-upgrade.md) | Body, Required | Firmware upgrade information |

## Response Type

[`FirmwareCampaign`](../../doc/models/firmware-campaign.md)

## Example Usage

```python
acc = '0000123456-00001'
body = CampaignFirmwareUpgrade()
body.campaign_name = 'Smart FOTA - test 4'
body.firmware_name = 'SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657'
body.firmware_from = 'SR1.2.0.0-10512'
body.firmware_to = 'SR1.2.0.0-10657'
body.protocol = 'LWM2M'
body.start_date = dateutil.parser.parse('2021-09-29').date()
body.end_date = dateutil.parser.parse('2021-10-01').date()
body.campaign_time_window_list = []

body.campaign_time_window_list.append(TimeWindow())
body.campaign_time_window_list[0].start_time = 18
body.campaign_time_window_list[0].end_time = 22

body.device_list = ['15-digit IMEI']

result = campaigns_controller.schedule_a_firmware_upgrade(acc, body)
```

## Example Response *(as JSON)*

```json
{
  "id": "f858b8c4-2153-11ec-8c44-aeb16d1aa652",
  "accountName": "0000123456-00001",
  "campaignName": "Smart FOTA - test 4",
  "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657",
  "protocol": "LWM2M",
  "firmwareFrom": "SR1.2.0.0-10512",
  "firmwareTo": "SR1.2.0.0-10657",
  "make": "SEQUANS Communications",
  "model": "GM01Q",
  "status": "CampaignRequestPending",
  "startDate": "2021-09-29",
  "endDate": "2021-10-01",
  "campaignTimeWindowList": [
    {
      "startTime": 18,
      "endTime": 22
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Add or Remove Devices

This endpoint allows user to Add or Remove devices to an existing campaign

```python
def add_or_remove_devices(self,
                         acc,
                         campaign_id,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | firmware upgrade information |
| `body` | [`AddOrRemoveDeviceRequest`](../../doc/models/add-or-remove-device-request.md) | Body, Required | Add or remove device to existing upgrade information |

## Response Type

[`AddOrRemoveDeviceResp1`](../../doc/models/add-or-remove-device-resp-1.md)

## Example Usage

```python
acc = '0000123456-00001'
campaign_id = 'campaignId0'
body = AddOrRemoveDeviceRequest()
body.mtype = 'remove'
body.device_list = ['15-digit IMEI', '15-digit IMEI', '15-digit IMEI']

result = campaigns_controller.add_or_remove_devices(acc, campaign_id, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "campaignId": "",
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "AddDeviceSucceed",
      "Reason": "Device added Successfully"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "AddDeviceSucceed",
      "Reason": "Device added Successfully"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Change Campaign Dates Time

This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged should be also provided

```python
def change_campaign_dates_time(self,
                              acc,
                              campaign_id,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Firmware upgrade information |
| `body` | [`ChangeCampaignDatesRequest1`](../../doc/models/change-campaign-dates-request-1.md) | Body, Required | New dates and time windows |

## Response Type

[`FirmwareCampaign`](../../doc/models/firmware-campaign.md)

## Example Usage

```python
acc = '0000123456-00001'
campaign_id = 'campaignId0'
body = ChangeCampaignDatesRequest1()
body.start_date = dateutil.parser.parse('2022-02-23').date()
body.end_date = dateutil.parser.parse('2022-02-24').date()
body.campaign_time_window_list = []

body.campaign_time_window_list.append(TimeWindow())
body.campaign_time_window_list[0].start_time = 14
body.campaign_time_window_list[0].end_time = 18


result = campaigns_controller.change_campaign_dates_time(acc, campaign_id, body)
```

## Example Response *(as JSON)*

```json
{
  "id": "4e03b882-936a-11ec-931f-76f56843c393",
  "accountName": "0000123456-00001",
  "campaignName": "modify-campaign-test-1",
  "firmwareName": "NordicSemiconductorASA_nRF9160_ee58ac77-f1fd-4960-8dc4-4d32e118a6d4_4325d595-7b69-4474-ba39-9c177930aac3",
  "protocol": "LWM2M",
  "firmwareFrom": "ee58ac77-f1fd-4960-8dc4-4d32e118a6d4",
  "firmwareTo": "4325d595-7b69-4474-ba39-9c177930aac3",
  "make": "Nordic Semiconductor ASA",
  "model": "nRF9160",
  "status": "CampaignRequestQueued",
  "startDate": "2022-02-23",
  "endDate": "2022-02-24",
  "campaignTimeWindowList": [
    {
      "startTime": 14,
      "endTime": 18
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Retrieve Campaign Level Information

This endpoint allows the user to retrieve campaign level information for a specified campaign

```python
def retrieve_campaign_level_information(self,
                                       acc,
                                       campaign_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Firmware upgrade identifier |

## Response Type

[`Campaign`](../../doc/models/campaign.md)

## Example Usage

```python
acc = '0000123456-00001'
campaign_id = 'campaignId0'

result = campaigns_controller.retrieve_campaign_level_information(acc, campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "f858b8c4-2153-11ec-8c44-aeb16d1aa652",
  "accountName": "0642233522-00001",
  "campaignName": "Smart FOTA - test 4",
  "protocol": "LWM2M",
  "make": "SEQUANS Communications",
  "model": "GM01Q",
  "status": "CampaignPreScheduled",
  "startDate": "2021-09-29",
  "endDate": "2021-10-01",
  "firmwareName": "SEQUANSCommunications_GM01Q_SR1.2.0.0-10512_SR1.2.0.0-10657",
  "firmwareFrom": "SR1.2.0.0-10512",
  "firmwareTo": "SR1.2.0.0-10657",
  "timeWindowList": [
    {
      "startTime": 18,
      "endTime": 22
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Delete a Campaign

This endpoint allows user to cancel a firmware campaign. A firmware campaign already started can not be cancelled

```python
def delete_a_campaign(self,
                     acc,
                     campaign_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `campaign_id` | `string` | Template, Required | Firmware upgrade information |

## Response Type

[`SuccessResponse1`](../../doc/models/success-response-1.md)

## Example Usage

```python
acc = '0000123456-00001'
campaign_id = 'campaignId0'

result = campaigns_controller.delete_a_campaign(acc, campaign_id)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

