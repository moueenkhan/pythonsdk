# Service Onboarding

```python
service_onboarding_controller = client.service_onboarding
```

## Class Name

`ServiceOnboardingController`

## Methods

* [Get Services](../../doc/controllers/service-onboarding.md#get-services)
* [Register Service](../../doc/controllers/service-onboarding.md#register-service)
* [Get Service Details](../../doc/controllers/service-onboarding.md#get-service-details)
* [Remove User Service](../../doc/controllers/service-onboarding.md#remove-user-service)
* [Check Job Status](../../doc/controllers/service-onboarding.md#check-job-status)


# Get Services

Fetch all organizational services in the platform

```python
def get_services(self,
                account_name,
                correlation_id=None,
                name=None,
                q=None,
                limit=None,
                off_set=None,
                sort_key=None,
                sort_dir=None,
                details_flag=True)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `name` | `string` | Query, Optional | Name of the service whose information needs to be fetched.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `q` | `string` | Query, Optional | Use the comma (:) character to separate multiple values eg type=myService:workloads.packageType=Helm,YAML:state=DRAFTED,VALIDATION_COMPLETED<br>**Constraints**: *Maximum Length*: `2048`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `limit` | `long\|int` | Query, Optional | number of items to return<br>**Constraints**: `>= 0`, `<= 1024` |
| `off_set` | `long\|int` | Query, Optional | Id of the last respose value in the previous list<br>**Constraints**: `>= 0`, `<= 1024` |
| `sort_key` | `string` | Query, Optional | Sorts the response by an attribute. Default is created_at<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `sort_dir` | [`SortDirectionEnum`](../../doc/models/sort-direction-enum.md) | Query, Optional | Sorts the response. Use asc for ascending or desc for descending order. The default is desc.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `details_flag` | `bool` | Query, Optional | Default as true. If it is true then it will return all details.<br>**Default**: `True` |

## Response Type

[`GetAllServiceRes`](../../doc/models/get-all-service-res.md)

## Example Usage

```python
account_name = 'AccountName0'
details_flag = True

result = service_onboarding_controller.get_services(account_name, None, None, None, None, None, None, None, details_flag)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Register Service

Create a new service with in user's organization

```python
def register_service(self,
                    account_name,
                    body,
                    correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`Service`](../../doc/models/service.md) | Body, Required | body |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`Service`](../../doc/models/service.md)

## Example Usage

```python
account_name = 'AccountName0'
body = Service()
body.name = 'MyService'
body.version = '1.0.0'

result = service_onboarding_controller.register_service(account_name, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 403 | Forbidden | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 415 | Unsupported media type | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 429 | Too many requests | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Get Service Details

Fetch a service details with in user's organization using service name and version

```python
def get_service_details(self,
                       account_name,
                       service_name,
                       version,
                       correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service whose information needs to be fetched.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of service whose information needs to be fetched.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`Service`](../../doc/models/service.md)

## Example Usage

```python
account_name = 'AccountName0'
service_name = 'serviceName8'
version = 'version4'

result = service_onboarding_controller.get_service_details(account_name, service_name, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| Default | unexpected error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Remove User Service

Remove a service from user's organization

```python
def remove_user_service(self,
                       account_name,
                       service_name,
                       version,
                       correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service which is about to be deleted.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of the service which is about to be deleted.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`DeleteResponse`](../../doc/models/delete-response.md)

## Example Usage

```python
account_name = 'AccountName0'
service_name = 'serviceName8'
version = 'version4'

result = service_onboarding_controller.remove_user_service(account_name, service_name, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Check Job Status

Check current status of job for a service using job ID

```python
def check_job_status(self,
                    account_name,
                    job_id,
                    correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `job_id` | `string` | Template, Required | Auto Generated Id of the job.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`CurrentStatus`](../../doc/models/current-status.md)

## Example Usage

```python
account_name = 'AccountName0'
job_id = 'jobId0'

result = service_onboarding_controller.check_job_status(account_name, job_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

