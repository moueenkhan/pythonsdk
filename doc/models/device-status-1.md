
# Device Status 1

Device status

## Structure

`DeviceStatus1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device IMEI |
| `status` | `string` | Required | Success or failure |
| `result_reason` | `string` | Optional | Result reason |
| `updated_time` | `datetime` | Optional | Updated Time |
| `recent_attempt_time` | `datetime` | Optional | the most recent attempt Time |
| `next_attempt_time` | `datetime` | Optional | next attempt Time |

## Example (as JSON)

```json
{
  "deviceId": "deviceId0",
  "status": "status8",
  "resultReason": null,
  "updatedTime": null,
  "recentAttemptTime": null,
  "nextAttemptTime": null
}
```

