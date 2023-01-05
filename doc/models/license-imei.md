
# License IMEI

IMEIs of the devices to assign or remove licenses

## Structure

`LicenseIMEI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Account name |
| `device_list` | `List of string` | Required | device IMEI list |

## Example (as JSON)

```json
{
  "deviceList": [
    "990003425730524",
    "990000473475967"
  ]
}
```

