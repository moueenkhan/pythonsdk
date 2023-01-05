# Callbacknotifications

```python
callbacknotifications_controller = client.callbacknotifications
```

## Class Name

`CallbacknotificationsController`

## Methods

* [Get Callbacks Using GET](../../doc/controllers/callbacknotifications.md#get-callbacks-using-get)
* [Register Callback Using POST](../../doc/controllers/callbacknotifications.md#register-callback-using-post)
* [Deregister Callback Using DELETE](../../doc/controllers/callbacknotifications.md#deregister-callback-using-delete)


# Get Callbacks Using GET

Returns the name and endpoint URL of the callback listening services registered for a given account.

```python
def get_callbacks_using_get(self,
                           account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |

## Response Type

[`CallbackListQueryResponse`](../../doc/models/callback-list-query-response.md)

## Example Usage

```python
account = '0242078689-00001'

result = callback_notifications_controller.get_callbacks_using_get(account)
```

## Example Response *(as JSON)*

```json
{
  "aname": "0252012345-00001",
  "name": "Fota",
  "url": "http://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Register Callback Using POST

Registers a URL to receive RESTful messages from a callback service when new firmware versions are available and when upgrades start and finish.

```python
def register_callback_using_post(self,
                                account,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `body` | [`CallbackRegistrationRequest1`](../../doc/models/callback-registration-request-1.md) | Body, Required | callback details |

## Response Type

[`CallbackRegistrationResponse1`](../../doc/models/callback-registration-response-1.md)

## Example Usage

```python
account = '0242078689-00001'
body = CallbackRegistrationRequest1()
body.name = 'Fota'
body.url = 'https://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx'

result = callback_notifications_controller.register_callback_using_post(account, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0204563412-00001",
  "serviceName": "Fota"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Deregister Callback Using DELETE

Deregisters the callback endpoint and stops ThingSpace from sending FOTA callback messages for the specified account.

```python
def deregister_callback_using_delete(self,
                                    account,
                                    service)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |
| `service` | [`ServiceEnumListEnum`](../../doc/models/service-enum-list-enum.md) | Template, Required | Callback type. Must be 'Fota' for Software Management Services API. |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
account = '0242078689-00001'
service = ServiceEnumListEnum.FOTA

result = callback_notifications_controller.deregister_callback_using_delete(account, service)
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

