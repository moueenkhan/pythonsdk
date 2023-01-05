# Exclusions

Exclude devices from location services

```python
exclusions_controller = client.exclusions
```

## Class Name

`ExclusionsController`

## Methods

* [Update Account Consent Exclusion](../../doc/controllers/exclusions.md#update-account-consent-exclusion)
* [Remove Devices From Exclusion List](../../doc/controllers/exclusions.md#remove-devices-from-exclusion-list)
* [Get Consent Exclusion](../../doc/controllers/exclusions.md#get-consent-exclusion)


# Update Account Consent Exclusion

This consents endpoint sets a new exclusion list.

```python
def update_account_consent_exclusion(self,
                                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ConsentRequest`](../../doc/models/consent-request.md) | Body, Required | consent request |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
body = ConsentRequest()
body.account_name = '1234567890-00001'
body.all_device = False
body.mtype = 'replace'
body.exclusion = ['980003420535573', '375535024300089', 'A100003861E585']

result = exclusions_controller.update_account_consent_exclusion(body)
```

## Example Response *(as JSON)*

```json
{
  "transactionID": "e223cc6d-6ff7-4b6b-9f21-1dd7f474bd88",
  "status": "QUEUED"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Remove Devices From Exclusion List

Removes devices from the exclusion list so that they can be located with Device Location Services requests.

```python
def remove_devices_from_exclusion_list(self,
                                      account_name,
                                      device_list)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | the numeric name of the account |
| `device_list` | `string` | Query, Required | a list of the device IDs to remove from the exclusion list |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
account_name = '0000123456-00001'
device_list = 'IMEI'

result = exclusions_controller.remove_devices_from_exclusion_list(account_name, device_list)
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


# Get Consent Exclusion

This consents endpoint retrieves a list of excluded devices in an account.

```python
def get_consent_exclusion(self,
                         account,
                         start_index)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `start_index` | `string` | Template, Required | Zero-based number of the first record to return |

## Response Type

[`ConsentResponse`](../../doc/models/consent-response.md)

## Example Usage

```python
account = '0252012345-00001'
start_index = '0'

result = exclusions_controller.get_consent_exclusion(account, start_index)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "2024009649-00001",
  "allDevice": false,
  "hasMoreData": false,
  "totalCount": 4,
  "updateTime": "2018-05-18 19:20:50.076 +0000 UTC",
  "exclusion": [
    "990003420535375",
    "420535399000375",
    "A100003861E585",
    "205353759900034"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

