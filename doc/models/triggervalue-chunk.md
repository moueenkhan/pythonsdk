
# Triggervalue Chunk

## Structure

`TriggervalueChunk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `string` | Optional | The system assigned name of the trigger being updated. |
| `trigger_name` | `string` | Optional | The user defined name of the trigger. |
| `organization_name` | `string` | Optional | The user assigned name of the organization associated with the trigger. |
| `trigger_category` | `string` | Optional | UsageAnomaly - This is the value to use in the request body to detect anomalous behaivior. The values in this table will only be relevant when this parameter is set to this value. |
| `trigger_attributes` | [`List of KeysChunk`](../../doc/models/keys-chunk.md) | Optional | Additional details and keys for the trigger. |
| `created_at` | `datetime` | Optional | Timestamp for whe the trigger was created. |
| `modified_at` | `datetime` | Optional | Timestamp for the most recent time the trigger was modified. |
| `anomalyattributes` | [`Anomalyattributes`](../../doc/models/anomalyattributes.md) | Optional | The details of the UsageAnomaly trigger. |
| `notification` | [`Notificationarray`](../../doc/models/notificationarray.md) | Optional | The notification details of the trigger. |

## Example (as JSON)

```json
{
  "triggerId": null,
  "triggerName": null,
  "organizationName": null,
  "triggerCategory": null,
  "triggerAttributes": null,
  "createdAt": null,
  "modifiedAt": null,
  "anomalyattributes": null,
  "notification": null
}
```

