
# Placement Intents

## Structure

`PlacementIntents`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_placement_at_launch_enabled` | `bool` | Optional | **Default**: `False` |
| `group_id` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `intent_chain` | [`List of IntentChainItem`](../../doc/models/intent-chain-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "isPlacementAtLaunchEnabled": null,
  "groupId": null,
  "intentChain": null
}
```

