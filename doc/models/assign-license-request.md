
# Assign License Request

## Structure

`AssignLicenseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `devices` | [`List of DeviceList1`](../../doc/models/device-list-1.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `sku_number` | `string` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "accountName": null,
  "devices": null,
  "skuNumber": null
}
```

