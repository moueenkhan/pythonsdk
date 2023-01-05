
# Get MEC Platforms Response

Response to return the optimal 5G Edge platforms for deployment based on a region, service profile of the service that you want to deploy or user equipment.

## Structure

`GetMECPlatformsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mec_platforms` | [`List of ResourcesMecplatform`](../../doc/models/resources-mecplatform.md) | Optional | A list of optimal MEC Platforms where you can register your deployed application.<br>**Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "MECPlatforms": null
}
```

