
# Error Response 1

ErrorResponse attribute of a service.

## Structure

`ErrorResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Optional | Code of the error. eg: SDMS_000_000<br>**Constraints**: *Maximum Length*: `12`, *Pattern*: `^[A-Z0-9_]+$` |
| `message` | `string` | Optional | Brief description of the error in the form of a message.<br>**Constraints**: *Maximum Length*: `200`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `remedy_message` | `string` | Optional | Suggestion on how to fix the issue.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "code": null,
  "message": null,
  "remedyMessage": null
}
```

