
# Firmware Campaign

Firmware upgrade information.

## Structure

`FirmwareCampaign`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `string` | Required | Upgrade identifier |
| `account_name` | `string` | Required | Account identifier |
| `campaign_name` | `string` | Optional | Campaign name |
| `firmware_name` | `string` | Optional | Firmware name (for firmware upgrade only) |
| `firmware_from` | `string` | Required | Old firmware version (for firmware upgrade only) |
| `firmware_to` | `string` | Required | New firmware version (for firmware upgrade only) |
| `protocol` | `string` | Required | Available values: LWM2M<br>**Default**: `'LWM2M'` |
| `make` | `string` | Required | make |
| `model` | `string` | Required | model |
| `start_date` | `date` | Required | Campaign start date |
| `end_date` | `date` | Required | Campaign end date |
| `campaign_time_window_list` | [`List of TimeWindow`](../../doc/models/time-window.md) | Optional | List of allowed campaign time windows |
| `status` | `string` | Required | Campaign status |

## Example (as JSON)

```json
{
  "id": null,
  "accountName": null,
  "firmwareFrom": null,
  "firmwareTo": null,
  "protocol": "LWM2M",
  "make": null,
  "model": null,
  "startDate": null,
  "endDate": null,
  "status": null
}
```

