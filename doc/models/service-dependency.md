
# Service Dependency

Dependency of the service.

## Structure

`ServiceDependency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rank` | `int` | Optional | The dependency rank.<br>**Constraints**: `<= 2048` |
| `mtype` | [`ServiceTypeEnum`](../../doc/models/service-type-enum.md) | Optional | Service Type. Ex: Installation, Operations, Custom.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `service_name` | `string` | Optional | Name of the dependent service<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Optional | Version of the service being used.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `package_type` | [`PackageTypeEnum`](../../doc/models/package-type-enum.md) | Optional | deployment package type<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |

## Example (as JSON)

```json
{
  "rank": null,
  "type": null,
  "serviceName": null,
  "version": null,
  "packageType": null
}
```

