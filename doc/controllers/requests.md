# Requests

Get the status of asynchronous reqeusts.

```python
requests_controller = client.requests
```

## Class Name

`RequestsController`


# Get Request Status Using GET

Returns the current status of an asynchronous request that was made for a single device.

```python
def get_request_status_using_get(self,
                                aname,
                                request_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |
| `request_id` | `string` | Template, Required | UUID from synchronous response |

## Response Type

[`RequestStatusResponse`](../../doc/models/request-status-response.md)

## Example Usage

```python
aname = '0252012345-00001'
request_id = '86c83330-4bf5-4235-9c4e-a83f93aeae4c'

result = requests_controller.get_request_status_using_get(aname, request_id)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "86c83330-4bf5-4235-9c4e-a83f93aeae4c",
  "status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

