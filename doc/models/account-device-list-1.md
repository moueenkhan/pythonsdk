
# Account Device List 1

Array of devices.

## Structure

`AccountDeviceList1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | Account name |
| `has_more_data` | `bool` | Required | has more device flag |
| `last_seen_device_id` | `string` | Optional | Last seen device identifier |
| `max_page_size` | `int` | Required | Maximum page size |
| `device_list` | [`List of AccountDevice1`](../../doc/models/account-device-1.md) | Required | Account device list |

## Example (as JSON)

```json
{
  "accountName": null,
  "hasMoreData": null,
  "maxPageSize": null,
  "deviceList": {
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
}
```

