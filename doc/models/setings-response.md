
# Setings Response

Settings for Anomaly Detection.

## Structure

`SetingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Indicates if the account name used has Anomaly Detection.<br />Success - The account has Anomaly Detection<br />Failure - The account does not have Anomaly Detection |
| `sensitivity_parameter` | [`List of Parameters`](../../doc/models/parameters.md) | Optional | The initial values and monitoring state for abnormal and very abnormal.<br>**Constraints**: *Maximum Items*: `10` |
| `status` | `string` | Optional | Indicates if Anomaly Detection is active on the account<br />Active - Anomaly Detection is active<br />Disabled- Anomaly Detection is not active |

## Example (as JSON)

```json
{
  "accountName": null,
  "sensitivityParameter": null,
  "status": null
}
```

