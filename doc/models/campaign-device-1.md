
# Campaign Device 1

Campaign history

## Structure

`CampaignDevice1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_device` | `int` | Optional | Total device count |
| `has_more_data` | `bool` | Required | Has more report flag |
| `last_seen_device_id` | `string` | Optional | Device identifier |
| `max_page_size` | `int` | Required | Maximum page size |
| `device_list` | [`List of DeviceStatus1`](../../doc/models/device-status-1.md) | Required | List of devices with id in IMEI |

## Example (as JSON)

```json
{
  "totalDevice": null,
  "hasMoreData": false,
  "lastSeenDeviceId": null,
  "maxPageSize": 94,
  "deviceList": [
    {
      "deviceId": "deviceId6",
      "status": "status2",
      "resultReason": null,
      "updatedTime": null,
      "recentAttemptTime": null,
      "nextAttemptTime": null
    },
    {
      "deviceId": "deviceId7",
      "status": "status1",
      "resultReason": null,
      "updatedTime": null,
      "recentAttemptTime": null,
      "nextAttemptTime": null
    }
  ]
}
```

