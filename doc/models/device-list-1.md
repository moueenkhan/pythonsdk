
# Device List 1

## Structure

`DeviceList1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | [`List of DeviceId1`](../../doc/models/device-id-1.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `ip_address` | `string` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9].[0-9].[0-9].[0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "deviceIds": null,
  "ipAddress": null
}
```

