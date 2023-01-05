# Licensemanagement

```python
licensemanagement_controller = client.licensemanagement
```

## Class Name

`LicensemanagementController`

## Methods

* [Assign Licenses Using POST](../../doc/controllers/licensemanagement.md#assign-licenses-using-post)
* [Remove Licenses Using POST](../../doc/controllers/licensemanagement.md#remove-licenses-using-post)
* [Createcancellation Candidate List Using POST](../../doc/controllers/licensemanagement.md#createcancellation-candidate-list-using-post)
* [Deletecancellation Candidate List Using DELETE](../../doc/controllers/licensemanagement.md#deletecancellation-candidate-list-using-delete)
* [Cancellation Candidate Query Using GET](../../doc/controllers/licensemanagement.md#cancellation-candidate-query-using-get)


# Assign Licenses Using POST

**This endpoint is deprecated.**

Assigns licenses to a specified list of devices so that firmware upgrades can be scheduled for those devices.

```python
def assign_licenses_using_post(self,
                              account,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `body` | [`LicensesAssignedRemovedRequest`](../../doc/models/licenses-assigned-removed-request.md) | Body, Required | IMEIs of the devices to assign licenses to |

## Response Type

[`LicensesAssignedRemovedResponse`](../../doc/models/licenses-assigned-removed-response.md)

## Example Usage

```python
account = '0242078689-00001'
body = LicensesAssignedRemovedRequest()
body.device_list = ['990003425730535', '990000473475989']

result = license_management_controller.assign_licenses_using_post(account, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licCount": 9000,
  "licUsedCount": 1000,
  "deviceList": [
    {
      "deviceId": "900000000000001",
      "status": "LicenseAssignSuccess",
      "Reason": "Success"
    },
    {
      "deviceId": "900000000000999",
      "status": "LicenseAssignSuccess",
      "Reason": "Success"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Remove Licenses Using POST

**This endpoint is deprecated.**

Remove unused licenses from device.

```python
def remove_licenses_using_post(self,
                              account,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `body` | [`LicensesAssignedRemovedRequest`](../../doc/models/licenses-assigned-removed-request.md) | Body, Required | IMEIs of the devices to assign licenses to |

## Response Type

[`LicensesAssignedRemovedResponse`](../../doc/models/licenses-assigned-removed-response.md)

## Example Usage

```python
account = '0242078689-00001'
body = LicensesAssignedRemovedRequest()
body.device_list = ['900000000000001', '900000000000998', '900000000000999']

result = license_management_controller.remove_licenses_using_post(account, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0242078689-00001",
  "licCount": 9000,
  "licUsedCount": 998,
  "deviceList": [
    {
      "deviceId": "900000000000001",
      "status": "LicenseRemoveSuccess",
      "Reason": "Success"
    },
    {
      "deviceId": "900000000000998",
      "status": "LicenseRemoveSuccess",
      "Reason": "Success"
    },
    {
      "deviceId": "900000000000999",
      "status": "LicenseRemoveFailed",
      "Reason": "No license attached to device"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Createcancellation Candidate List Using POST

**This endpoint is deprecated.**

Creates a list of devices from which licenses will be removed if the number of MRC licenses becomes less than the number of assigned licenses.

```python
def createcancellation_candidate_list_using_post(self,
                                                account,
                                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `body` | [`CancellationCandidateCreateRequest`](../../doc/models/cancellation-candidate-create-request.md) | Body, Required | cancellation candidate device list |

## Response Type

[`CancellationCandidateCreateResponse`](../../doc/models/cancellation-candidate-create-response.md)

## Example Usage

```python
account = '0242078689-00001'
body = CancellationCandidateCreateRequest()
body.mtype = 'append'
body.device_list = ['990003425730535', '990000473475989']

result = license_management_controller.createcancellation_candidate_list_using_post(account, body)
```

## Example Response *(as JSON)*

```json
{
  "count": 2,
  "deviceList": [
    "900000000000001",
    "900000000000999"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Deletecancellation Candidate List Using DELETE

**This endpoint is deprecated.**

Deletes the entire list of cancellation candidate devices.

```python
def deletecancellation_candidate_list_using_delete(self,
                                                  account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
account = '0242078689-00001'

result = license_management_controller.deletecancellation_candidate_list_using_delete(account)
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


# Cancellation Candidate Query Using GET

**This endpoint is deprecated.**

Returns a list of devices from which licenses will be removed if the number of MRC licenses becomes less than the number of assigned licenses.

```python
def cancellation_candidate_query_using_get(self,
                                          account,
                                          start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `start_index` | `string` | Template, Required | The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for the third request, etc. |

## Response Type

[`CancellationCandidateQueryResponse`](../../doc/models/cancellation-candidate-query-response.md)

## Example Usage

```python
account = '0242078689-00001'
start_index = 'startIndex4'

result = license_management_controller.cancellation_candidate_query_using_get(account, start_index)
```

## Example Response *(as JSON)*

```json
{
  "count": 6,
  "hasMoreData": false,
  "updateTime": "2018-03-22T12:06:06.000Z",
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

