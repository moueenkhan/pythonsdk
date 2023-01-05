
# Create Trigger 3

Trigger Information

## Structure

`CreateTrigger3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `string` | Optional | Trigger ID |
| `trigger_name` | `string` | Optional | Trigger Name |
| `trigger_category` | `string` | Optional | UsageAnomaly - This is the value to use in the request body to detect anomalous behaivior. The values in this table will only be relevant when this parameter is set to this value. |
| `account_name` | `string` | Optional | Account name<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `anomaly_trigger_request` | [`TriggerRequestarray`](../../doc/models/trigger-requestarray.md) | Optional | The details of the UsageAnomaly trigger. |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | The notification details of the trigger. |

## Example (as JSON)

```json
{
  "triggerId": null,
  "triggerName": null,
  "triggerCategory": null,
  "accountName": null,
  "anomalyTriggerRequest": null,
  "notification": null
}
```

