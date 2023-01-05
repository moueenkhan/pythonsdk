
# Subscription Response 1

## Structure

`SubscriptionResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `subscription_list` | [`List of Subscription2`](../../doc/models/subscription-2.md) | Optional | **Constraints**: *Maximum Items*: `5` |

## Example (as JSON)

```json
{
  "accountName": null,
  "subscriptionList": null
}
```

