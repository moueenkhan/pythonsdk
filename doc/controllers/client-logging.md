# Client Logging

```python
client_logging_controller = client.client_logging
```

## Class Name

`ClientLoggingController`

## Methods

* [Get Logging Enabled Devices List](../../doc/controllers/client-logging.md#get-logging-enabled-devices-list)
* [Enable Logging for Devices List](../../doc/controllers/client-logging.md#enable-logging-for-devices-list)
* [Disable Logging for Devices List](../../doc/controllers/client-logging.md#disable-logging-for-devices-list)
* [Enable Device Logging](../../doc/controllers/client-logging.md#enable-device-logging)
* [Delete Device Logging](../../doc/controllers/client-logging.md#delete-device-logging)
* [Get Device Logs](../../doc/controllers/client-logging.md#get-device-logs)


# Get Logging Enabled Devices List

Returns an array of all devices in the specified account for which logging is enabled.

```python
def get_logging_enabled_devices_list(self,
                                    account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |

## Response Type

[`List of DeviceLoggingStatus`](../../doc/models/device-logging-status.md)

## Example Usage

```python
account = '0000123456-00001'

result = client_logging_controller.get_logging_enabled_devices_list(account)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "991124018926684",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "992234129057795",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "998891785613351",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-23"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Enable Logging for Devices List

Each customer may have a maximum of 20 devices enabled for logging

```python
def enable_logging_for_devices_list(self,
                                   account,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`DeviceLoggingRequest`](../../doc/models/device-logging-request.md) | Body, Required | Device logging information |

## Response Type

[`List of DeviceLoggingStatus`](../../doc/models/device-logging-status.md)

## Example Usage

```python
account = '0000123456-00001'
body = DeviceLoggingRequest()
body.device_ids = ['990013907835573', '991124018926684', '992234129057795', '998891785613351', '990013907835573']

result = client_logging_controller.enable_logging_for_devices_list(account, body)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "991124018926684",
    "expiryDate": "2020-10-19"
  },
  {
    "deviceId": "992234129057795",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "998891785613351",
    "expiryDate": "2020-10-23"
  },
  {
    "deviceId": "990013907835573",
    "expiryDate": "2020-10-23"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Disable Logging for Devices List

Turn logging off for a list of devices

```python
def disable_logging_for_devices_list(self,
                                    account,
                                    device_ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `device_ids` | `string` | Query, Required | the list of device IDs |

## Response Type

`void`

## Example Usage

```python
account = '0000123456-00001'
device_ids = '990013907835573'

result = client_logging_controller.disable_logging_for_devices_list(account, device_ids)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Enable Device Logging

Enables logging for a specific device.

```python
def enable_device_logging(self,
                         account,
                         device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `device_id` | `string` | Template, Required | Device IMEI identifier |

## Response Type

[`DeviceLoggingStatus`](../../doc/models/device-logging-status.md)

## Example Usage

```python
account = '0000123456-00001'
device_id = '990013907835573'

result = client_logging_controller.enable_device_logging(account, device_id)
```

## Example Response *(as JSON)*

```json
{
  "deviceId": "990013907835573",
  "expiryDate": "2020-10-19"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Delete Device Logging

Disables logging for a specific device.

```python
def delete_device_logging(self,
                         account,
                         device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `device_id` | `string` | Template, Required | Device IMEI identifier |

## Response Type

`void`

## Example Usage

```python
account = '0000123456-00001'
device_id = '990013907835573'

result = client_logging_controller.delete_device_logging(account, device_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Device Logs

Gets logs for a specific device.

```python
def get_device_logs(self,
                   account,
                   device_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `device_id` | `string` | Template, Required | Device IMEI identifier |

## Response Type

[`List of DeviceLog`](../../doc/models/device-log.md)

## Example Usage

```python
account = '0000123456-00001'
device_id = '990013907835573'

result = client_logging_controller.get_device_logs(account, device_id)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceId": "990013907835573",
    "logTime": "2020-10-22T19:29:50.901Z",
    "logType": "string",
    "eventLog": "string",
    "binaryLogFileBase64": "string",
    "binaryLogFilename": "string"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

