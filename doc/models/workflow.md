
# Workflow

workflow attribute of a service.

## Structure

`Workflow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | The service version workflow name.<br>**Constraints**: *Maximum Length*: `63`, *Pattern*: `^[a-z0-9-_.]+$` |
| `version` | `string` | Required | The Service version workflow value.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `id` | `string` | Optional | auto generated uuid for each workdflow triggered<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `mtype` | [`WorkflowTypeEnum`](../../doc/models/workflow-type-enum.md) | Optional | Service Type. Ex: Installation, Operations, Custom.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `installation_wf` | [`InstallationWf`](../../doc/models/installation-wf.md) | Optional | installationWf attribute of a service. |
| `operations_wf` | [`OperationsWf`](../../doc/models/operations-wf.md) | Optional | operationsWf attribute of a service. |
| `custom_wf` | [`CustomWf`](../../doc/models/custom-wf.md) | Optional | customWf attribute of a service. |
| `files` | `List of string` | Optional | Files which are being generated.<br>**Constraints**: *Maximum Items*: `10000`, *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `status` | `string` | Optional | status of the workflow<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |
| `created_date` | `datetime` | Optional | The date on which the workflow is created. |
| `last_modified_date` | `datetime` | Optional | The date when the created workflow was last modified. |
| `created_by` | `string` | Optional | Identity of the user who created the workflow.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `updated_by` | `string` | Optional | Identity of the user who updated the workflow.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |

## Example (as JSON)

```json
{
  "name": "camera_add_on",
  "version": "1.0.0"
}
```

