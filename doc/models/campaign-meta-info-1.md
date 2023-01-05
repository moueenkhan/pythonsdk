
# Campaign Meta Info 1

Campaign and campaign details.

## Structure

`CampaignMetaInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | Account identifier |
| `id` | `string` | Required | Campaign identifier |
| `campaign_name` | `string` | Optional | Campaign name |
| `firmware_name` | `string` | Optional | firmware name |
| `firmware_from` | `string` | Optional | Old firmware version |
| `firmware_to` | `string` | Optional | New software version |
| `protocol` | [`CampaignMetaInfoProtocolEnum`](../../doc/models/campaign-meta-info-protocol-enum.md) | Optional | Firmware protocol. Valid values include: LWM2M, OMD-DM.<br>**Default**: `'LWM2M'` |
| `make` | `string` | Required | Device make |
| `model` | `string` | Required | Device model |
| `start_date` | `date` | Required | Campaign start date |
| `end_date` | `date` | Required | Campaign end date |
| `campaign_time_window_list` | [`List of TimeWindow`](../../doc/models/time-window.md) | Optional | List of allowed campaign time windows |
| `status` | `string` | Required | Firmware upgrade status |

## Example (as JSON)

```json
{
  "accountName": "accountName4",
  "id": "id0",
  "campaignName": null,
  "firmwareName": null,
  "firmwareFrom": null,
  "firmwareTo": null,
  "protocol": null,
  "make": "make0",
  "model": "model2",
  "startDate": "2016-03-13",
  "endDate": "2016-03-13",
  "campaignTimeWindowList": null,
  "status": "status8"
}
```

