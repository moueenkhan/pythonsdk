# Category

```python
category_controller = client.category
```

## Class Name

`CategoryController`


# Create Category

Create a new category with in user's organization

```python
def create_category(self,
                   account_name,
                   body,
                   correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`List of Category`](../../doc/models/category.md) | Body, Required | body<br>**Constraints**: *Maximum Items*: `10000` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`List of Category`](../../doc/models/category.md)

## Example Usage

```python
account_name = 'AccountName0'
body = []

body.append(Category())
body[0].category_name = 'Video Camera Monitoring'

body.append(Category())
body[1].category_name = 'Video Camera Monitoring'


result = category_controller.create_category(account_name, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

