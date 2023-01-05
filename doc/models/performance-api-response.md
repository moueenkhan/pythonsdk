
# Performance Api Response

Response to query the most recent data for Key Performance Indicators (KPIs) like network availability, MEC hostnames and more.

## Structure

`PerformanceApiResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_status` | `string` | Optional | Success or Failed |
| `start` | `string` | Optional | Timestamp of the query's start, format:mm/dd/yyyy,hr:min:sec |
| `end` | `string` | Optional | Timestamp of the query's end , format:mm/dd/yyyy, hr:min:sec |
| `query_result` | [`List of Result`](../../doc/models/result.md) | Optional | Result of the query to fetch the most recent data for Key Performance Indicators (KPIs) like network availability, MEC hostnames and more. |

## Example (as JSON)

```json
{
  "QueryStatus": "Success",
  "Start": "1/28/2021 12:00:00",
  "End": "1/28/2021 12:15:00",
  "QueryResult": [
    {
      "name": "NetworkAvailability",
      "data": [
        "100",
        "percent",
        "high"
      ]
    }
  ]
}
```

