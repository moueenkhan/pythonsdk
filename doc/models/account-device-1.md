
# Account Device 1

Device information.

## Structure

`AccountDevice1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device identifier |
| `mdn` | `string` | Required | MDN |
| `model` | `string` | Required | Device model |
| `make` | `string` | Required | Device make |
| `firmware` | `string` | Required | Device firmware version |
| `fota_eligible` | `string` | Required | Device fota capable LWM2M, OMD-DM, HTTP or NONE |
| `status` | `string` | Required | Device status |
| `license_assigned` | `bool` | Required | License assigned device |
| `protocol` | [`DevicesProtocolEnum`](../../doc/models/devices-protocol-enum.md) | Required | Firmware protocol. Valid values include: LWM2M, OMADM, HTTP.<br>**Default**: `'LWM2M'` |
| `software_list` | [`List of SoftwareInfo`](../../doc/models/software-info.md) | Required | List of sofware |
| `file_list` | [`List of SoftwareInfo`](../../doc/models/software-info.md) | Optional | List of files |
| `create_time` | `datetime` | Optional | The date and time of when the device is created |
| `upgrade_time` | `datetime` | Optional | The date and time of when the device firmware or software is updated |
| `update_time` | `datetime` | Optional | The date and time of when the device is updated |
| `refresh_time` | `datetime` | Optional | The date and time of when the device is refreshed |

## Example (as JSON)

```json
{
  "deviceId": null,
  "mdn": null,
  "model": null,
  "make": null,
  "firmware": null,
  "fotaEligible": null,
  "status": null,
  "licenseAssigned": null,
  "protocol": "LWM2M",
  "softwareList": {
    "name": "FOTA_Verizon_Model-A_02To03_HF",
    "version": "3",
    "upgradeTime": "2020-09-08T19:00:51.541Z"
  }
}
```

