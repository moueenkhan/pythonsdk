# Sms

Exchange Short Message Service (SMS) messages with devices.

```python
sms_controller = client.sms
```

## Class Name

`SmsController`

## Methods

* [Send Sms Message Using POST](../../doc/controllers/sms.md#send-sms-message-using-post)
* [Get Sms Messages Using GET](../../doc/controllers/sms.md#get-sms-messages-using-get)
* [Start Sms Callback Using PUT](../../doc/controllers/sms.md#start-sms-callback-using-put)


# Send Sms Message Using POST

The messages are queued on the ThingSpace Platform and sent as soon as possible, but they may be delayed due to traffic and routing considerations.

```python
def send_sms_message_using_post(self,
                               body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SMSSendRequest`](../../doc/models/sms-send-request.md) | Body, Required | SMS Request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = SMSSendRequest()
body.service_plan = 'T Plan 2'
body.sms_message = 'The rain in Spain stays mainly in the plain.'

result = sms_controller.send_sms_message_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Get Sms Messages Using GET

When HTTP status is 202, a URL will be returned in the Location header of the form /sms/{aname}/history?next={token}. This URL can be used to request the next set of messages.

```python
def get_sms_messages_using_get(self,
                              aname,
                              next=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |
| `next` | `long\|int` | Query, Optional | Continue the previous query from the URL in Location Header |

## Response Type

[`SmsMessagesResponse`](../../doc/models/sms-messages-response.md)

## Example Usage

```python
aname = '0252012345-00001'

result = sms_controller.get_sms_messages_using_get(aname)
```

## Example Response *(as JSON)*

```json
{
  "messages": [
    {
      "deviceIds": [
        {
          "id": "09623489171",
          "kind": "esn"
        }
      ],
      "message": "testmessage1",
      "timestamp": "2016-01-01T12:29:49-08:00"
    },
    {
      "deviceIds": [
        {
          "id": "09623489171",
          "kind": "esn"
        }
      ],
      "message": "testmessage2",
      "timestamp": "2016-01-01T12:31:02-08:00"
    }
  ],
  "hasMoreData": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Start Sms Callback Using PUT

Tells the ThingSpace Platform to start sending mobile-originated SMS messages through the EnhancedConnectivityService callback service. SMS messages from devices are queued until they are retrieved by your application, either by callback or synchronously with GET /sms/{accountName}/history.

```python
def start_sms_callback_using_put(self,
                                aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
aname = '0252012345-00001'

result = sms_controller.start_sms_callback_using_put(aname)
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
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

