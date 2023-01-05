
# Subscription 2

## Structure

`Subscription2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `extended_attributes` | [`List of KvPair1`](../../doc/models/kv-pair-1.md) | Optional | **Constraints**: *Maximum Items*: `5` |
| `license_assigned` | `int` | Optional | **Constraints**: `>= 0`, `<= 10` |
| `license_available` | `int` | Optional | **Constraints**: `>= 0`, `<= 10` |
| `license_purchased` | `int` | Optional | **Constraints**: `>= 0`, `<= 10` |
| `license_type` | `string` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `sku_number` | `string` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "extendedAttributes": null,
  "licenseAssigned": null,
  "licenseAvailable": null,
  "licensePurchased": null,
  "licenseType": null,
  "skuNumber": null
}
```

