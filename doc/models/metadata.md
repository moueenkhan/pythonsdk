
# Metadata

## Structure

`Metadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | - |
| `display_name` | `string` | Optional | - |
| `created_at` | `string` | Optional | - |
| `modified_at` | `string` | Optional | - |
| `labels` | [`MetadataLabels`](../../doc/models/metadata-labels.md) | Optional | - |
| `annotations` | [`MetadataAnnotations`](../../doc/models/metadata-annotations.md) | Optional | - |
| `organization_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `partner_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `project_id` | `int` | Optional | **Constraints**: `>= 0`, `<= 1024` |
| `id` | `string` | Optional | - |

## Example (as JSON)

```json
{
  "name": null,
  "displayName": null,
  "createdAt": null,
  "modifiedAt": null,
  "labels": null,
  "annotations": null,
  "organizationID": null,
  "partnerID": null,
  "projectID": null,
  "id": null
}
```

