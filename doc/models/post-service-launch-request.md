
# Post Service Launch Request

## Structure

`PostServiceLaunchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | name of the received request<br>**Constraints**: *Maximum Length*: `50`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `service_name` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `csp_profile_id` | `string` | Required | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `service_profile_id` | `string` | Required | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `service_version` | `string` | Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^(.*)$` |

## Example (as JSON)

```json
{
  "name": "name0",
  "serviceName": null,
  "cspProfileId": "cspProfileId2",
  "serviceProfileId": "serviceProfileId2",
  "serviceVersion": null
}
```

