
# Boundary

Deployment boundary of a service.

## Structure

`Boundary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `csp` | [`CspEnum`](../../doc/models/csp-enum.md) | Optional | Cloud service provider ex: AWS_PUBLIC_CLOUD, AWS_WL, AWS_OUTPOST, AZURE_EDGE, AZURE_PUBLIC_CLOUD.<br>**Default**: `'AWS_WL'` |
| `region` | `string` | Optional | Boundary region ex: US East (Ohio)<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `zone_id` | `List of string` | Optional | Zones listed under a specific region<br>**Constraints**: *Maximum Items*: `10000`, *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "csp": null,
  "region": null,
  "zoneId": null
}
```

