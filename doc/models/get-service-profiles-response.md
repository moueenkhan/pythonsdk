
# Get Service Profiles Response

Response on successful retrieval of service profiles.

## Structure

`GetServiceProfilesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Optional | HTTP status code.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `data` | `List of string` | Optional | A comma delimited list of all the service profiles registered under your API key<br>**Constraints**: *Maximum Items*: `100`, *Maximum Length*: `32` |

## Example (as JSON)

```json
{
  "status": null,
  "data": null
}
```

