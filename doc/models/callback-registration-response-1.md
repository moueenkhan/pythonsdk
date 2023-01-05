
# Callback Registration Response 1

Registered callback account name and service name

## Structure

`CallbackRegistrationResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The name of the billing account for which callback messages will be sent. |
| `service_name` | `string` | Optional | The name of the callback service, which identifies the type and format of messages that will be sent to the registered URL. This will be 'Fota' for the Software Management Services callback. |

## Example (as JSON)

```json
{
  "accountName": "0204563412-00001",
  "serviceName": "Fota"
}
```

