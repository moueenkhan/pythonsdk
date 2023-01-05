# Service Management

```python
service_management_controller = client.service_management
```

## Class Name

`ServiceManagementController`

## Methods

* [Start Service Onboarding](../../doc/controllers/service-management.md#start-service-onboarding)
* [Sand Box Start Testing](../../doc/controllers/service-management.md#sand-box-start-testing)
* [Start Publish](../../doc/controllers/service-management.md#start-publish)
* [Stop Service Testing](../../doc/controllers/service-management.md#stop-service-testing)
* [Ready to Public Use](../../doc/controllers/service-management.md#ready-to-public-use)


# Start Service Onboarding

Start service onboarding process to kick off service artifact validation and making the service ready for sandbox testing. On successful completion of this process system will generate claims for each selected cloud provider using which user can start sandbox testing

```python
def start_service_onboarding(self,
                            account_name,
                            service_name,
                            version,
                            correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | Name of the service which is to be onboarded.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `version` | `string` | Template, Required | Version of service  which is to be onboarded.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |

## Response Type

[`ServiceManagementRes`](../../doc/models/service-management-res.md)

## Example Usage

```python
account_name = 'AccountName0'
service_name = 'serviceName8'
version = 'version4'

result = service_management_controller.start_service_onboarding(account_name, service_name, version)
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


# Sand Box Start Testing

Initiate testing of a service in sandbox environment per claim based on service's compatibility(s).

```python
def sand_box_start_testing(self,
                          account_name,
                          service_id,
                          claim_id,
                          body,
                          correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_id` | `string` | Template, Required | serviceId eg:UUID of serviceId Service Created<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `claim_id` | `string` | Template, Required | claimId eg:UUID of claimId Claim Created<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`ClusterInfoDetails`](../../doc/models/cluster-info-details.md) | Body, Required | body |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementRes`](../../doc/models/service-management-res.md)

## Example Usage

```python
account_name = 'AccountName0'
service_id = 'serviceId6'
claim_id = 'claimId8'
body = ClusterInfoDetails()
body.cluster_name = 'ctc-1'
body.namespace = 'default'

result = service_management_controller.sand_box_start_testing(account_name, service_id, claim_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| Default | unexpected error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Start Publish

Use this API to start publishing a service. On successful completion, service's status can be marked as Publish.

```python
def start_publish(self,
                 account_name,
                 service_name,
                 version,
                 correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | service Name eg:any sub string of serviceName<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of service  which is to be published.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementRes`](../../doc/models/service-management-res.md)

## Example Usage

```python
account_name = 'AccountName0'
service_name = 'serviceName8'
version = 'version4'

result = service_management_controller.start_publish(account_name, service_name, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| Default | unexpected error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Stop Service Testing

Use this API to start service certification process. On successful completion of this process, service's status will  change to certified.

```python
def stop_service_testing(self,
                        account_name,
                        service_name,
                        version,
                        correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | service Name eg:any sub string of serviceName<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of service  which is to be certified.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementRes`](../../doc/models/service-management-res.md)

## Example Usage

```python
account_name = 'AccountName0'
service_name = 'serviceName8'
version = 'version4'

result = service_management_controller.stop_service_testing(account_name, service_name, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| Default | unexpected error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Ready to Public Use

Use this API to start the process to change a service's status to "Ready to Use". On success, service's status will be changed to "Ready to Use". Only a ready to use service can be deployed in production environment

```python
def ready_to_public_use(self,
                       account_name,
                       service_name,
                       version,
                       correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | service Name eg:any sub string of serviceName<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `version` | `string` | Template, Required | Version of the service  which is already certified and is ready for public use.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`ServiceManagementRes`](../../doc/models/service-management-res.md)

## Example Usage

```python
account_name = 'AccountName0'
service_name = 'serviceName8'
version = 'version4'

result = service_management_controller.ready_to_public_use(account_name, service_name, version)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| Default | unexpected error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

