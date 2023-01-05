
# Resource Base

Resource Base of the service.

## Structure

`ResourceBase`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `unit` | `string` | Optional | Resource unit ex :MB.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]!,+\-=_:.&*%\s]+$` |
| `value` | `long\|int` | Optional | Resource value  ex: 200MB.<br>**Constraints**: `>= 0`, `<= 1024` |
| `max` | `long\|int` | Optional | Resource max value ex: 400MB.<br>**Constraints**: `>= 0`, `<= 1024` |
| `min` | `long\|int` | Optional | Resource min value ex: 10MB.<br>**Constraints**: `>= 0`, `<= 1024` |

## Example (as JSON)

```json
{
  "unit": null,
  "value": null,
  "max": null,
  "min": null
}
```

