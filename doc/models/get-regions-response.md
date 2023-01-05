
# Get Regions Response

Response to return an array of all regions in the Verizon 5G Edge service. You can use the region IDs from the response to find optimal Edge platforms or service endpoints.

## Structure

`GetRegionsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `regions` | [`List of Regions`](../../doc/models/regions.md) | Optional | An array of all regions in the Verizon 5G Edge service.<br>**Constraints**: *Maximum Items*: `100` |

## Example (as JSON)

```json
{
  "regions": null
}
```

