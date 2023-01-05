
# Cluster Config

## Structure

`ClusterConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tags` | [`Params`](../../doc/models/params.md) | Optional | - |
| `end_point_access_type` | [`ClusterConfigEndpPointAccessTypeEnum`](../../doc/models/cluster-config-endp-point-access-type-enum.md) | Optional | **Default**: `'privateAccess'` |
| `auto_create_network_infra` | `bool` | Optional | **Default**: `True` |
| `infra_i_pv_4_range` | `string` | Optional | **Default**: `'192.168.0.0/16'` |
| `network_nat_mode` | [`NetworkNatModeEnum`](../../doc/models/network-nat-mode-enum.md) | Optional | **Default**: `'single'` |
| `availability_zones` | [`List of ListString`](../../doc/models/list-string.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `private_network_infra_ids` | [`List of ListString`](../../doc/models/list-string.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `public_network_infra_ids` | [`List of ListString`](../../doc/models/list-string.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "tags": null,
  "endPointAccessType": null,
  "autoCreateNetworkInfra": null,
  "infraIPv4range": null,
  "networkNatMode": null,
  "availabilityZones": null,
  "privateNetworkInfraIds": null,
  "publicNetworkInfraIds": null
}
```

