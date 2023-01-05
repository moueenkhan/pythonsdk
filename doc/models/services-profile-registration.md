
# Services Profile Registration

## Structure

`ServicesProfileRegistration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | Provide Service Profile Id |
| `name` | `string` | Optional | Provide name for Service Profile<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `service_name` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `service_version` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `current_version` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `version` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Optional | - |
| `customer_id` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `created_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `created_at` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `last_updated_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `last_updated_at` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |
| `linked_service_instances` | [`List of LinkedServiceInstance`](../../doc/models/linked-service-instance.md) | Optional | - |
| `access_intents` | [`AccessIntents`](../../doc/models/access-intents.md) | Optional | - |
| `placement_intents` | [`PlacementIntents`](../../doc/models/placement-intents.md) | Optional | - |
| `deployment_locations` | [`List of DeploymentLocation`](../../doc/models/deployment-location.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "serviceName": null,
  "serviceVersion": null,
  "currentVersion": null,
  "version": null,
  "state": null,
  "customerID": null,
  "createdBy": null,
  "createdAt": null,
  "lastUpdatedBy": null,
  "lastUpdatedAt": null,
  "linkedServiceInstances": null,
  "accessIntents": null,
  "placementIntents": null,
  "deploymentLocations": null
}
```

