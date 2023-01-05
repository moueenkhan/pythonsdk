# Licenses

For the deprecated endpoints, please use the **v3** endpoints

```python
licenses_controller = client.licenses
```

## Class Name

`LicensesController`

## Methods

* [Get User Fota Licenses Summary](../../doc/controllers/licenses.md#get-user-fota-licenses-summary)
* [Assign Fota Licenses to Devices](../../doc/controllers/licenses.md#assign-fota-licenses-to-devices)
* [Remove Licenses From Devices](../../doc/controllers/licenses.md#remove-licenses-from-devices)
* [Summarize Fota Licenses Assignment](../../doc/controllers/licenses.md#summarize-fota-licenses-assignment)
* [Assign Fota Licenses to Devices 1](../../doc/controllers/licenses.md#assign-fota-licenses-to-devices-1)
* [Remove Licenses From Devices 1](../../doc/controllers/licenses.md#remove-licenses-from-devices-1)


# Get User Fota Licenses Summary

The endpoint allows user to list license usage.

```python
def get_user_fota_licenses_summary(self,
                                  account,
                                  last_seen_device_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `last_seen_device_id` | `string` | Query, Optional | Last seen device identifier |

## Response Type

[`LicenseSummary`](../../doc/models/license-summary.md)

## Example Usage

```python
account = '0000123456-00001'
last_seen_device_id = '15-digit IMEI'

result = licenses_controller.get_user_fota_licenses_summary(account, last_seen_device_id)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0402196254-00001",
  "totalLicense": 5000,
  "assignedLicenses": 4319,
  "hasMoreData": true,
  "lastSeenDeviceId": "1000",
  "maxPageSize": 10,
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000473475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000347475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990007303425535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Assign Fota Licenses to Devices

**This endpoint is deprecated.**

This endpoint allows user to assign licenses to a list of devices.

```python
def assign_fota_licenses_to_devices(self,
                                   account,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`LicenseIMEI`](../../doc/models/license-imei.md) | Body, Required | License assignment |

## Response Type

[`LicenseResponse`](../../doc/models/license-response.md)

## Example Usage

```python
account = '0242078689-00001'
body = LicenseIMEI()
body.device_list = ['990003425730524', '990000473475967']

result = licenses_controller.assign_fota_licenses_to_devices(account, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licTotalCount": 1000,
  "licUsedCount": 502,
  "deviceList": [
    {
      "deviceId": "990003425730524",
      "status": "Success",
      "resultReason": "Success"
    },
    {
      "deviceId": "990000473475967",
      "status": "Failure",
      "resultReason": "Device does not exist."
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Remove Licenses From Devices

**This endpoint is deprecated.**

This endpoint allows user to remove licenses from a list of devices.

```python
def remove_licenses_from_devices(self,
                                account,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`LicenseIMEI`](../../doc/models/license-imei.md) | Body, Required | License removal |

## Response Type

[`LicenseResponse`](../../doc/models/license-response.md)

## Example Usage

```python
account = '0242078689-00001'
body = LicenseIMEI()
body.device_list = ['990003425730535', '990000473475989', '900000000000999']

result = licenses_controller.remove_licenses_from_devices(account, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licTotalCount": 1000,
  "licUsedCount": 998,
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "status": "Success",
      "resultReason": "Success"
    },
    {
      "deviceId": "990000473475989",
      "status": "Success",
      "resultReason": "Success"
    },
    {
      "deviceId": "900000000000999",
      "status": "Failure",
      "resultReason": "No license attached to device"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Summarize Fota Licenses Assignment

The endpoint allows user to list license usage

```python
def summarize_fota_licenses_assignment(self,
                                      acc,
                                      last_seen_device_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `last_seen_device_id` | `string` | Query, Optional | Last seen device identifier |

## Response Type

[`LicenseSummary`](../../doc/models/license-summary.md)

## Example Usage

```python
acc = '0000123456-00001'
last_seen_device_id = '0'

result = licenses_controller.summarize_fota_licenses_assignment(acc, last_seen_device_id)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "totalLicenses": 5000,
  "assignedLicenses": 4319,
  "hasMoreData": true,
  "lastSeenDeviceId": "1000",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "assignmentTime": "2017-11-29 20:15:42.738 +0000 UTC"
    },
    {
      "deviceId": "15-digit IMEI",
      "assignmentTime": "2017-11-29 20:15:42.738 +0000 UTC"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Assign Fota Licenses to Devices 1

This endpoint allows user to assign licenses to a list of devices

```python
def assign_fota_licenses_to_devices_1(self,
                                     acc,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `body` | [`LicensesAssignedRemovedRequest`](../../doc/models/licenses-assigned-removed-request.md) | Body, Required | License assignment |

## Response Type

[`LicenseResponse1`](../../doc/models/license-response-1.md)

## Example Usage

```python
acc = '0000123456-00001'
body = LicensesAssignedRemovedRequest()
body.device_list = ['15-digit IMEI', '15-digit IMEI']

result = licenses_controller.assign_fota_licenses_to_devices_1(acc, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "licCount": 2,
  "licUsedCount": 2,
  "licTotalCount": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "LicenseAssignSuccess",
      "Reason": "Device license preexisting"
    },
    {
      "deviceId": "15-digit IMEI",
      "status": "LicenseAssignSuccess",
      "Reason": "Device license preexisting"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Remove Licenses From Devices 1

This endpoint allows user to remove licenses from a list of devices

```python
def remove_licenses_from_devices_1(self,
                                  acc,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `body` | [`LicensesAssignedRemovedRequest`](../../doc/models/licenses-assigned-removed-request.md) | Body, Required | License removal. |

## Response Type

[`LicenseResponse1`](../../doc/models/license-response-1.md)

## Example Usage

```python
acc = '0000123456-00001'
body = LicensesAssignedRemovedRequest()
body.device_list = ['15-digit IMEI', '15-digit IMEI', '15-digit IMEI']

result = licenses_controller.remove_licenses_from_devices_1(acc, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "licCount": 9000,
  "licUsedCount": 998,
  "licTotalCount": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "status": "Success",
      "resultReason": "Success",
      "updatedTime": "2021-06-10T15:13:30.941Z",
      "recentAttemptTime": "2021-06-10T15:13:30.941Z",
      "nextAttemptTime": "2021-06-10T15:13:30.941Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

