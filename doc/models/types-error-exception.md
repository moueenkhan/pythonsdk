
# Types Error Exception

Base type for all errors.

## Structure

`TypesErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Required | HTTP status code or status of response<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `message` | `string` | Required | Error details<br>**Constraints**: *Maximum Length*: `32` |
| `data` | [`Data1`](../../doc/models/data-1.md) | Required | For cases where user input exceeds the boundary values an additional 'data' key will be returned with a relevant description. |

## Example (as JSON)

```json
{
  "status": "status8",
  "message": "message0",
  "data": {
    "additionalMessage": null
  }
}
```

