
# Workload 1

workload attribute of a service.

## Structure

`Workload1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | The Auto Generated Id of the workload.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `name` | `string` | Required | Name of the workload needs to be deployed<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `description` | `string` | Optional | A brief workload description.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `package_type` | [`PackageTypeEnum`](../../doc/models/package-type-enum.md) | Optional | deployment package type<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `upload_type` | [`WorkloadUploadTypeEnum`](../../doc/models/workload-upload-type-enum.md) | Optional | Allowed values are: GIT files (PULL_FROM_REPO), MANUAL_UPLOAD.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_type` | [`RepositoryTypeEnum`](../../doc/models/repository-type-enum.md) | Optional | Repository types allowed: GIT/HELM.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `repository_id` | `string` | Optional | In case of ‘Pull files from my repository’, The user can provide the existing repositoryID<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `repository` | [`Repository1`](../../doc/models/repository-1.md) | Optional | Users can create a repository to maintain service artifacts. Repository would be either a Git or HELM repository. |
| `files` | `List of string` | Optional | Files which are being generated.<br>**Constraints**: *Maximum Items*: `10000`, *Maximum Length*: `10000`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `revision_type` | [`RevisionTypeEnum`](../../doc/models/revision-type-enum.md) | Optional | Allowed values for revision type are BRANCH or TAG.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `helm_git_branch` | [`HelmGitBranch1`](../../doc/models/helm-git-branch-1.md) | Optional | helmGitBranch would have branchName, helmChartPath, and valuesYAMLPaths attributes. |
| `helm_git_tag` | [`HelmGitTag1`](../../doc/models/helm-git-tag-1.md) | Optional | helmGitTag would have tagName, helmChartPath, and valuesYAMLPaths attributes. |
| `helm_yaml_git_tag` | [`HelmYamlGitTag1`](../../doc/models/helm-yaml-git-tag-1.md) | Optional | helmYamlGitTag would have tagName and valuesYAMLPaths attributes. |
| `helm_helmrepo` | [`HelmHelmrepo`](../../doc/models/helm-helmrepo.md) | Optional | helmHelmrepo would have HelmChartName and HelmChartVersion. |
| `yaml_git_branch` | [`YamlGitBranch1`](../../doc/models/yaml-git-branch-1.md) | Optional | yamlGitBranch would have branchName and valuesYAMLPaths attributes. |
| `terraform_git_branch` | [`TerraformGitBranch1`](../../doc/models/terraform-git-branch-1.md) | Optional | - |
| `terraform_git_tag` | [`TerraformGitTag1`](../../doc/models/terraform-git-tag-1.md) | Optional | - |
| `created_date` | `datetime` | Optional | The date on which the workload is created. |
| `last_modified_dte` | `datetime` | Optional | The date when the created workload was last modified. |
| `created_by` | `string` | Optional | Identity of the user who created the workload.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `updated_by` | `string` | Optional | Identity of the user who updated the workload.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "name": "MECSDWorkload"
}
```

