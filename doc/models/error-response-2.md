
# Error Response 2

Error Response

## Structure

`ErrorResponse2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | [`ErrorCodeEnum`](../../doc/models/error-code-enum.md) | Required | Error Code. Available values: INVALID_ACCESS, INVALID_PARAMETER, INTERNAL_ERROR, SUCCESS |
| `error_message` | `string` | Required | Error Message |

## Example (as JSON)

```json
{
  "errorCode": "INVALID_ACCESS",
  "errorMessage": "errorMessage8"
}
```

