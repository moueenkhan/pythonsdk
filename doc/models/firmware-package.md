
# Firmware Package

Available firmware.

## Structure

`FirmwarePackage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `firmware_name` | `string` | Required | Firmware name |
| `firmware_from` | `string` | Required | Firmware from version |
| `firmware_to` | `string` | Required | Firmware to version |
| `launch_date` | `datetime` | Required | Firmware launch date |
| `release_note` | `string` | Required | Firmware release note |
| `model` | `string` | Required | Firmware applicable device model |
| `make` | `string` | Required | Firmware applicable device make |
| `protocol` | [`CampaignMetaInfoProtocolEnum`](../../doc/models/campaign-meta-info-protocol-enum.md) | Required | Firmware protocol. Valid values include: LWM2M, OMD-DM.<br>**Default**: `'LWM2M'` |

## Example (as JSON)

```json
{
  "firmwareName": null,
  "firmwareFrom": null,
  "firmwareTo": null,
  "launchDate": null,
  "releaseNote": null,
  "model": null,
  "make": null,
  "protocol": "LWM2M"
}
```

