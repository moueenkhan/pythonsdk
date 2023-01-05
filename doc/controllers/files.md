# Files

```python
files_controller = client.files
```

## Class Name

`FilesController`


# Service Upload File Payload

Upload workload payload/package in the MEC platform

```python
def service_upload_file_payload(self,
                               account_name,
                               service_name,
                               version,
                               category_type,
                               category_name,
                               payload,
                               correlation_id=None,
                               category_version=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Required | User account name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `service_name` | `string` | Template, Required | ServiceName to which the file is going to be associated.<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[a-zA-Z0-9\-_]+$` |
| `version` | `string` | Template, Required | Version of the service being used.<br>**Constraints**: *Maximum Length*: `10`, *Pattern*: `^[0-9\.]+$` |
| `category_type` | [`CategoryTypeEnum`](../../doc/models/category-type-enum.md) | Query, Required | Type of the file being uploaded.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `category_name` | `string` | Query, Required | workloadName used in the service while creation.<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[a-zA-Z0-9-_.]+$` |
| `payload` | `typing.BinaryIO` | Form, Required | payload/file which is to be uploaded should be provided in formData. |
| `correlation_id` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `50`, *Pattern*: `^[a-zA-Z0-9-]+$` |
| `category_version` | `string` | Query, Optional | It is mandatory for only Service file, not mandatory for Workload & Workflow file<br>**Constraints**: *Maximum Length*: `100`, *Pattern*: `^[0-9\.]+$` |

## Response Type

[`FileServiceRes`](../../doc/models/file-service-res.md)

## Example Usage

```python
account_name = 'AccountName0'
service_name = 'serviceName8'
version = 'version4'
category_type = CategoryTypeEnum.GENERAL_VALIDATION
category_name = 'categoryName2'
payload = FileWrapper(open('dummy_file', 'rb'), 'optional-content-type')

result = files_controller.service_upload_file_payload(account_name, service_name, version, category_type, category_name, payload)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 401 | Unauthorized | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 404 | Not found | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |
| 500 | Internal Server Error | [`ErrorResponseError1Exception`](../../doc/models/error-response-error-1-exception.md) |

