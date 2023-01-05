
# Callback Registration Response

## Structure

`CallbackRegistrationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Optional | The name of the account that registered the callback URL |
| `name` | [`CallbackServiceNameEnum`](../../doc/models/callback-service-name-enum.md) | Optional | The name of the callback service. |

## Example (as JSON)

```json
{
  "accountName": "0212312345-00001",
  "serviceName": "Location"
}
```

