
# Get All Claims Res

Response to get all claims.

## Structure

`GetAllClaimsRes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | Count for all the claims returned after hitting the API.<br>**Constraints**: `<= 20480` |
| `claims_res_list` | [`List of Claims`](../../doc/models/claims.md) | Optional | List of all claims.<br>**Constraints**: *Maximum Items*: `2048` |

## Example (as JSON)

```json
{
  "count": null,
  "claimsResList": null
}
```

