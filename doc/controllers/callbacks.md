# Callbacks

Receive notifications from the API

```python
callbacks_controller = client.callbacks
```

## Class Name

`CallbacksController`

## Methods

* [Get Diagnostics Subscription Callback Info](../../doc/controllers/callbacks.md#get-diagnostics-subscription-callback-info)
* [Register Diagnostics Callback URL](../../doc/controllers/callbacks.md#register-diagnostics-callback-url)
* [Unregister Diagnostics Callback](../../doc/controllers/callbacks.md#unregister-diagnostics-callback)
* [Get Registered Callback UR Ls](../../doc/controllers/callbacks.md#get-registered-callback-ur-ls)
* [Register Callback URL](../../doc/controllers/callbacks.md#register-callback-url)
* [Deregister Callback URL](../../doc/controllers/callbacks.md#deregister-callback-url)
* [Get Registered Callback Information](../../doc/controllers/callbacks.md#get-registered-callback-information)
* [Update HTTPS Callback Address](../../doc/controllers/callbacks.md#update-https-callback-address)
* [Create HTTPS Callback Address](../../doc/controllers/callbacks.md#create-https-callback-address)
* [Delete Registered Callback](../../doc/controllers/callbacks.md#delete-registered-callback)
* [Registered Callback Information](../../doc/controllers/callbacks.md#registered-callback-information)
* [Update Https Callback Address 1](../../doc/controllers/callbacks.md#update-https-callback-address-1)
* [Create Https Callback Address 1](../../doc/controllers/callbacks.md#create-https-callback-address-1)
* [Delete Https Callback Address](../../doc/controllers/callbacks.md#delete-https-callback-address)
* [List Callbacks Using GET](../../doc/controllers/callbacks.md#list-callbacks-using-get)
* [Register Callback Using POST](../../doc/controllers/callbacks.md#register-callback-using-post)
* [Unregister Callback Using DELETE](../../doc/controllers/callbacks.md#unregister-callback-using-delete)
* [Callbacks Account Number Get](../../doc/controllers/callbacks.md#callbacks-account-number-get)
* [Callbacks Account Number Post](../../doc/controllers/callbacks.md#callbacks-account-number-post)
* [Callbacks Account Number Name Service Delete](../../doc/controllers/callbacks.md#callbacks-account-number-name-service-delete)


# Get Diagnostics Subscription Callback Info

This endpoint allows user to get the registered callback information of an existing diagnostics subscription

```python
def get_diagnostics_subscription_callback_info(self,
                                              account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | Account identifier |

## Response Type

[`Callback`](../../doc/models/callback.md)

## Example Usage

```python
account_name = '0000123456-00001'

result = callbacks_controller.get_diagnostics_subscription_callback_info(account_name)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "string",
  "endpoint": "https://yourwebsite.com",
  "httpHeaders": {},
  "createdOn": "2019-09-07T23:57:53.292Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Register Diagnostics Callback URL

This endpoint allows user update the callback HTTPS address of an existing diagnostics subscription

```python
def register_diagnostics_callback_url(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CallbackRegistrationRequest`](../../doc/models/callback-registration-request.md) | Body, Required | Callback Url Registration |

## Response Type

[`Callback`](../../doc/models/callback.md)

## Example Usage

```python
body = CallbackRegistrationRequest()
body.account_name = 'TestQAAccount'
body.service_name = 'Diagnostics'
body.endpoint = 'https://yourwebsite.com'
body.http_headers = jsonpickle.decode('{}')

result = callbacks_controller.register_diagnostics_callback_url(body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "string",
  "endpoint": "https://yourwebsite.com",
  "httpHeaders": {},
  "createdOn": "2019-09-07T23:57:53.292Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Unregister Diagnostics Callback

This endpoint allows user to delete a registered callback Url and credential.

```python
def unregister_diagnostics_callback(self,
                                   account_name,
                                   service_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | Account identifier |
| `service_name` | `string` | Query, Required | Service name for Callback Notification |

## Response Type

[`Callback`](../../doc/models/callback.md)

## Example Usage

```python
account_name = '0000123456-00001'
service_name = 'string'

result = callbacks_controller.unregister_diagnostics_callback(account_name, service_name)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "TestQAAccount",
  "serviceName": "string",
  "endpoint": "https://yourwebsite.com",
  "httpHeaders": {},
  "createdOn": "2019-09-07T23:57:53.292Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Registered Callback UR Ls

Returns a list of all registered callback URLs for the account.

```python
def get_registered_callback_ur_ls(self,
                                 account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | account number |

## Response Type

[`List of Callback1`](../../doc/models/callback-1.md)

## Example Usage

```python
account = '0252012345-00001'

result = callbacks_controller.get_registered_callback_ur_ls(account)
```

## Example Response *(as JSON)*

```json
[
  {
    "name": "Location",
    "accountName": "0252012345-00001",
    "serviceName": "Location",
    "url": "http://10.120.102.147:50569/CallbackListener/Location.asmx"
  },
  {
    "name": "Location",
    "accountName": "0252012345-00001",
    "serviceName": "DeviceLocation",
    "url": "http://10.120.102.147:50569/CallbackListener/DeviceLocation.asmx"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorException`](../../doc/models/error-exception.md) |


# Register Callback URL

Provide a URL to receive messages from a ThingSpace callback service.

```python
def register_callback_url(self,
                         account,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | account number |
| `body` | [`Callback1`](../../doc/models/callback-1.md) | Body, Required | callback registration information |

## Response Type

[`CallbackRegistrationResponse`](../../doc/models/callback-registration-response.md)

## Example Usage

```python
account = '0252012345-00001'
body = Callback1()
body.name = CallbackServiceNameEnum.LOCATION
body.url = 'http://10.120.102.183:50559/CallbackListener/LocationServiceMessages.asmx'

result = callbacks_controller.register_callback_url(account, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0212312345-00001",
  "serviceName": "Location"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorException`](../../doc/models/error-exception.md) |


# Deregister Callback URL

Deregister a URL to stop receiving callback messages.

```python
def deregister_callback_url(self,
                           account,
                           service)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | account number |
| `service` | [`CallbackServiceNameEnum`](../../doc/models/callback-service-name-enum.md) | Template, Required | callback service name |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
account = '0252012345-00001'
service = CallbackServiceNameEnum.LOCATION

result = callbacks_controller.deregister_callback_url(account, service)
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
| 400 | Error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Registered Callback Information

This endpoint allows user to get the registered callback information.

```python
def get_registered_callback_information(self,
                                       account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |

## Response Type

[`CallbackSummary`](../../doc/models/callback-summary.md)

## Example Usage

```python
account = '0000123456-00001'

result = callbacks_controller.get_registered_callback_information(account)
```

## Example Response *(as JSON)*

```json
{
  "url": "http://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Update HTTPS Callback Address

This endpoint allows user to update the HTTPS callback address.

```python
def update_https_callback_address(self,
                                 account,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`CallbackRequest`](../../doc/models/callback-request.md) | Body, Required | Callback Url registration |

## Response Type

[`CallbackResp`](../../doc/models/callback-resp.md)

## Example Usage

```python
account = '0000123456-00001'
body = CallbackRequest()
body.url = 'https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'

result = callbacks_controller.update_https_callback_address(account, body)
```

## Example Response *(as JSON)*

```json
{
  "url": "https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Create HTTPS Callback Address

This endpoint allows user to create the HTTPS callback address.

```python
def create_https_callback_address(self,
                                 account,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `body` | [`CallbackRequest`](../../doc/models/callback-request.md) | Body, Required | Callback Url registration |

## Response Type

[`CallbackResp`](../../doc/models/callback-resp.md)

## Example Usage

```python
account = '0000123456-00001'
body = CallbackRequest()
body.url = 'https://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx'

result = callbacks_controller.create_https_callback_address(account, body)
```

## Example Response *(as JSON)*

```json
{
  "url": "https://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Delete Registered Callback

This endpoint allows user to delete a previously registered callback Url.

```python
def delete_registered_callback(self,
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
account = '0000123456-00001'

result = callbacks_controller.delete_registered_callback(account)
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


# Registered Callback Information

This endpoint allows user to get the registered callback information

```python
def registered_callback_information(self,
                                   acc)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |

## Response Type

[`CallbackRequest`](../../doc/models/callback-request.md)

## Example Usage

```python
acc = '0000123456-00001'

result = callbacks_controller.registered_callback_information(acc)
```

## Example Response *(as JSON)*

```json
{
  "url": "http://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Update Https Callback Address 1

This endpoint allows the user to update the HTTPS callback address

```python
def update_https_callback_address_1(self,
                                   acc,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `body` | [`CallbackRequest`](../../doc/models/callback-request.md) | Body, Required | Callback Url registration |

## Response Type

[`CallbackRequest`](../../doc/models/callback-request.md)

## Example Usage

```python
acc = '0000123456-00001'
body = CallbackRequest()
body.url = 'https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'

result = callbacks_controller.update_https_callback_address_1(acc, body)
```

## Example Response *(as JSON)*

```json
{
  "url": "https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Create Https Callback Address 1

This endpoint allows the user to create the HTTPS callback address

```python
def create_https_callback_address_1(self,
                                   acc,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `body` | [`CallbackRequest`](../../doc/models/callback-request.md) | Body, Required | Callback Url registration |

## Response Type

[`CallbackRequest`](../../doc/models/callback-request.md)

## Example Usage

```python
acc = '0000123456-00001'
body = CallbackRequest()
body.url = 'https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx'

result = callbacks_controller.create_https_callback_address_1(acc, body)
```

## Example Response *(as JSON)*

```json
{
  "url": "https://255.255.11.135:50559/CallbackListener/FirmwareServiceMessages.asmx"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Delete Https Callback Address

This endpoint allows user to delete a previously registered callback URL

```python
def delete_https_callback_address(self,
                                 acc)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |

## Response Type

[`SuccessResponse1`](../../doc/models/success-response-1.md)

## Example Usage

```python
acc = '0000123456-00001'

result = callbacks_controller.delete_https_callback_address(acc)
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


# List Callbacks Using GET

Returns the name and endpoint URL of the callback listening services registered for a given account.

```python
def list_callbacks_using_get(self,
                            aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |

## Response Type

[`List of Callback2`](../../doc/models/callback-2.md)

## Example Usage

```python
aname = '0252012345-00001'

result = callbacks_controller.list_callbacks_using_get(aname)
```

## Example Response *(as JSON)*

```json
[
  {
    "accountName": "0252012345-00001",
    "serviceName": "CarrierService",
    "url": "http://10.120.102.147:50569/CallbackListener/Carrier.asmx"
  },
  {
    "accountName": "0252012345-00001",
    "password": "drowssap",
    "serviceName": "DeviceUsage",
    "url": "http://10.120.102.147:50569/CallbackListener/Usage.asmx",
    "username": "zaffod"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Register Callback Using POST

You are responsible for creating and running a listening process on your server at that URL.

```python
def register_callback_using_post(self,
                                aname,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |
| `body` | [`RegisterCallbackRequest`](../../doc/models/register-callback-request.md) | Body, Required | Request |

## Response Type

[`CallbackRegistrationResponse1`](../../doc/models/callback-registration-response-1.md)

## Example Usage

```python
aname = 'TestAccount-2'
body = RegisterCallbackRequest()
body.name = 'CarrierService'
body.url = 'http://10.120.102.183:50559/CallbackListener/CarrierServiceMessages.asmx'

result = callbacks_controller.register_callback_using_post(aname, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "122333444-00002",
  "serviceName": "CarrierService"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Unregister Callback Using DELETE

Stops ThingSpace from sending callback messages for the specified account and service.

```python
def unregister_callback_using_delete(self,
                                    aname,
                                    sname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |
| `sname` | `string` | Template, Required | Service name |

## Response Type

[`CallbackRegistrationResponse1`](../../doc/models/callback-registration-response-1.md)

## Example Usage

```python
aname = '1223334444-00001'
sname = 'CarrierService'

result = callbacks_controller.unregister_callback_using_delete(aname, sname)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "1223334444-00001",
  "serviceName": "CarrierService"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Callbacks Account Number Get

Find registered callback listener for account by account number.

```python
def callbacks_account_number_get(self,
                                account_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Query, Required | A unique identifier for an account. |

## Response Type

[`List of CallBackCreated`](../../doc/models/call-back-created.md)

## Example Usage

```python
account_number = 'accountNumber2'

result = callbacks_controller.callbacks_account_number_get(account_number)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 403 | Forbidden request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 404 | Bad request. Not found. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 409 | Bad request. Conflict state. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 500 | Internal Server Error. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Callbacks Account Number Post

Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace Platform callback service. The messages are REST messages. You are responsible for creating and running a listening process on your server at that URL to receive and parse the messages.

```python
def callbacks_account_number_post(self,
                                 account_number,
                                 name,
                                 url,
                                 body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Query, Required | A unique identifier for an account. |
| `name` | `string` | Header, Required | The name to be assigned to the lister service |
| `url` | `string` | Header, Required | The address of the listerner service |
| `body` | [`CallBack3`](../../doc/models/call-back-3.md) | Body, Optional | - |

## Response Type

[`CallBackCreated`](../../doc/models/call-back-created.md)

## Example Usage

```python
account_number = 'accountNumber2'
name = 'name0'
url = 'url4'

result = callbacks_controller.callbacks_account_number_post(account_number, name, url)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 403 | Forbidden request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 404 | Bad request. Not found. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 409 | Bad request. Conflict state. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 500 | Internal Server Error. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |


# Callbacks Account Number Name Service Delete

Stops ThingSpace from sending callback messages for the specified account and listener name.

```python
def callbacks_account_number_name_service_delete(self,
                                                account_number,
                                                name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `string` | Query, Required | A unique identifier for a `Account`. |
| `name` | `string` | Query, Required | The name of the callback service that will be deleted |

## Response Type

[`ApiResponseCode`](../../doc/models/api-response-code.md)

## Example Usage

```python
account_number = 'accountNumber2'
name = 'name0'

result = callbacks_controller.callbacks_account_number_name_service_delete(account_number, name)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 401 | Unauthorized request. Access token is missing or invalid. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 403 | Forbidden request. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 404 | Bad request. Not found. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 409 | Bad request. Conflict state. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |
| 500 | Internal Server Error. | [`ErrorResponseError2Exception`](../../doc/models/error-response-error-2-exception.md) |

