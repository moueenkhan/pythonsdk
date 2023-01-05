
# Repository 1

Users can create a repository to maintain service artifacts. Repository would be either a Git or HELM repository.

## Structure

`Repository1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | System generated unique identifier to identify repository uniquely.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `name` | `string` | Required | Name of the repository to be created.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `description` | `string` | Optional | Description of the repository being created.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |
| `mtype` | [`RepositoryTypeEnum`](../../doc/models/repository-type-enum-1.md) | Optional | Type for the repository which can be Git or Helm.<br>**Constraints**: *Maximum Length*: `20` |
| `tag` | `string` | Optional | Attribute which can be used to tag a repository.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s\/]+$` |
| `endpoint` | `string` | Optional | Endpoint URL for the repository from where resources needs to be fetched.<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s\/]+$` |
| `reacheability` | [`ReacheabilityEnum`](../../doc/models/reacheability-enum.md) | Optional | Reachability can be of two types, Internet and Private Network. |
| `ca_certificate` | `string` | Optional | Required if your repository uses a private certificate authencation.Please provide ur CA certificat in PEM format.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `agents` | `List of string` | Optional | This attribute can be used to specify GITOps Agent to fetch details from private repository.<br>**Constraints**: *Maximum Items*: `10000`, *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `ssl_disabled` | `bool` | Optional | Boolean value to check the SSL certification. |
| `is_validated` | `bool` | Optional | True if CSP is validated using provided credential, false otherwise.<br>**Default**: `False` |
| `validation_status` | `string` | Optional | Status when the repository is validated eg: CREDENTIAL_VALIDATION_SUCCESS.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `credentials_type` | [`CredentialsTypeEnum`](../../doc/models/credentials-type-enum.md) | Optional | credentialsType can be of two types, UserPassCredentials and SSHCredentials. |
| `credentials` | [`Credentials1`](../../doc/models/credentials-1.md) | Optional | Credentials of a repository. |
| `ssh_key` | `string` | Optional | SSH Private Key in PEM format<br>**Constraints**: *Maximum Length*: `10000`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `last_validated_date` | `datetime` | Optional | Time when the repository was validated. |
| `created_date` | `datetime` | Optional | Date when the repository was created. |
| `last_modified_date` | `datetime` | Optional | Date when the repository was updated. |
| `created_by` | `string` | Optional | User information by whom the repository was created.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `updated_by` | `string` | Optional | User information by whom the repository was updated.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `is_deleted` | `bool` | Optional | When it will be soft deleted, status will be changed<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "name": "myRepo"
}
```

