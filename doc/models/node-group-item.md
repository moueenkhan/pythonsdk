
# Node Group Item

## Structure

`NodeGroupItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `organization_id` | `string` | Optional | - |
| `partner_id` | `string` | Optional | - |
| `instance_type` | `string` | Optional | - |
| `edge_id` | `string` | Optional | - |
| `id` | `string` | Optional | - |
| `provision_id` | `string` | Optional | - |
| `node_type` | `string` | Optional | - |
| `nodes` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `nodes_min` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `nodes_max` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `node_volume_size` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `node_volume_type` | `string` | Optional | - |
| `node_private_networking` | `bool` | Optional | - |
| `node_zones` | `List of string` | Optional | **Constraints**: *Maximum Items*: `100` |
| `node_ami_family` | `string` | Optional | - |
| `node_labels` | [`NodeLabels`](../../doc/models/node-labels.md) | Optional | - |
| `nodegroup_type` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `enable_asg_access` | `bool` | Optional | - |
| `enable_full_access_to_ecr` | `bool` | Optional | - |
| `version_info_id` | `string` | Optional | - |
| `upgrade_info_id` | `string` | Optional | - |
| `tags` | [`NodeGroupItemTags`](../../doc/models/node-group-item-tags.md) | Optional | - |
| `config_file_content` | `string` | Optional | - |
| `provision` | [`Provision`](../../doc/models/provision.md) | Optional | - |
| `version_info` | [`VersionInfo`](../../doc/models/version-info.md) | Optional | - |
| `upgrade_info` | [`UpgradeInfo`](../../doc/models/upgrade-info.md) | Optional | - |

## Example (as JSON)

```json
{
  "name": null,
  "created_at": null,
  "modified_at": null,
  "organization_id": null,
  "partner_id": null,
  "instance_type": null,
  "edge_id": null,
  "id": null,
  "provision_id": null,
  "node_type": null,
  "nodes": null,
  "nodes_min": null,
  "nodes_max": null,
  "node_volume_size": null,
  "node_volume_type": null,
  "node_private_networking": null,
  "node_zones": null,
  "node_ami_family": null,
  "node_labels": null,
  "nodegroup_type": null,
  "enable_asg_access": null,
  "enable_full_access_to_ecr": null,
  "version_info_id": null,
  "upgrade_info_id": null,
  "tags": null,
  "config_file_content": null,
  "provision": null,
  "version_info": null,
  "upgrade_info": null
}
```

