# Session

Start and end Connectivity Management sessions.

```python
session_controller = client.session
```

## Class Name

`SessionController`

## Methods

* [Login Using POST](../../doc/controllers/session.md#login-using-post)
* [Logout Using POST](../../doc/controllers/session.md#logout-using-post)
* [Reset Using PUT](../../doc/controllers/session.md#reset-using-put)


# Login Using POST

Initiates a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent API requests.

```python
def login_using_post(self,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LogInRequest`](../../doc/models/log-in-request.md) | Body, Optional | request |

## Response Type

[`LogInResponse`](../../doc/models/log-in-response.md)

## Example Usage

```python
body = LogInRequest()
body.username = 'zbeeblebrox'
body.password = 'IMgr8'

result = session_controller.login_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "sessionToken": "bcce3ea6-fe4f-4952-bacf-eadd80718e83"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Logout Using POST

Ends a Connectivity Management session.

```python
def logout_using_post(self)
```

## Response Type

[`LogOutRequest`](../../doc/models/log-out-request.md)

## Example Usage

```python
result = session_controller.logout_using_post()
```

## Example Response *(as JSON)*

```json
{
  "sessionToken": "bcce3ea6-fe4f-4952-bacf-eadd80718e83"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Reset Using PUT

The new password is effective immediately. Passwords do not expire, but Verizon recommends changing your password every 90 days.

```python
def reset_using_put(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SessionResetPasswordRequest`](../../doc/models/session-reset-password-request.md) | Body, Required | Current Password |

## Response Type

[`SessionResetPasswordResponse`](../../doc/models/session-reset-password-response.md)

## Example Usage

```python
body = SessionResetPasswordRequest()
body.old_password = 'grflbk'

result = session_controller.reset_using_put(body)
```

## Example Response *(as JSON)*

```json
{
  "newPassword": "Wh0a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

