
# SMS Send Request

Request to send SMS.

## Structure

`SMSSendRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The name of a billing account. |
| `custom_fields` | [`List of KvPair`](../../doc/models/kv-pair.md) | Optional | The names and values of custom fields, if you want to only include devices that have matching custom fields. |
| `data_encoding` | `string` | Optional | The SMS message encoding, which can be 7-bit (default), 8-bit-ASCII, 8-bit-UTF-8, 8-bit-DATA. |
| `device_ids` | [`List of DeviceId`](../../doc/models/device-id.md) | Optional | The devices that you want to send the message to, specified by device identifier. |
| `group_name` | `string` | Optional | The name of a device group, if you want to send the SMS message to all devices in the device group. |
| `service_plan` | `string` | Optional | The name of a service plan, if you want to only include devices that have that service plan. |
| `sms_message` | `string` | Optional | The contents of the SMS message. The SMS message is limited to 160 characters in 7-bit format, or 140 characters in 8-bit format. |

## Example (as JSON)

```json
{
  "servicePlan": "T Plan 2",
  "smsMessage": "The rain in Spain stays mainly in the plain."
}
```

