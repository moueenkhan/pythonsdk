
# Device Filter Without Account

Filter for devices without account.

## Structure

`DeviceFilterWithoutAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `group_name` | `string` | Optional | Only include devices that are in this device group. |
| `service_plan` | `string` | Optional | Only include devices that have this service plan. |
| `custom_fields` | [`List of KvPair`](../../doc/models/kv-pair.md) | Optional | Custom field names and values, if you want to only include devices that have matching values. |

## Example (as JSON)

```json
{
  "groupName": "suspended devices"
}
```

