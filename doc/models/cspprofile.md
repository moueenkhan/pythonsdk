
# Cspprofile

The user can create cloud credentials used for deploying workloads to the CSP environment.

## Structure

`Cspprofile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | System generated unique identifier to identify the CSP Profile uniquely.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `usage` | `long\|int` | Optional | Usage tells how many services are using the CSP Profile. Only CSP Profile with 0 usage count be allowed to delete.<br>**Constraints**: `>= 0`, `<= 1024` |
| `csp_profile_name` | `string` | Required | Name of the cloud credential to uniquely identify the CSP.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `customer_id` | `string` | Optional | Unique identification of the organization creating the CSP Profile.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `project_name` | `string` | Optional | Project name where service artifacts needs to be stored.<br>**Constraints**: *Maximum Length*: `63`, *Pattern*: `^[a-z0-9-.]+$` |
| `mtype` | [`CspProfileTypeEnum`](../../doc/models/csp-profile-type-enum.md) | Optional | Type of CspProfile<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `aws_csp_profile` | [`AwsCspProfile`](../../doc/models/aws-csp-profile.md) | Optional | Information related to manage resources in AWS infrastructure. |
| `azure_csp_profile` | [`AzureCspProfile`](../../doc/models/azure-csp-profile.md) | Optional | Information related to manage resources in Azure infrastructure. |
| `default_location` | [`DefaultLocation`](../../doc/models/default-location.md) | Optional | Default location where service needs to be deployed. |
| `verification_time_stamp` | `datetime` | Optional | Auto Derived Time of creation. Part of response only |
| `state` | `string` | Optional | state of the csp profile<br>**Constraints**: *Maximum Length*: `20`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `is_validated` | `bool` | Optional | True if CSP is validated using provided credential, false otherwise.<br>**Default**: `False` |
| `created_date` | `datetime` | Optional | Auto Derived Time of creation. Part of response only |
| `last_modified_date` | `datetime` | Optional | Last modified time. Part of response only |
| `created_by` | `string` | Optional | User who created the dropDown. Part of response only<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `last_modified_by` | `string` | Optional | User who last modified the dropDown. Part of response only<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |

## Example (as JSON)

```json
{
  "cspProfileName": "acme-aws-outpost"
}
```

