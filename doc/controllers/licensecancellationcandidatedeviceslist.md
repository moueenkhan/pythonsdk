# Licensecancellationcandidatedeviceslist

```python
licensecancellationcandidatedeviceslist_controller = client.licensecancellationcandidatedeviceslist
```

## Class Name

`LicensecancellationcandidatedeviceslistController`

## Methods

* [Get License Cancellation Candidate Devices List](../../doc/controllers/licensecancellationcandidatedeviceslist.md#get-license-cancellation-candidate-devices-list)
* [Create License Cancellation Candidate Devices List](../../doc/controllers/licensecancellationcandidatedeviceslist.md#create-license-cancellation-candidate-devices-list)
* [Delete Candidate Devices List](../../doc/controllers/licensecancellationcandidatedeviceslist.md#delete-candidate-devices-list)


# Get License Cancellation Candidate Devices List

**This endpoint is deprecated.**

The license cancel endpoint allows user to list registered license cancellation candidate devices.

```python
def get_license_cancellation_candidate_devices_list(self,
                                                   account,
                                                   start_index=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `start_index` | `string` | Query, Optional | Start index to retrieve |

## Response Type

[`GetCancelList`](../../doc/models/get-cancel-list.md)

## Example Usage

```python
account = '0242078689-00001'

result = license_cancellation_candidate_devices_list_controller.get_license_cancellation_candidate_devices_list(account)
```

## Example Response *(as JSON)*

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

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Create License Cancellation Candidate Devices List

**This endpoint is deprecated.**

The license cancel endpoint allows user to create a list of license cancellation candidate devices.

```python
def create_license_cancellation_candidate_devices_list(self,
                                                      account,
                                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`CreateCancelList`](../../doc/models/create-cancel-list.md) | Body, Required | license cancellation candidate devices |

## Response Type

[`CreateCancelListResponse`](../../doc/models/create-cancel-list-response.md)

## Example Usage

```python
account = '0242078689-00001'
body = CreateCancelList()
body.mtype = 'append'
body.count = 2
body.device_list = ['990003425730535', '990000473475989']

result = license_cancellation_candidate_devices_list_controller.create_license_cancellation_candidate_devices_list(account, body)
```

## Example Response *(as JSON)*

```json
{
  "count": 2,
  "deviceList": [
    "990003425730535",
    "990000473475989"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Delete Candidate Devices List

**This endpoint is deprecated.**

This endpoint allows user to delete a created cancel candidate device list.

```python
def delete_candidate_devices_list(self,
                                 account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |

## Response Type

[`SuccessResponse1`](../../doc/models/success-response-1.md)

## Example Usage

```python
account = '0242078689-00001'

result = license_cancellation_candidate_devices_list_controller.delete_candidate_devices_list(account)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

