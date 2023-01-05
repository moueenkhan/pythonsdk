
# Resource

Resource of the service.

## Structure

`Resource`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `compute_resources` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `gpu_required` | `bool` | Optional | GPU required or not for onboarding service<br>**Default**: `False` |
| `gpu` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `storage` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `memory` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `latency` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `request_rate` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |
| `bandwidth` | [`ResourceBase`](../../doc/models/resource-base.md) | Optional | Resource Base of the service. |

## Example (as JSON)

```json
{
  "computeResources": null,
  "gpuRequired": null,
  "gpu": null,
  "storage": null,
  "memory": null,
  "latency": null,
  "requestRate": null,
  "bandwidth": null
}
```

