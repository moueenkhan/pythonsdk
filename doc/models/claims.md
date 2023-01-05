
# Claims

Users would provide CSP compatibility during service creation, which are nothing but declaring service compatibility with different cloud service providers like AWS or Azure. This API would help users to fetch all  service claims using which user can initiate sandbox testing of the service.

## Structure

`Claims`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Optional | Auto Generated Id.<br>**Constraints**: *Maximum Length*: `200`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `name` | `string` | Optional | Name of the claim.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `claim_status` | [`ClaimStatusEnum`](../../doc/models/claim-status-enum.md) | Optional | Current status of the claim can have only two values eg: VERIFIED/UNVERIFIED. |
| `sand_box_state` | [`StateOfSandboxEnum`](../../doc/models/state-of-sandbox-enum.md) | Optional | State of sandbox can have value like - STARTED, NOT_STARTED, STOPPED, PAUSED, COMPLETED, DELETED, STOP_IN_PROGRESS, PAUSE_IN_PROGRESS, TEST_IN_PROGRESS, MARK_FOR_DELETEION. |
| `sand_box_status` | [`StatusOfSandboxEnum`](../../doc/models/status-of-sandbox-enum.md) | Optional | Status of sandbox can have value like - NA, INPROGRESS, SUCCESS, FAILED. |
| `environment` | `string` | Optional | Claim environment in which it is deployed eg: AWS Public Cloud.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\- _]+$` |
| `claim_type` | [`ClaimTypeEnum`](../../doc/models/claim-type-enum.md) | Optional | Claim type can have values like - PUBLIC_MEC, PRIVATE_MEC. |
| `start_time_stamp` | `datetime` | Optional | Start time when the claim got introduced. |
| `service_instance_id` | `string` | Optional | Auto Generated Id of the service instance.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `csp_profile_id` | `string` | Optional | CSP Profile ID in which service will be deployed.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `service_id` | `string` | Optional | Auto Generated Id of the service which is to be deployed.<br>**Constraints**: *Maximum Length*: `36`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `end_time_stamp` | `datetime` | Optional | End time when the claim got introduced. |
| `created_date` | `datetime` | Optional | Auto Derived Time of creation. Part of response only |
| `last_modified_date` | `datetime` | Optional | Last modified time. Part of response only |
| `created_by` | `string` | Optional | User who created the dropDown. Part of response only<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `last_modified_by` | `string` | Optional | User who last modified the dropDown. Part of response only<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |

## Example (as JSON)

```json
{
  "name": null,
  "sandBoxState": null,
  "sandBoxStatus": null,
  "cspProfileId": null
}
```

