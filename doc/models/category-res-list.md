
# Category Res List

Response to get category list.

## Structure

`CategoryResList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `categories` | `List of string` | Optional | Can be any name just to define it under a category.<br>**Constraints**: *Maximum Items*: `10000`, *Minimum Length*: `1`, *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9?$@#()\[\]'!,+\-=_:.&*%\s]+$` |

## Example (as JSON)

```json
{
  "categories": null
}
```

