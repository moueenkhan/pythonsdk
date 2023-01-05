
# Cloud

## Structure

`Cloud`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `provider` | [`CloudProviderEnum`](../../doc/models/cloud-provider-enum.md) | Optional | Cloud provider where you plan to provision and operate your Kubernetes cluster |
| `distribution` | [`CloudDestributionEnum`](../../doc/models/cloud-destribution-enum.md) | Optional | Supported Kubernetes distribution for the selected cloud provider |
| `common_config` | [`CommonConfig`](../../doc/models/common-config.md) | Optional | - |
| `cluster_config` | [`ClusterConfig`](../../doc/models/cluster-config.md) | Optional | - |
| `node_config` | [`NodeConfig`](../../doc/models/node-config.md) | Optional | - |
| `node_configs` | [`List of NodeConfig`](../../doc/models/node-config.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `advance_config` | [`AdvanceConfig`](../../doc/models/advance-config.md) | Optional | - |

## Example (as JSON)

```json
{
  "provider": null,
  "distribution": null,
  "commonConfig": null,
  "clusterConfig": null,
  "nodeConfig": null,
  "nodeConfigs": null,
  "advanceConfig": null
}
```

