
# Add or Remove Device Resp

Add or remove devices from the existing software upgrade information.

## Structure

`AddOrRemoveDeviceResp`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Required | Account identifier |
| `campaign_id` | `string` | Required | Campaign identifier |
| `request_id` | `string` | Required | Request identifier |

## Example (as JSON)

```json
{
  "accountName": "0402196254-00001",
  "campaignId": "60b5d639-ccdc-4db8-8824-069bd94c95bf",
  "requestId": null
}
```

