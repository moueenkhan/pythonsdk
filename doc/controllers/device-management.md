# Device Management

```python
device_management_controller = client.device_management
```

## Class Name

`DeviceManagementController`

## Methods

* [Devices Services Get](../../doc/controllers/device-management.md#devices-services-get)
* [Devices Services Put](../../doc/controllers/device-management.md#devices-services-put)


# Devices Services Get

Gets the list of a status for hyper-precise location devices

```python
def devices_services_get(self,
                        imei,
                        account_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `string` | Query, Required | A unique identifier for a `Device`. |
| `account_number` | `string` | Query, Required | A unique identifier for a `Account`. |

## Response Type

[`BullseyeServiceResponse`](../../doc/models/bullseye-service-response.md)

## Example Usage

```python
imei = 'imei6'
account_number = 'accountNumber2'

result = device_management_controller.devices_services_get(imei, account_number)
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


# Devices Services Put

Enable/disable hyper-precise service for a device.

```python
def devices_services_put(self,
                        imei,
                        bullseye_enable,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `string` | Header, Required | International Mobile Equipment Identifier. The unique ID of a device. |
| `bullseye_enable` | `bool` | Header, Required | Set to Enable (true) or Disable (false) |
| `body` | [`BullseyeServiceRequest`](../../doc/models/bullseye-service-request.md) | Body, Optional | List of devices and hyper-precise required statuses. |

## Response Type

[`BullseyeServiceResponse`](../../doc/models/bullseye-service-response.md)

## Example Usage

```python
imei = 'imei6'
bullseye_enable = False

result = device_management_controller.devices_services_put(imei, bullseye_enable)
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

