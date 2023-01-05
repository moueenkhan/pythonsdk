
# Running Instance

Running instance of a service.

## Structure

`RunningInstance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `instance_name` | `string` | Optional | ServiceInstanceName<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `instance_id` | `string` | Optional | ServiceInstanceID<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `csp` | `string` | Optional | ServiceInstanceName<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `status` | [`Status1Enum`](../../doc/models/status-1-enum.md) | Optional | Can have any value as - DRAFT_INPROGRESS, DRAFT_COMPLETE, DESIGN_INPROGRESS, DESIGN_FAILED, DESIGN_COMPLETED, VALIDATION_INPROGRESS,  VALIDATION_FAILED, VALIDATION_COMPLETED, TESTING_INPROGRESS, TESTING_FAILED, TESTING_COMPLETED, READY_TO_USE_INPROGRESS, READY_TO_USE_FAILED, READY_TO_USE_COMPLETED, READY_TO_PRIVATE_USE_INPROGRESS, READY_TO_PRIVATE_USE_FAILED, READY_TO_PRIVATE_USE_COMPLETED,  PUBLISH_INPROGRESS,  PUBLISH_FAILED,  PUBLISH_COMPLETED,  CERTIFY_INPROGRESS,  CERTIFY_FAILED, CERTIFY_COMPLETED, DEPRECATE_INPROGRESS,  DEPRECATE_FAILED, DEPRECATE_COMPLETED, MARKDELETE_INPROGRESS, MARKDELETE_FAILED, MARKDELETE_COMPLETED. |

## Example (as JSON)

```json
{
  "instanceName": null,
  "instanceID": null,
  "CSP": null
}
```

