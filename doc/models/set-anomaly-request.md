
# Set Anomaly Request

Anomaly detection request.

## Structure

`SetAnomalyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | The name of a billing account. An account name is usually numeric, and must include any leading zeros.<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32` |
| `request_type` | `string` | Optional | The type of request being made. anomaly is the request to activate Anomaly Detection. |
| `sensitivity_parameter` | [`List of Parameters`](../../doc/models/parameters.md) | Optional | The initial values and monitoring state for abnormal and very abnormal.<br>**Constraints**: *Maximum Items*: `10` |

## Example (as JSON)

```json
{
  "accountName": null,
  "requestType": null,
  "sensitivityParameter": null
}
```

