
# Deployment Location

## Structure

`DeploymentLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ern` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `cluster` | [`DeploymentLocationCluster`](../../doc/models/deployment-location-cluster.md) | Optional | - |
| `namespace` | [`Namespace`](../../doc/models/namespace.md) | Optional | - |

## Example (as JSON)

```json
{
  "ern": null,
  "cluster": null,
  "namespace": null
}
```

