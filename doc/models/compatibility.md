
# Compatibility

Compatibility would have the attribute csp which is Cloud service provider ex: AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE, AZURE_PUBLIC_CLOUD.

## Structure

`Compatibility`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `csp` | [`CspEnum`](../../doc/models/csp-enum.md) | Optional | Cloud service provider ex: AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE, AZURE_PUBLIC_CLOUD.<br>**Default**: `'AWS_WL'` |

## Example (as JSON)

```json
{
  "csp": null
}
```

