# Service Instance Operations

```python
service_instance_operations_controller = client.service_instance_operations
```

## Class Name

`ServiceInstanceOperationsController`

## Methods

* [Service Instance Retrive](../../doc/controllers/service-instance-operations.md#service-instance-retrive)
* [All Instance Retrieve](../../doc/controllers/service-instance-operations.md#all-instance-retrieve)


# Service Instance Retrive

Retrive a Service Instance

```python
def service_instance_retrive(self,
                            service_instance_id,
                            account_name,
                            cluster=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_instance_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `account_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `cluster` | `bool` | Query, Optional | **Default**: `False` |

## Response Type

[`GetService`](../../doc/models/get-service.md)

## Example Usage

```python
service_instance_id = 'serviceInstanceId2'
account_name = 'AccountName0'
cluster = False

result = service_instance_operations_controller.service_instance_retrive(service_instance_id, account_name, cluster)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 401 | Unauthorized | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 403 | Forbidden | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 404 | Not found | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 415 | Unsupported media type | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 429 | Too many requests | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 500 | Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | unexpected error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |


# All Instance Retrieve

Retrieve all instances for all services

```python
def all_instance_retrieve(self,
                         account_name,
                         offset=None,
                         state=None,
                         limit=None,
                         searchbyname=None,
                         listofstate=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `offset` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `state` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `limit` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64` |
| `searchbyname` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `listofstate` | `List of string` | Query, Optional | **Constraints**: *Maximum Items*: `100`, *Maximum Length*: `128`, *Pattern*: `^(.*)$` |

## Response Type

[`AllServiceInstanceResponse`](../../doc/models/all-service-instance-response.md)

## Example Usage

```python
account_name = 'AccountName0'

result = service_instance_operations_controller.all_instance_retrieve(account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 401 | Unauthorized | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 403 | Forbidden | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 404 | Not found | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 415 | Unsupported media type | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 429 | Too many requests | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 500 | Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | unexpected error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |

