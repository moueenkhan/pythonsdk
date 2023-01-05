
# Device Firmware Version

Device and firmware information.

## Structure

`DeviceFirmwareVersion`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Optional | result |
| `reason` | `string` | Optional | result reason |
| `device_id` | `string` | Required | Device IMEI |
| `firmware_version` | `string` | Required | Device Firmware Version |
| `firmware_version_update_time` | `datetime` | Optional | Firmware Version Update Time |

## Example (as JSON)

```json
{
  "status": null,
  "reason": null,
  "deviceId": "deviceId0",
  "firmwareVersion": "firmwareVersion2",
  "firmwareVersionUpdateTime": null
}
```

