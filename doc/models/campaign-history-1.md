
# Campaign History 1

Campaign history.

## Structure

`CampaignHistory1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Required | Has more report flag |
| `last_seen_campaign_id` | `string` | Optional | Campaign identifier |
| `campaign_list` | [`List of CampaignMetaInfo1`](../../doc/models/campaign-meta-info-1.md) | Required | Firmware upgrade list |

## Example (as JSON)

```json
{
  "hasMoreData": false,
  "lastSeenCampaignId": null,
  "campaignList": [
    {
      "accountName": "accountName6",
      "id": "id2",
      "campaignName": null,
      "firmwareName": null,
      "firmwareFrom": null,
      "firmwareTo": null,
      "protocol": null,
      "make": "make8",
      "model": "model0",
      "startDate": "2016-03-13",
      "endDate": "2016-03-13",
      "campaignTimeWindowList": null,
      "status": "status6"
    }
  ]
}
```

