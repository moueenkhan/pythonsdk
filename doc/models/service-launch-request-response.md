
# Service Launch Request Response

## Structure

`ServiceLaunchRequestResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `service_name` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `state` | [`ServiceLaunchStatEnum`](../../doc/models/service-launch-stat-enum.md) | Optional | **Constraints**: *Maximum Length*: `60`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `service_version` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `service_id` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `service_profile_id` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `csp_profile_id` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |
| `config_files` | [`List of ConfigFileItem`](../../doc/models/config-file-item.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `linked_service_instances` | [`List of LinkedServiceInstance`](../../doc/models/linked-service-instance.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `updated_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^(.*)$` |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "serviceName": null,
  "state": null,
  "serviceVersion": null,
  "serviceId": null,
  "serviceProfileId": null,
  "cspProfileId": null,
  "configFiles": null,
  "linkedServiceInstances": null,
  "updatedAt": null,
  "updatedBy": null
}
```

