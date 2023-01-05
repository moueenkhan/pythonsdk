# Tags

```python
tags_controller = client.tags
```

## Class Name

`TagsController`


# Create Tag

Create a new Tag with in user's organization.

```python
def create_tag(self,
              account_name,
              body,
              correlation_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `body` | [`List of Tag`](../../doc/models/tag.md) | Body, Required | body<br>**Constraints**: *Maximum Items*: `10000` |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |

## Response Type

[`List of Tag`](../../doc/models/tag.md)

## Example Usage

```python
account_name = 'AccountName0'
body = []

body.append(Tag())
body[0].key = 'Mytag'

body.append(Tag())
body[1].key = 'Mytag'


result = tags_controller.create_tag(account_name, body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 415 | Unsupported media type | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

