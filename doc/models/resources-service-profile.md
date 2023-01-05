
# Resources Service Profile

Information about the resource requirements and service characteristics of an edge application. Includes serviceProfileId. Used when retrieving a service profile.

## Structure

`ResourcesServiceProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_profile_id` | `string` | Optional | Unique identifier for a service profile |
| `client_type` | [`ClientTypeEnum`](../../doc/models/client-type-enum.md) | Required | The category of application client. |
| `ecsp_filter` | `string` | Optional | identity of the preferred Edge Computing Service Provider<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `client_schedule` | `string` | Optional | The expected operation schedule of the application client (e.g. time windows)<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |
| `client_service_area` | `string` | Optional | The expected location(s) (e.g. route) of the hosting UE during the Client's operation schedule.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |
| `network_resources` | [`TypesNetworkResources`](../../doc/models/types-network-resources.md) | Optional | Network resources of a service profile |
| `compute_resources` | [`TypesComputeResources`](../../doc/models/types-compute-resources.md) | Optional | Compute resources of a service profile |
| `properties` | [`Properties`](../../doc/models/properties.md) | Optional | Additional service support information for the MEC platform. |

## Example (as JSON)

```json
{
  "serviceProfileId": null,
  "clientType": "IoT",
  "ecspFilter": null,
  "clientSchedule": null,
  "clientServiceArea": null,
  "networkResources": null,
  "computeResources": null,
  "properties": null
}
```

