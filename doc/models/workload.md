
# Workload

## Structure

`Workload`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `name` | `string` | Required | Name of the workload needs to be deployed<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `description` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `package_type` | [`PackageTypeEnum`](../../doc/models/package-type-enum.md) | Optional | deployment package type<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `upload_type` | [`WorkloadUploadTypeEnum`](../../doc/models/workload-upload-type-enum.md) | Optional | **Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_type` | [`RepositoryTypeEnum`](../../doc/models/repository-type-enum.md) | Optional | **Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository` | [`Repository`](../../doc/models/repository.md) | Optional | - |
| `files` | `List of string` | Optional | **Constraints**: *Maximum Items*: `10000` |
| `revision_type` | [`RevisionTypeEnum`](../../doc/models/revision-type-enum.md) | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `helm_git_branch` | [`HelmGitBranch`](../../doc/models/helm-git-branch.md) | Optional | - |
| `helm_git_tag` | [`HelmGitTag`](../../doc/models/helm-git-tag.md) | Optional | - |
| `helm_yaml_git_tag` | [`HelmYamlGitTag`](../../doc/models/helm-yaml-git-tag.md) | Optional | - |
| `helm_repo` | [`HelmRepo`](../../doc/models/helm-repo.md) | Optional | - |
| `yaml_git_branch` | [`YamlGitBranch`](../../doc/models/yaml-git-branch.md) | Optional | - |
| `terraform_git_branch` | [`TerraformGitBranch`](../../doc/models/terraform-git-branch.md) | Optional | - |
| `terraform_git_tag` | [`TerraformGitTag`](../../doc/models/terraform-git-tag.md) | Optional | - |
| `created_date` | `datetime` | Optional | - |
| `last_modified_dte` | `datetime` | Optional | - |
| `created_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `updated_by` | `string` | Optional | **Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "name": "MECSDWorkload"
}
```

