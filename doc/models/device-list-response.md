
# Device List Response

Device list information.

## Structure

`DeviceListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | Account name |
| `device_count` | `int` | Required | Total device count |
| `device_list` | [`List of DeviceListStatus`](../../doc/models/device-list-status.md) | Required | List of devices with id in IMEI<br>**Constraints**: *Maximum Items*: `1000` |

## Example (as JSON)

```json
{
  "accountName": "accountName4",
  "deviceCount": 236,
  "deviceList": [
    {
      "deviceId": "deviceId6",
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
    },
    {
      "deviceId": "deviceId7",
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
  ]
}
```

