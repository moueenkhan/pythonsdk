
# Add or Remove Device Resp 1

Add or remove devices to existing upgrade information.

## Structure

`AddOrRemoveDeviceResp1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | Account identifier |
| `campaign_id` | `string` | Required | Campaign identifier |
| `device_list` | [`List of DeviceListItem`](../../doc/models/device-list-item.md) | Required | Array of devices changed. |

## Example (as JSON)

```json
{
  "accountName": null,
  "campaignId": null,
  "deviceList": {
    "deviceId": "900000000000001",
    "status": "LicenseAssignSuccess",
    "Reason": "Success"
  }
}
```

