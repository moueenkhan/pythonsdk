# Firmware

State of Firmware across devices in the account

```python
firmware_controller = client.firmware
```

## Class Name

`FirmwareController`

## Methods

* [List of Available Firmware](../../doc/controllers/firmware.md#list-of-available-firmware)
* [Synchronize Device Firmware](../../doc/controllers/firmware.md#synchronize-device-firmware)
* [Report Device Firmware](../../doc/controllers/firmware.md#report-device-firmware)


# List of Available Firmware

This endpoint allows user to list the firmware of an account

```python
def list_of_available_firmware(self,
                              acc,
                              protocol)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `protocol` | [`FirmwareProtocolEnum`](../../doc/models/firmware-protocol-enum.md) | Query, Required | Filter to retrieve a specific protocol type used |

## Response Type

[`List of FirmwarePackage`](../../doc/models/firmware-package.md)

## Example Usage

```python
acc = '0000123456-00001'
protocol = FirmwareProtocolEnum.LW_M2M

result = firmware_controller.list_of_available_firmware(acc, protocol)
```

## Example Response *(as JSON)*

```json
[
  {
    "firmwareName": "VerizonSmartCommunities_LCO-277C4N_BG96MAR04A04M1G_BG96MAR04A04M1G_BETA0130B",
    "firmwareFrom": "BG96MAR04A04M1G",
    "firmwareTo": "BG96MAR04A04M1G_BETA0130B",
    "launchDate": "2012-04-23T18:25:43.511Z",
    "releaseNote": "",
    "model": "LCO-277C4N",
    "make": "Verizon Smart Communities",
    "protocol": "LWM2M"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Synchronize Device Firmware

Synchronize ThingSpace with the FOTA server for up to 100 devices

```python
def synchronize_device_firmware(self,
                               acc,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `body` | [`LicensesAssignedRemovedRequest`](../../doc/models/licenses-assigned-removed-request.md) | Body, Required | DeviceIds to get firmware info synchronously |

## Response Type

[`DeviceFirmwareList`](../../doc/models/device-firmware-list.md)

## Example Usage

```python
acc = '0000123456-00001'
body = LicensesAssignedRemovedRequest()
body.device_list = ['15-digit IMEI', '15-digit IMEI']

result = firmware_controller.synchronize_device_firmware(acc, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "deviceFirmwarVersionList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "FirmwareVersionUpdateSuccess",
      "Reason": "",
      "firmwareVersion": "SR1.2.0.0-10657",
      "VersionUpdateTime": "2012-04-23T18:25:43.511Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Report Device Firmware

Ask a device to report its firmware version asynchronously

```python
def report_device_firmware(self,
                          acc,
                          device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `device_id` | `string` | Template, Required | Device identifier |

## Response Type

[`UpdateDeviceFirmwareVersionResp`](../../doc/models/update-device-firmware-version-resp.md)

## Example Usage

```python
acc = '0000123456-00001'
device_id = 'deviceId0'

result = firmware_controller.report_device_firmware(acc, device_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

