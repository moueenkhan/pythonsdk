
# Create Cancel List Response

List of created license cancellation devices

## Structure

`CreateCancelListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Required | the number of devices |
| `device_list` | `List of string` | Required | device IMEI list |

## Example (as JSON)

```json
{
  "count": 2,
  "deviceList": [
    "990003425730535",
    "990000473475989"
  ]
}
```

