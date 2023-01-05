# Service Profile

```python
service_profile_controller = client.service_profile
```

## Class Name

`ServiceProfileController`

## Methods

* [Create-Service-Profile](../../doc/controllers/service-profile.md#create-service-profile)
* [Update-Service-Profile](../../doc/controllers/service-profile.md#update-service-profile)
* [Submit-Service-Profile](../../doc/controllers/service-profile.md#submit-service-profile)


# Create-Service-Profile

Creates a service profile that describes the resource requirements of a service.

```python
def create_service_profile(self,
                          account_name,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `body` | [`PostServiceProfile`](../../doc/models/post-service-profile.md) | Body, Required | The request body passes all of the needed parameters to create a service profile. |

## Response Type

[`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md)

## Example Usage

```python
account_name = 'AccountName0'
body = PostServiceProfile()

result = service_profile_controller.create_service_profile(account_name, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |


# Update-Service-Profile

Update the definition of a Service Profile.

```python
def update_service_profile(self,
                          id,
                          body,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `36`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `body` | [`PostServiceProfile`](../../doc/models/post-service-profile.md) | Body, Required | The request body passes the rest of the needed parameters to create a service profile. Parameters other than `serviceProfileId` will be edited |
| `account_name` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md)

## Example Usage

```python
id = 'Id6'
body = PostServiceProfile()

result = service_profile_controller.update_service_profile(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |


# Submit-Service-Profile

Submit a service profile

```python
def submit_service_profile(self,
                          id,
                          body,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |
| `body` | [`ServicesProfileRegistration`](../../doc/models/services-profile-registration.md) | Body, Required | The request body passes all of the needed parameters to create a service profile. |
| `account_name` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`ErrorResponse`](../../doc/models/error-response.md)

## Example Usage

```python
id = 'id0'
body = ServicesProfileRegistration()

result = service_profile_controller.submit_service_profile(id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 412 | Precondition Failed | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 500 | Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |

