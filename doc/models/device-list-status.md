
# Device List Status

Device information

## Structure

`DeviceListStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `string` | Required | Device IMEI |
| `request_status` | `string` | Optional | Success or failure |
| `result_reason` | `string` | Optional | Result reason |
| `mdn` | `string` | Optional | MDN |
| `model` | `string` | Optional | Device model |
| `make` | `string` | Optional | Device make |
| `firmware` | `string` | Optional | Device firmware version |
| `fota_eligible` | `string` | Optional | Device fota capable LWM2M, OMD-DM, HTTP or NONE |
| `status` | `string` | Optional | Device status |
| `license_assigned` | `bool` | Optional | License assigned device |
| `protocol` | [`DevicesProtocolEnum`](../../doc/models/devices-protocol-enum.md) | Optional | Firmware protocol. Valid values include: LWM2M, OMADM, HTTP.<br>**Default**: `'LWM2M'` |
| `software_list` | [`List of SoftwareInfo`](../../doc/models/software-info.md) | Optional | List of sofware<br>**Constraints**: *Maximum Items*: `1000` |
| `file_list` | [`List of SoftwareInfo`](../../doc/models/software-info.md) | Optional | List of files<br>**Constraints**: *Maximum Items*: `1000` |
| `create_time` | `datetime` | Optional | The date and time of when the device is created |
| `status_time` | `datetime` | Optional | The date and time of when the device firmware or software is updated |
| `update_time` | `datetime` | Optional | The date and time of when the device is updated |
| `refresh_time` | `datetime` | Optional | The date and time of when the device is refreshed |
| `last_connection_time` | `datetime` | Optional | The date and time of when the device reachability is checked |

## Example (as JSON)

```json
{
  "deviceId": "deviceId0",
  "requestStatus": null,
  "resultReason": null,
  "mdn": null,
  "model": null,
  "make": null,
  "firmware": null,
  "fotaEligible": null,
  "status": null,
  "licenseAssigned": null,
  "protocol": null,
  "softwareList": null,
  "fileList": null,
  "createTime": null,
  "statusTime": null,
  "updateTime": null,
  "refreshTime": null,
  "lastConnectionTime": null
}
```

