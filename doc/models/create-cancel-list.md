
# Create Cancel List

License cancellation candidate devices

## Structure

`CreateCancelList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `string` | Optional | List creation option |
| `count` | `int` | Optional | the number of devices |
| `device_list` | `List of string` | Required | device IMEI list |

## Example (as JSON)

```json
{
  "type": "append",
  "count": 2,
  "deviceList": [
    "990003425730535",
    "990000473475989"
  ]
}
```

