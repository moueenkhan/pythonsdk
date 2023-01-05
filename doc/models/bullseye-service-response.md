
# Bullseye Service Response

Status of Hyper Precise Location on the device.

## Structure

`BullseyeServiceResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Optional | The account the device belongs to. |
| `device_list` | [`List of DeviceServiceResponse`](../../doc/models/device-service-response.md) | Optional | List of devices. |
| `response_type` | [`ApiResponseCode`](../../doc/models/api-response-code.md) | Optional | ResponseCode and/or a message indicating success or failure of the request. |

## Example (as JSON)

```json
{
  "accountNumber": null,
  "deviceList": null,
  "responseType": null
}
```

