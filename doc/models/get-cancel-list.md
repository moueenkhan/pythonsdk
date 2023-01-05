
# Get Cancel List

A list of license cancellation candidate devices

## Structure

`GetCancelList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Required | Cancellation candidate devices count |
| `has_more_data` | `bool` | Required | flag to indicat more devices |
| `update_time` | `string` | Required | Last update time |
| `device_list` | `List of string` | Required | device IMEI list |

## Example (as JSON)

```json
{
  "count": 6,
  "hasMoreData": false,
  "updateTime": "2018-03-22 00:06:00.069 +0000 UTC",
  "deviceList": [
    "990003425730535",
    "990000473475989",
    "990005733420535",
    "990000347475989",
    "990007303425535",
    "990007590473489"
  ]
}
```

