# 5G MEC Performance API

```python
m_5g_mec_performance_api_controller = client.m_5g_mec_performance_api
```

## Class Name

`M5gMECPerformanceAPIController`


# Get Mecplatforms Using POST

Query the most recent data for Key Performance Indicators (KPIs) like network availability, MEC hostnames and more.

```python
def get_mecplatforms_using_post(self,
                               body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PerformanceApiRequest`](../../doc/models/performance-api-request.md) | Body, Optional | - |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`PerformanceApiResponse`](../../doc/models/performance-api-response.md)

## Example Usage

```python
body = PerformanceApiRequest()
body.imei = '440246108109673'
body.msisdn = '10691876598'

result = m_5g_mec_performance_api_controller.get_mecplatforms_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "QueryStatus": "Success",
  "Start": "1/28/2021 12:00:00",
  "End": "1/28/2021 12:15:00",
  "QueryResult": [
    {
      "name": "NetworkAvailability",
      "data": [
        "100",
        "percent",
        "high"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseErrorException`](../../doc/models/error-response-error-exception.md) |
| 401 | Unauthorized | [`ErrorResponseErrorException`](../../doc/models/error-response-error-exception.md) |
| 403 | Forbidden | [`ErrorResponseErrorException`](../../doc/models/error-response-error-exception.md) |
| 404 | Resource Not Found | [`ErrorResponseErrorException`](../../doc/models/error-response-error-exception.md) |
| 405 | Method Not Allowed | [`ErrorResponseErrorException`](../../doc/models/error-response-error-exception.md) |
| 503 | Service Unavailable | [`ErrorResponseErrorException`](../../doc/models/error-response-error-exception.md) |

