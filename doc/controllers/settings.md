# Settings

Choose what level and interval of alerting for anomalies detected.

```python
settings_controller = client.settings
```

## Class Name

`SettingsController`

## Methods

* [Get Diagnostics Settings](../../doc/controllers/settings.md#get-diagnostics-settings)
* [Set Anomaly Settings](../../doc/controllers/settings.md#set-anomaly-settings)
* [Get Anomaly Settings](../../doc/controllers/settings.md#get-anomaly-settings)
* [Reset Anomaly Settings](../../doc/controllers/settings.md#reset-anomaly-settings)


# Get Diagnostics Settings

This endpoint retrieves diagnostics settings synchronously

```python
def get_diagnostics_settings(self,
                            account_name,
                            devices)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | Account identifier |
| `devices` | `string` | Query, Required | Devices list format: [{"id":"{imei1}","kind":"imei"},{"id":"{imei2}","kind":"imei"}] |

## Response Type

[`List of Setting`](../../doc/models/setting.md)

## Example Usage

```python
account_name = '0000123456-00001'
devices = '[{"id":"864508030026238","kind":"IMEI"},{"id":"864508030026238","kind":"IMEI"}]'

result = settings_controller.get_diagnostics_settings(account_name, devices)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "string",
    "device": {
      "id": "864508030026238",
      "kind": "IMEI"
    },
    "attributes": [
      {
        "name": "MANUFACTURER",
        "value": "string",
        "createdOn": "2019-09-07T23:08:03.532Z",
        "isObservable": true,
        "isObserving": true,
        "frequency": {
          "value": 5,
          "unit": "SECOND"
        }
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`ErrorException`](../../doc/models/error-exception.md) |


# Set Anomaly Settings

Uses the subscribed account ID to activate Anomaly Detection and set threshold values.

```python
def set_anomaly_settings(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SetAnomalyRequest`](../../doc/models/set-anomaly-request.md) | Body, Required | Settings Request |

## Response Type

[`RequestResponse1`](../../doc/models/request-response-1.md)

## Example Usage

```python
body = SetAnomalyRequest()
body.account_name = '0000123456-00001'
body.request_type = 'anomaly'
body.sensitivity_parameter = []

body.sensitivity_parameter.append(Parameters())
body.sensitivity_parameter[0].abnormal_max_value = 1.1
body.sensitivity_parameter[0].enable_abnormal = True
body.sensitivity_parameter[0].enable_very_abnormal = True
body.sensitivity_parameter[0].very_abnormal_max_value = 0.55


result = settings_controller.set_anomaly_settings(body)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | All error responses will be in this format | [`RestErrorResponseError1Exception`](../../doc/models/rest-error-response-error-1-exception.md) |


# Get Anomaly Settings

Retrieves the current Anomnaly Detection settings for an account.

```python
def get_anomaly_settings(self,
                        account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Template, Required | The name of the subscribed account |

## Response Type

[`SetingsResponse`](../../doc/models/setings-response.md)

## Example Usage

```python
account_name = '0000123456-00001'

result = settings_controller.get_anomaly_settings(account_name)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "Success",
  "sensitivityParameter": [
    {
      "abnormalMaxValue": 1.1,
      "enableAbnormal": true,
      "enableVeryAbnormal": true,
      "veryAbnormalMaxValue": 0.55
    }
  ],
  "status": "Active"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RestErrorResponseError1Exception`](../../doc/models/rest-error-response-error-1-exception.md) |


# Reset Anomaly Settings

Resets the thresholds to Zero.

```python
def reset_anomaly_settings(self,
                          account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Template, Required | The name of the subscribed account |

## Response Type

[`RequestResponse1`](../../doc/models/request-response-1.md)

## Example Usage

```python
account_name = '0000123456-00001'

result = settings_controller.reset_anomaly_settings(account_name)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RestErrorResponseError1Exception`](../../doc/models/rest-error-response-error-1-exception.md) |

