
# Csp Profile Res List

Response to csp profile list.

## Structure

`CspProfileResList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | Total number of records available.<br>**Constraints**: `<= 1024` |
| `csp_profile_list` | [`List of Cspprofile`](../../doc/models/cspprofile.md) | Optional | List of all available CSP profile available with in the user’s organization.<br>**Constraints**: *Maximum Items*: `2048` |

## Example (as JSON)

```json
{
  "count": null,
  "cspProfileList": null
}
```

