# Service Request

```python
service_request_controller = client.service_request
```

## Class Name

`ServiceRequestController`

## Methods

* [Get Service Launch Request](../../doc/controllers/service-request.md#get-service-launch-request)
* [Create Service Launch Request](../../doc/controllers/service-request.md#create-service-launch-request)
* [Submit Service Request](../../doc/controllers/service-request.md#submit-service-request)


# Get Service Launch Request

Get service launch request

```python
def get_service_launch_request(self,
                              account_name,
                              user_name,
                              id=None,
                              correlation_id=None,
                              name=None,
                              offset=None,
                              limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `user_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `id` | `uuid\|string` | Query, Optional | - |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `name` | `string` | Query, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `offset` | `long\|int` | Query, Optional | **Constraints**: `>= 0`, `<= 1024` |
| `limit` | `long\|int` | Query, Optional | **Constraints**: `>= 0`, `<= 1024` |

## Response Type

[`GetServiceLaunchRequest`](../../doc/models/get-service-launch-request.md)

## Example Usage

```python
account_name = 'AccountName0'
user_name = 'userName2'

result = service_request_controller.get_service_launch_request(account_name, user_name)
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


# Create Service Launch Request

Create servicelaunch request

```python
def create_service_launch_request(self,
                                 account_name,
                                 user_name,
                                 correlation_id=None,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `user_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `body` | [`PostServiceLaunchRequest`](../../doc/models/post-service-launch-request.md) | Body, Optional | - |

## Response Type

[`ServiceLaunchRequestResponse`](../../doc/models/service-launch-request-response.md)

## Example Usage

```python
account_name = 'AccountName0'
user_name = 'userName2'

result = service_request_controller.create_service_launch_request(account_name, user_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 404 | HTTP 404 Not found | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 500 | Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |


# Submit Service Request

Submit service request

```python
def submit_service_request(self,
                          id,
                          account_name,
                          user_name,
                          correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Template, Required | - |
| `account_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `user_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |

## Response Type

[`ServiceLaunchRequestResponse`](../../doc/models/service-launch-request-response.md)

## Example Usage

```python
id = '00001770-0000-0000-0000-000000000000'
account_name = 'AccountName0'
user_name = 'userName2'

result = service_request_controller.submit_service_request(id, account_name, user_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 412 | Precondition Failed | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 500 | Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |

