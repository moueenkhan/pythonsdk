
# Campaign Firmware Upgrade

Firmware upgrade for devices.

## Structure

`CampaignFirmwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `campaign_name` | `string` | Optional | Campaign name |
| `firmware_name` | `string` | Required | Firmware name to upgrade to |
| `firmware_from` | `string` | Required | Old firmware version |
| `firmware_to` | `string` | Required | New firmware version |
| `protocol` | `string` | Required | Valid values include: LWM2M, OMA and HTTP.<br>**Default**: `'LWM2M'` |
| `start_date` | `date` | Required | Campaign start date |
| `end_date` | `date` | Required | Campaign end date |
| `campaign_time_window_list` | [`List of TimeWindow`](../../doc/models/time-window.md) | Optional | List of allowed campaign time windows |
| `device_list` | `List of string` | Required | device IMEI list |

## Example (as JSON)

```json
{
  "firmwareName": null,
  "firmwareFrom": null,
  "firmwareTo": null,
  "protocol": "LWM2M",
  "startDate": null,
  "endDate": null,
  "deviceList": null
}
```

