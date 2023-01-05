
# Change Campaign Dates Request 1

Campaign dates and time windows.

## Structure

`ChangeCampaignDatesRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `date` | Required | Campaign start date |
| `end_date` | `date` | Required | Campaign end date |
| `campaign_time_window_list` | [`List of TimeWindow`](../../doc/models/time-window.md) | Optional | List of allowed campaign time windows |

## Example (as JSON)

```json
{
  "startDate": "2016-03-13",
  "endDate": "2016-03-13",
  "campaignTimeWindowList": null
}
```

