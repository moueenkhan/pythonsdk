
# Deletea Subscription Request

The subscription to delete.

## Structure

`DeleteaSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountidentifier` | [`Accountidentifier`](../../doc/models/accountidentifier.md) | Optional | The ID of the authenticating billing account, in the format `{"billingaccountid":"1234567890-12345"}`. |
| `resourceidentifier` | [`ListString`](../../doc/models/list-string.md) | Optional | The ID of the target to delete, in the format {"id": "dd1682d3-2d80-cefc-f3ee-25154800beff"}. |

## Example (as JSON)

```json
{
  "accountidentifier": {
    "billingaccountid": "1223334444-00001"
  },
  "resourceidentifier": {
    "id": "f8b112df-739c-6236-f059-106c67bafd99"
  }
}
```

