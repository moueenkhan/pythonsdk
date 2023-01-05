
# Credentials 1

Credentials of a repository.

## Structure

`Credentials1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Optional | User name to connect to the repository.<br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `40`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |
| `password` | `string` | Optional | Account password to connect to user provided repository.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,^+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "name": null,
  "password": null
}
```

