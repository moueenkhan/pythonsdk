
# Cancellation Candidate Create Response

List of licenses assigned

## Structure

`CancellationCandidateCreateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `count` | `int` | Optional | The total number of devices on the cancellation candidate list. |
| `device_list` | `List of string` | Optional | The IMEIs of the devices. |

## Example (as JSON)

```json
{
  "count": 2,
  "deviceList": [
    "900000000000001",
    "900000000000999"
  ]
}
```

