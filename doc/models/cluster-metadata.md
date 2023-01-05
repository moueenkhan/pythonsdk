
# Cluster Metadata

## Structure

`ClusterMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | name of the cluster to be used<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `description` | `string` | Optional | Description of the cluster<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-\s]{1,500}$` |
| `cluster_type` | [`ClusterTypeEnum`](../../doc/models/cluster-type-enum.md) | Optional | - |
| `cloud` | [`Cloud`](../../doc/models/cloud.md) | Optional | - |
| `data_center` | [`DataCenter`](../../doc/models/data-center.md) | Optional | - |
| `labels` | [`List of Params`](../../doc/models/params.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `ingress_ips` | [`IngressIps`](../../doc/models/ingress-ips.md) | Optional | - |
| `upgrade_protection` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "name": null,
  "description": null,
  "clusterType": null,
  "cloud": null,
  "dataCenter": null,
  "labels": null,
  "ingressIps": null,
  "upgradeProtection": null
}
```

