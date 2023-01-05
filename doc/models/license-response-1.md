
# License Response 1

License assignment/removal response.

## Structure

`LicenseResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | Account name |
| `lic_total_count` | `int` | Required | Total license count |
| `lic_used_count` | `int` | Required | Assigned license count |
| `device_list` | [`List of DeviceStatus1`](../../doc/models/device-status-1.md) | Required | List of devices with id in IMEI |

## Example (as JSON)

```json
{
  "accountName": "accountName4",
  "licTotalCount": 72,
  "licUsedCount": 68,
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

