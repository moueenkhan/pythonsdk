# Claims

```python
claims_controller = client.claims
```

## Class Name

`ClaimsController`

## Methods

* [Get Service Claims](../../doc/controllers/claims.md#get-service-claims)
* [Associate Cloud Credential With Service Claim](../../doc/controllers/claims.md#associate-cloud-credential-with-service-claim)
* [Mark Service Claim Status Completed](../../doc/controllers/claims.md#mark-service-claim-status-completed)
* [Update Service Claim Status](../../doc/controllers/claims.md#update-service-claim-status)


# Get Service Claims

Use this API to fetch all service's claim(s) associated with a service. Service claims are generated based on service's compatibility with different cloud service provider.

```python
def get_service_claims(self,
                      account_name,
                      service_id,
                      correlation_id=None,
                      claim_status=None,
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
| `service_id` | `string` | Template, Required | Auto Generated Id of the claim whose information needs to be fetched.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `claim_status` | `string` | Query, Optional | queries with claim status on the claims<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `q` | `string` | Query, Optional | Use the comma (,) character to separate multiple values,eg claimType=Public MEC:claims.sandBoxState=NOT_STARTED,STARTED<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `limit` | `long\|int` | Query, Optional | number of items to return<br>**Constraints**: `>= 0`, `<= 1024` |
| `off_set` | `long\|int` | Query, Optional | Id of the last respose value in the previous list<br>**Constraints**: `>= 0`, `<= 1024` |
| `sort_key` | `string` | Query, Optional | Sorts the response by an attribute. Default is created_at<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `sort_dir` | [`SortDirectionEnum`](../../doc/models/sort-direction-enum.md) | Query, Optional | Sorts the response. Use asc for ascending or desc for descending order. The default is desc.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `details_flag` | `bool` | Query, Optional | Default as true. If it is true then it will return all details.<br>**Default**: `True` |

## Response Type

[`GetAllClaimsRes`](../../doc/models/get-all-claims-res.md)

## Example Usage

```python
account_name = 'AccountName0'
service_id = 'serviceId6'
details_flag = True

result = claims_controller.get_service_claims(account_name, service_id, None, None, None, None, None, None, None, details_flag)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Associate Cloud Credential With Service Claim

Associate an existing cloud credential with a service's claim which will be used to connect to user's cloud provider

```python
def associate_cloud_credential_with_service_claim(self,
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
| `service_id` | `string` | Template, Required | ServiceId System generated unique identifier which user is using.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `claim_id` | `string` | Template, Required | ClaimId System generated unique identifier which user is using.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `body` | [`CspProfileIdRequest`](../../doc/models/csp-profile-id-request.md) | Body, Required | body |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`CSPResponse`](../../doc/models/csp-response.md)

## Example Usage

```python
account_name = 'AccountName0'
service_id = 'serviceId6'
claim_id = 'claimId8'
body = CspProfileIdRequest()

result = claims_controller.associate_cloud_credential_with_service_claim(account_name, service_id, claim_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not Found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Mark Service Claim Status Completed

Use this API to mark a servic's claim status as complete post successful verification of sandbox testing in the respective sandbox environment.

```python
def mark_service_claim_status_completed(self,
                                       account_name,
                                       service_id,
                                       claim_id,
                                       correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_id` | `string` | Template, Required | ServiceId System generated unique identifier which user is using.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `claim_id` | `string` | Template, Required | ClaimId System generated unique identifier which user is using.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

`void`

## Example Usage

```python
account_name = 'AccountName0'
service_id = 'serviceId6'
claim_id = 'claimId8'

result = claims_controller.mark_service_claim_status_completed(account_name, service_id, claim_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not Found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Update Service Claim Status

Using this API user can update service's claim status as complete/verified etc.

```python
def update_service_claim_status(self,
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
| `service_id` | `string` | Template, Required | ServiceId System generated unique identifier which user is using.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `claim_id` | `string` | Template, Required | ClaimId System generated unique identifier which user is using.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[A-Za-z0-9_-]+$` |
| `body` | [`ClaimStatus1`](../../doc/models/claim-status-1.md) | Body, Required | body |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

`void`

## Example Usage

```python
account_name = 'AccountName0'
service_id = 'serviceId6'
claim_id = 'claimId8'
body = ClaimStatus1()

result = claims_controller.update_service_claim_status(account_name, service_id, claim_id, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not Found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

