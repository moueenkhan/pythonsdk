
# Service Delete Response

Response to delete a service.

## Structure

`ServiceDeleteResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `selected_service` | [`SelectedService`](../../doc/models/selected-service.md) | Optional | Service which is selected. |
| `dependent_service` | [`List of DependentService`](../../doc/models/dependent-service.md) | Optional | List of dependent services.<br>**Constraints**: *Maximum Items*: `2048` |
| `running_instances` | [`List of RunningInstance`](../../doc/models/running-instance.md) | Optional | List of running Instance.<br>**Constraints**: *Maximum Items*: `2048` |
| `error_details` | [`ErrorResponse1`](../../doc/models/error-response-1.md) | Optional | ErrorResponse attribute of a service. |

## Example (as JSON)

```json
{
  "selectedService": null,
  "dependentService": null,
  "runningInstances": null,
  "errorDetails": null
}
```

