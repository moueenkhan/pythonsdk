
# Status

## Structure

`Status`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | `string` | Optional | - |
| `conditions` | [`List of StatusConditionItem`](../../doc/models/status-condition-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `node_info` | [`StatusNodeInfo`](../../doc/models/status-node-info.md) | Optional | - |
| `capacity` | [`StatusCapacity`](../../doc/models/status-capacity.md) | Optional | - |
| `allocatable` | [`StatusAllocatable`](../../doc/models/status-allocatable.md) | Optional | - |
| `allocated` | [`StatusAllocated`](../../doc/models/status-allocated.md) | Optional | - |
| `ips` | [`List of Ip`](../../doc/models/ip.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "state": null,
  "conditions": null,
  "nodeInfo": null,
  "capacity": null,
  "allocatable": null,
  "allocated": null,
  "ips": null
}
```

