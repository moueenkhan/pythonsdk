
# Account Device

Account device information

## Structure

`AccountDevice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device identifier |
| `mdn` | `string` | Required | MDN |
| `model` | `string` | Required | Device model |
| `make` | `string` | Required | Device make |
| `fota_eligible` | `bool` | Required | Device fota capable |
| `app_fota_eligible` | `bool` | Required | Device application fota capable |
| `license_assigned` | `bool` | Required | License assigned device |
| `distribution_type` | `string` | Required | LWM2M, OMD-DM or HTTP |
| `software_list` | [`List of SoftwareInfo`](../../doc/models/software-info.md) | Required | List of sofware |
| `create_time` | `datetime` | Optional | The date and time of when the device is created. |
| `upgrade_time` | `datetime` | Optional | The date and time of when the device firmware or software is upgraded. |
| `update_time` | `datetime` | Optional | The date and time of when the device is updated. |
| `refresh_time` | `datetime` | Optional | The date and time of when the device is refreshed. |

## Example (as JSON)

```json
{
  "deviceId": "15-digit IMEI",
  "mdn": "10-digit MDN",
  "model": "Model-A",
  "make": "Verizon",
  "fotaEligible": true,
  "appFotaEligible": true,
  "licenseAssigned": true,
  "distributionType": "HTTP",
  "softwareList": [
    {
      "name": "FOTA_Verizon_Model-A_02To03_HF",
      "version": "3",
      "upgradeTime": "2020-09-08T19:00:51.541Z"
    }
  ],
  "createTime": "2020-09-08T19:00:51.541Z",
  "upgradeTime": "2020-09-08T19:00:51.541Z",
  "updateTime": "2020-09-08T19:00:51.541Z",
  "refreshTime": "2020-09-08T19:00:51.541Z"
}
```

