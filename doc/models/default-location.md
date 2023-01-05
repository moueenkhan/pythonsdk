
# Default Location

Default location where service needs to be deployed.

## Structure

`DefaultLocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region` | `string` | Optional | CSP region where service needs to be deployed.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `zone` | `string` | Optional | Zone with in a region where service needs to be deployed.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "region": null,
  "zone": null
}
```

