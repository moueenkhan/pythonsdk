
# Operations Wf

operationsWf attribute of a service.

## Structure

`OperationsWf`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_type` | [`EventTypeEnum`](../../doc/models/event-type-enum.md) | Optional | Workflow event type. Ex: BACKUP, RESTORE, MOVE, SUSPEND, STOP, AUTOSCALE, DEPRECATE.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `upload_type` | [`WorkloadUploadTypeEnum`](../../doc/models/workload-upload-type-enum.md) | Optional | Allowed values are: GIT files (PULL_FROM_REPO), MANUAL_UPLOAD.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_id` | `string` | Optional | Repository ID of an existing repository.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository` | [`Repository1`](../../doc/models/repository-1.md) | Optional | Users can create a repository to maintain service artifacts. Repository would be either a Git or HELM repository. |
| `source_code_type` | [`SourceCodeTypeEnum`](../../doc/models/source-code-type-enum.md) | Optional | source code type can be JAVA or GO.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `revision_type` | [`RevisionTypeEnum`](../../doc/models/revision-type-enum.md) | Optional | Revision type can be a BRANCH or TAG.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `name` | `string` | Optional | branch or tag name<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `path` | `string` | Optional | The workflow path.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |

## Example (as JSON)

```json
{
  "eventType": null,
  "uploadType": null,
  "repositoryId": null,
  "repository": null,
  "sourceCodeType": null,
  "revisionType": null,
  "name": null,
  "path": null
}
```

