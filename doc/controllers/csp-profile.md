# CSP Profile

```python
csp_profile_controller = client.csp_profile
```

## Class Name

`CSPProfileController`

## Methods

* [Fetch Cloud Credential Details](../../doc/controllers/csp-profile.md#fetch-cloud-credential-details)
* [Create Cloud Credential](../../doc/controllers/csp-profile.md#create-cloud-credential)
* [Remove Cloud Credential](../../doc/controllers/csp-profile.md#remove-cloud-credential)


# Fetch Cloud Credential Details

Fetch available cloud credentials with in user's organization

```python
def fetch_cloud_credential_details(self,
                                  account_name,
                                  correlation_id=None,
                                  q=None,
                                  limit=None,
                                  off_set=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `q` | `string` | Query, Optional | Use the coloumn (:) character to separate multiple query params eg type=AWS:awsCspProfile.credType=ACCESS_KEY,ROLE_ARN:state=UNVERIFIED,VERIFIED<br>**Constraints**: *Maximum Length*: `2048`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!\/,+\-=_:.&*%\s]+$` |
| `limit` | `long\|int` | Query, Optional | number of items to return<br>**Constraints**: `>= 0`, `<= 1024` |
| `off_set` | `long\|int` | Query, Optional | Id of the last respose value in the previous list<br>**Constraints**: `>= 0`, `<= 1024` |

## Response Type

[`CspProfileResList`](../../doc/models/csp-profile-res-list.md)

## Example Usage

```python
account_name = 'AccountName0'

result = csp_profile_controller.fetch_cloud_credential_details(account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 403 | Forbidden | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 429 | Too many requests | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| Default | Forbidden | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Create Cloud Credential

Create a new cloud credential with in user's organization

```python
def create_cloud_credential(self,
                           account_name,
                           body,
                           correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`Cspprofile`](../../doc/models/cspprofile.md) | Body, Required | body |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`Cspprofile`](../../doc/models/cspprofile.md)

## Example Usage

```python
account_name = 'AccountName0'
body = Cspprofile()
body.csp_profile_name = 'acme-aws-outpost'

result = csp_profile_controller.create_cloud_credential(account_name, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 403 | Forbidden | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 429 | too many requests | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| Default | Forbidden | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Remove Cloud Credential

Remove a cloud credential from user's organization

```python
def remove_cloud_credential(self,
                           account_name,
                           id,
                           correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `id` | `string` | Template, Required | Csp Profile Id |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`DeleteResponse`](../../doc/models/delete-response.md)

## Example Usage

```python
account_name = 'AccountName0'
id = 'id0'

result = csp_profile_controller.remove_cloud_credential(account_name, id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

