
# Common Config

## Structure

`CommonConfig`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `cloud_credentials` | [`CloudCredentials`](../../doc/models/cloud-credentials.md) | Optional | - |
| `k_8_s_version` | [`K8sVersionEnum`](../../doc/models/k8-s-version-enum.md) | Optional | Version of K8s platform<br>**Default**: `'1.18'` |
| `blueprint` | [`Blueprint`](../../doc/models/blueprint.md) | Optional | - |

## Example (as JSON)

```json
{
  "cloudCredentials": null,
  "k8sVersion": null,
  "blueprint": null
}
```

