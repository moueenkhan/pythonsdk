# Repository

```python
repository_controller = client.repository
```

## Class Name

`RepositoryController`

## Methods

* [Get Repository List](../../doc/controllers/repository.md#get-repository-list)
* [Create Repository](../../doc/controllers/repository.md#create-repository)
* [Delete Repository](../../doc/controllers/repository.md#delete-repository)


# Get Repository List

GET All Repository  in the platform

```python
def get_repository_list(self,
                       account_name,
                       correlation_id=None,
                       mtype=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `mtype` | `string` | Query, Optional | Repository Type<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`List of Repository1`](../../doc/models/repository-1.md)

## Example Usage

```python
account_name = 'AccountName0'

result = repository_controller.get_repository_list(account_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Create Repository

Create a repository with in user's organziation

```python
def create_repository(self,
                     account_name,
                     body,
                     correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`Repository1`](../../doc/models/repository-1.md) | Body, Required | body |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`Repository1`](../../doc/models/repository-1.md)

## Example Usage

```python
account_name = 'AccountName0'
body = Repository1()
body.name = 'myRepo'

result = repository_controller.create_repository(account_name, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |


# Delete Repository

Delete the Repository

```python
def delete_repository(self,
                     account_name,
                     repository_name,
                     correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository_name` | `string` | Template, Required | Name of the repository which is about to be deleted.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`DeleteResponse`](../../doc/models/delete-response.md)

## Example Usage

```python
account_name = 'AccountName0'
repository_name = 'repositoryName4'

result = repository_controller.delete_repository(account_name, repository_name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

