
# Callback Registration Request 1

Callback endpoint information

## Structure

`CallbackRegistrationRequest1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `string` | Required | The name of the callback service that you want to subscribe to, which must be 'Fota' for Software Management Services callbacks. |
| `url` | `string` | Required | The address on your server where you have enabled a listening service for Software Management Services callback messages. |
| `username` | `string` | Optional | The user name that ThingSpace should return in the callback messages. |
| `password` | `string` | Optional | The password that ThingSpace should return in the callback messages. |

## Example (as JSON)

```json
{
  "name": "Fota",
  "url": "https://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

