# Locations

Locate devices

```python
locations_controller = client.locations
```

## Class Name

`LocationsController`

## Methods

* [Get Devices Locations Synchronous](../../doc/controllers/locations.md#get-devices-locations-synchronous)
* [Get Devices Locations Asynchronous](../../doc/controllers/locations.md#get-devices-locations-asynchronous)
* [Cancel Device Location Request](../../doc/controllers/locations.md#cancel-device-location-request)
* [Create Location Report](../../doc/controllers/locations.md#create-location-report)
* [Retrieve Location Report](../../doc/controllers/locations.md#retrieve-location-report)
* [Get Location Report Status](../../doc/controllers/locations.md#get-location-report-status)
* [Cancel Queued Location Report Generation](../../doc/controllers/locations.md#cancel-queued-location-report-generation)


# Get Devices Locations Synchronous

This locations endpoint retrieves the locations for a list of devices.

```python
def get_devices_locations_synchronous(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocationRequest`](../../doc/models/location-request.md) | Body, Required | location request |

## Response Type

[`List of Location`](../../doc/models/location.md)

## Example Usage

```python
body = LocationRequest()
body.account_name = '1234567890-00001'
body.accuracy_mode = 0
body.cache_mode = CacheModeEnum.ENUM_1
body.device_list = []

body.device_list.append(DeviceInfo())
body.device_list[0].id = '980003420535573'
body.device_list[0].kind = 'imei'
body.device_list[0].mdn = '7892345678'

body.device_list.append(DeviceInfo())
body.device_list[1].id = '375535024300089'
body.device_list[1].kind = 'imei'
body.device_list[1].mdn = '7897654321'

body.device_list.append(DeviceInfo())
body.device_list[2].id = 'A100003861E585'
body.device_list[2].kind = 'meid'
body.device_list[2].mdn = '7897650914'


result = locations_controller.get_devices_locations_synchronous(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "msid": "7892345678",
    "pd": {
      "time": "20170520004421",
      "x": "33.45324",
      "y": "-84.59621",
      "radius": "5571",
      "qos": false
    },
    "error": {}
  },
  {
    "msid": "8583239709",
    "pd": {
      "time": "20170525214342",
      "x": "38.8408694",
      "y": "-105.0422583",
      "radius": "3866",
      "qos": false
    },
    "error": {}
  },
  {
    "msid": "7897654321",
    "pd": {},
    "error": {
      "time": "20170525214342",
      "type": "POSITION METHOD FAILURE",
      "info": "Exception code=ABSENT SUBSCRIBER"
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Devices Locations Asynchronous

Requests the current or cached location of up to 10,000 IoT or consumer devices (phones, tablets. etc.). This request returns a synchronous transaction ID, and the location information for each device is returned asynchronously as a DeviceLocation callback message

```python
def get_devices_locations_asynchronous(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocationRequest`](../../doc/models/location-request.md) | Body, Required | location request |

## Response Type

[`DeviceLocationResponse`](../../doc/models/device-location-response.md)

## Example Usage

```python
body = LocationRequest()
body.account_name = '2234434445-32333'
body.accuracy_mode = 0
body.cache_mode = CacheModeEnum.ENUM_2
body.device_list = []

body.device_list.append(DeviceInfo())
body.device_list[0].id = '354677790348290'
body.device_list[0].kind = 'imei'
body.device_list[0].mdn = '5557337468'


result = locations_controller.get_devices_locations_asynchronous(body)
```

## Example Response *(as JSON)*

```json
{
  "txid": "4be7c858-0ef9-4b15-a0c1-95061456d835",
  "status": "QUEUED"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Cancel Device Location Request

Cancel a queued or unfinished device location request

```python
def cancel_device_location_request(self,
                                  accountname,
                                  txid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `string` | Query, Required | Account identifier in "##########-#####" |
| `txid` | `string` | Template, Required | Transaction ID of the request to cancel, from the synchronous response to the original request |

## Response Type

[`TransactionID`](../../doc/models/transaction-id.md)

## Example Usage

```python
accountname = '1234567890-00001'
txid = '2c90bd28-ece4-42ef-9f02-7e3bd4fbff33'

result = locations_controller.cancel_device_location_request(accountname, txid)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Create Location Report

Request an asynchronous device location report

```python
def create_location_report(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LocationRequest`](../../doc/models/location-request.md) | Body, Required | location request |

## Response Type

[`LocationReportResponse`](../../doc/models/location-report-response.md)

## Example Usage

```python
body = LocationRequest()
body.account_name = '1234567890-00001'
body.accuracy_mode = 0
body.cache_mode = CacheModeEnum.ENUM_1
body.device_list = []

body.device_list.append(DeviceInfo())
body.device_list[0].id = '980003420535573'
body.device_list[0].kind = 'imei'
body.device_list[0].mdn = '7892345678'

body.device_list.append(DeviceInfo())
body.device_list[1].id = '375535024300089'
body.device_list[1].kind = 'imei'
body.device_list[1].mdn = '7897654321'

body.device_list.append(DeviceInfo())
body.device_list[2].id = 'A100003861E585'
body.device_list[2].kind = 'meid'
body.device_list[2].mdn = '7897650914'


result = locations_controller.create_location_report(body)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33",
  "status": "QUEUED",
  "estimatedDuration": "12"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Retrieve Location Report

Download a completed asynchronous device location report

```python
def retrieve_location_report(self,
                            account,
                            txid,
                            startindex)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `txid` | `string` | Template, Required | Transaction ID from POST /locationreports response |
| `startindex` | `int` | Template, Required | Zero-based number of the first record to return |

## Response Type

[`LocationReport`](../../doc/models/location-report.md)

## Example Usage

```python
account = '0252012345-00001'
txid = '2017-12-11Te8b47da2-3a45-46cf-9903-61815e1e97e9'
startindex = 0

result = locations_controller.retrieve_location_report(account, txid, startindex)
```

## Example Response *(as JSON)*

```json
{
  "startIndex": "0",
  "txid": "2017-12-11Te8b47da2-3a45-46cf-9903-61815e1e97e9",
  "totalCount": 3,
  "hasMoreData": false,
  "devLocationList": [
    {
      "error": {},
      "msid": "7892345678",
      "pd": {
        "qos": false,
        "radius": "5571",
        "time": "20170520004421",
        "x": "33.45324",
        "y": "-84.59621"
      }
    },
    {
      "error": {},
      "msid": "8583239709",
      "pd": {
        "qos": false,
        "radius": "3866",
        "time": "20170525214342",
        "x": "38.8408694",
        "y": "-105.0422583"
      }
    },
    {
      "error": {
        "time": "20170525214342",
        "type": "POSITION METHOD FAILURE",
        "info": "Exception code=ABSENT SUBSCRIBER"
      },
      "msid": "7897654321",
      "pd": {}
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Location Report Status

Returns the current status of a requested device location report

```python
def get_location_report_status(self,
                              account,
                              txid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `txid` | `string` | Template, Required | Transaction ID of the report |

## Response Type

[`LocationReportStatus`](../../doc/models/location-report-status.md)

## Example Usage

```python
account = '0252012345-00001'
txid = '2c90bd28-ece4-42ef-9f02-7e3bd4fbff33'

result = locations_controller.get_location_report_status(account, txid)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33",
  "status": "INPROGRESS"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Cancel Queued Location Report Generation

Cancel a queued device location report

```python
def cancel_queued_location_report_generation(self,
                                            account,
                                            txid)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `txid` | `string` | Template, Required | Transaction ID of the report to cancel |

## Response Type

[`TransactionID`](../../doc/models/transaction-id.md)

## Example Usage

```python
account = '0252012345-00001'
txid = '2c90bd28-ece4-42ef-9f02-7e3bd4fbff33'

result = locations_controller.cancel_queued_location_report_generation(account, txid)
```

## Example Response *(as JSON)*

```json
{
  "txid": "2c90bd28-ece4-42ef-9f02-7e3bd4fbff33"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

