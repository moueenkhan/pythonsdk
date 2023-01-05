
# Campaign

Firmware upgrade information.

## Structure

`Campaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | Upgrade identifier |
| `account_name` | `string` | Required | Account identifier |
| `campaign_name` | `string` | Optional | Campaign name |
| `firmware_name` | `string` | Optional | firmware name |
| `firmware_from` | `string` | Optional | Old firmware version |
| `firmware_to` | `string` | Optional | New firmware version |
| `protocol` | `string` | Required | The protocol of the firmware distribution. Default: LWM2M<br>**Default**: `'LWM2M'` |
| `make` | `string` | Required | Applicable make |
| `model` | `string` | Required | Applicable model |
| `start_date` | `date` | Required | Campaign start date |
| `end_date` | `date` | Required | Campaign end date |
| `campaign_time_window_list` | [`List of TimeWindow`](../../doc/models/time-window.md) | Optional | List of allowed campaign time windows |
| `status` | `string` | Required | Firmware upgrade status |

## Example (as JSON)

```json
{
  "id": null,
  "accountName": null,
  "protocol": "LWM2M",
  "make": null,
  "model": null,
  "startDate": null,
  "endDate": null,
  "status": null
}
```

