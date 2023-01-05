
# Delete Devices Response Message

Response Message to Delete Device.

## Structure

`DeleteDevicesResponseMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_ids` | `object` | Optional | One object per device to be deleted. Each object must contain a kind and id element identifying the device. |
| `status` | `string` | Optional | “Success” if the device was deleted, or “Failed” if there was a problem. |
| `message` | `string` | Optional | Not present if status=Success. One of these messages if status=Failed:The device is not in deactivate state.The user does not have access to delete the device. |

## Example (as JSON)

```json
{
  "deviceIds": [
    {
      "id": "09005470263",
      "kind": "esn"
    }
  ],
  "status": "Success"
}
```

