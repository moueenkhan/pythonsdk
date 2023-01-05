
# Device Firmware Upgrade

Firmware upgrades information.

## Structure

`DeviceFirmwareUpgrade`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device identifier |
| `campaign_id` | `string` | Required | Campaign identifier |
| `account_name` | `string` | Required | Account identifier |
| `firmware_name` | `string` | Optional | Firmware name |
| `firmware_from` | `string` | Optional | Old firmware version |
| `firmware_to` | `string` | Optional | New firmware version |
| `start_date` | `date` | Required | Firmware upgrade start date |
| `status` | `string` | Required | Firmware upgrade status |
| `reason` | `string` | Required | Software upgrade result reason |
| `report_updated_time` | `string` | Optional | Report updated time |

## Example (as JSON)

```json
{
  "deviceId": "deviceId0",
  "campaignId": "campaignId0",
  "accountName": "accountName4",
  "firmwareName": null,
  "firmwareFrom": null,
  "firmwareTo": null,
  "startDate": "2016-03-13",
  "status": "status8",
  "reason": "reason4",
  "reportUpdatedTime": null
}
```

