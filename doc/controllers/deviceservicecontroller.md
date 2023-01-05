# Deviceservicecontroller

```python
deviceservicecontroller = client.deviceservicecontroller
```

## Class Name

`Deviceservicecontroller`

## Methods

* [Assign License Using POST](../../doc/controllers/deviceservicecontroller.md#assign-license-using-post)
* [Assign License Delete Using DELETE](../../doc/controllers/deviceservicecontroller.md#assign-license-delete-using-delete)


# Assign License Using POST

This corresponds to the M2M-MC SOAP interface, `ChangeDeviceSkuSubscription`.

```python
def assign_license_using_post(self,
                             body,
                             x_request_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssignLicenseRequest`](../../doc/models/assign-license-request.md) | Body, Required | Request |
| `x_request_id` | `string` | Header, Optional | Transaction Id<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]-[0-9]{3,32}$` |

## Response Type

[`RequestResponse2`](../../doc/models/request-response-2.md)

## Example Usage

```python
body = AssignLicenseRequest()

result = device_service_controller.assign_license_using_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 401 | Unauthorized | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 403 | Forbidden | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 404 | Not Found / Does not exist | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 406 | Format / Request Unacceptable | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 429 | Too many requests | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| Default | Error response | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |


# Assign License Delete Using DELETE

This corresponds to the M2M-MC SOAP interface, `ChangeDeviceSkuSubscription`.

```python
def assign_license_delete_using_delete(self,
                                      x_request_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_request_id` | `string` | Header, Required | Transaction Id<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]-[0-9]{3,32}$` |

## Response Type

[`RequestResponse2`](../../doc/models/request-response-2.md)

## Example Usage

```python
x_request_id = 'X-Request-ID2'

result = device_service_controller.assign_license_delete_using_delete(x_request_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 401 | Unauthorized | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 403 | Forbidden | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 404 | Not Found / Does not exist | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 406 | Format / Request Unacceptable | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 429 | Too many requests | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| Default | Error response | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |

