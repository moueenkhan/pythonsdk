
# Response Error Exception

## Structure

`ResponseErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Z]{2,5}_[0-9]{3}_[0-9]{3}$` |
| `message` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `remedy_message` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |

## Example (as JSON)

```json
{
  "code": null,
  "message": null,
  "remedyMessage": null
}
```

