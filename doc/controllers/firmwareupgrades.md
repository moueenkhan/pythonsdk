# Firmwareupgrades

```python
firmwareupgrades_controller = client.firmwareupgrades
```

## Class Name

`FirmwareupgradesController`

## Methods

* [Firmware Query Using GET](../../doc/controllers/firmwareupgrades.md#firmware-query-using-get)
* [Schedule Firmware Upgrade Using POST](../../doc/controllers/firmwareupgrades.md#schedule-firmware-upgrade-using-post)
* [Firmware Upgrade Request Using GET](../../doc/controllers/firmwareupgrades.md#firmware-upgrade-request-using-get)
* [Firmware Upgrade Updatet Using PUT](../../doc/controllers/firmwareupgrades.md#firmware-upgrade-updatet-using-put)
* [Cancel Firmware Upgrade Using DELETE](../../doc/controllers/firmwareupgrades.md#cancel-firmware-upgrade-using-delete)


# Firmware Query Using GET

Lists all device firmware images available for an account, based on the devices registered to that account.

```python
def firmware_query_using_get(self,
                            account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |

## Response Type

[`List of Firmware`](../../doc/models/firmware.md)

## Example Usage

```python
account = '0242078689-00001'

result = firmware_upgrades_controller.firmware_query_using_get(account)
```

## Example Response *(as JSON)*

```json
[
  {
    "firmwareName": "FOTA_Verizon_Model-A_01To02_HF",
    "participantName": "0402196254-00001",
    "launchDate": "2018-04-01T16:03:00.000Z",
    "releaseNote": "",
    "model": "Model-A",
    "make": "Verizon",
    "fromVersion": "VerizonFirmwareVersion-01",
    "toVersion": "VerizonFirmwareVersion-02"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Schedule Firmware Upgrade Using POST

Schedules a firmware upgrade for devices.

```python
def schedule_firmware_upgrade_using_post(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FirmwareUpgradeRequest`](../../doc/models/firmware-upgrade-request.md) | Body, Required | Details of the firmware upgrade request. |

## Response Type

[`FirmwareUpgradeQueryResponse`](../../doc/models/firmware-upgrade-query-response.md)

## Example Usage

```python
body = FirmwareUpgradeRequest()
body.account_name = '0402196254-00001'
body.firmware_name = 'FOTA_Verizon_Model-A_01To02_HF'
body.firmware_to = 'VerizonFirmwareVersion-02'
body.start_date = dateutil.parser.parse('2018-04-01T16:03:00Z')
body.device_list = ['990003425730535', '990000473475989']

result = firmware_upgrades_controller.schedule_firmware_upgrade_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "id": "e3a8d88a-04c6-4ef3-b039-89b62f91e962",
  "accountName": "0242078689-00001",
  "firmwareName": "FOTA_Verizon_Model-A_01To02_HF",
  "firmwareTo": "VerizonFirmwareVersion-02",
  "startDate": "2018-04-01",
  "status": "RequestPending",
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "status": "RequestPending"
    },
    {
      "deviceId": "990000473475989",
      "status": "RequestPending"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Firmware Upgrade Request Using GET

Returns information about a specified upgrade, include the target date of the upgrade, the list of devices in the upgrade, and the status of the upgrade for each device.

```python
def firmware_upgrade_request_using_get(self,
                                      account,
                                      upgrade_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `upgrade_id` | `string` | Template, Required | The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled. |

## Response Type

[`FirmwareUpgradeQueryResponse`](../../doc/models/firmware-upgrade-query-response.md)

## Example Usage

```python
account = '0242078689-00001'
upgrade_id = 'e3a8d88a-04c6-4ef3-b039-89b62f91e962'

result = firmware_upgrades_controller.firmware_upgrade_request_using_get(account, upgrade_id)
```

## Example Response *(as JSON)*

```json
{
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "accountName": "0402196254-00001",
  "firmwareName": "FOTA_Verizon_Model-A_01To02_HF",
  "firmwareTo": "VerizonFirmwareVersion-02",
  "startDate": "2018-04-01",
  "status": "Queued",
  "deviceList": [
    {
      "deviceId": "900000000000002",
      "status": "Device Accepted",
      "resultReason": "success"
    },
    {
      "deviceId": "900000000000003",
      "status": "Device Accepted",
      "resultReason": "success"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Firmware Upgrade Updatet Using PUT

Add or remove devices from a scheduled upgrade.

```python
def firmware_upgrade_updatet_using_put(self,
                                      account,
                                      upgrade_id,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `upgrade_id` | `string` | Template, Required | The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled. |
| `body` | [`FirmwareUpgradeChangeRequest`](../../doc/models/firmware-upgrade-change-request.md) | Body, Required | List of devices to add or remove. |

## Response Type

[`FirmwareUpgradeChangeResponse`](../../doc/models/firmware-upgrade-change-response.md)

## Example Usage

```python
account = '0242078689-00001'
upgrade_id = 'e3a8d88a-04c6-4ef3-b039-89b62f91e962'
body = FirmwareUpgradeChangeRequest()
body.mtype = FirmwareTypeEnumListEnum.APPEND
body.device_list = ['15-digit IMEI', '15-digit IMEI']

result = firmware_upgrades_controller.firmware_upgrade_updatet_using_put(account, upgrade_id, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "id": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
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


# Cancel Firmware Upgrade Using DELETE

Cancel a scheduled upgrade.

```python
def cancel_firmware_upgrade_using_delete(self,
                                        account,
                                        upgrade_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `upgrade_id` | `string` | Template, Required | The UUID of the scheduled upgrade that you want to cancel. |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
account = '0242078689-00001'
upgrade_id = 'e3a8d88a-04c6-4ef3-b039-89b62f91e962'

result = firmware_upgrades_controller.cancel_firmware_upgrade_using_delete(account, upgrade_id)
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

