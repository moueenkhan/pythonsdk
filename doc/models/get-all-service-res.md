
# Get All Service Res

Response to get all services.

## Structure

`GetAllServiceRes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_records` | `int` | Optional | Will display the total number of records fetched.<br>**Constraints**: `<= 20480` |
| `service_res_list` | [`List of Service`](../../doc/models/service.md) | Optional | Response to fetch all services.<br>**Constraints**: *Maximum Items*: `2048` |

## Example (as JSON)

```json
{
  "totalRecords": null,
  "serviceResList": null
}
```

