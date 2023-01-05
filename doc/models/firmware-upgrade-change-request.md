
# Firmware Upgrade Change Request

List of devices to add or remove.

## Structure

`FirmwareUpgradeChangeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`FirmwareTypeEnumListEnum`](../../doc/models/firmware-type-enum-list-enum.md) | Required | append or remove |
| `device_list` | `List of string` | Required | The IMEIs of the devices. |

## Example (as JSON)

```json
{
  "type": "append",
  "deviceList": [
    "15-digit IMEI",
    "15-digit IMEI"
  ]
}
```

