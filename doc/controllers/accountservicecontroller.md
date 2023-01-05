# Accountservicecontroller

```python
accountservicecontroller = client.accountservicecontroller
```

## Class Name

`Accountservicecontroller`


# Get Account Subscription List Using POST

This corresponds to the M2M-MC SOAP interface, `GetSubscriptionInformation`.

```python
def get_account_subscription_list_using_post(self,
                                            body,
                                            x_request_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SubscriptionRequest`](../../doc/models/subscription-request.md) | Body, Required | Account Subscription Request |
| `x_request_id` | `string` | Header, Optional | Transaction Id<br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9]-[0-9]{3,32}$` |

## Response Type

[`SubscriptionResponse1`](../../doc/models/subscription-response-1.md)

## Example Usage

```python
body = SubscriptionRequest()

result = account_service_controller.get_account_subscription_list_using_post(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 401 | Unauthorized | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 403 | Forbidden | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 404 | Not Found / Does not exist | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 406 | Format / Request Unacceptable | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| 429 | Too many requests | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |
| Default | Error response | [`RestErrorResponseError2Exception`](../../doc/models/rest-error-response-error-2-exception.md) |

