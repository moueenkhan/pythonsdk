# Software

```python
software_controller = client.software
```

## Class Name

`SoftwareController`


# Get Available Software List

This endpoint allows user to list a certain type of software of an account.

```python
def get_available_software_list(self,
                               account,
                               distribution_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `distribution_type` | `string` | Query, Optional | Filter distributionType to get specific type of software. Value is LWM2M, OMD-DM or HTTP |

## Response Type

[`List of SoftwarePackage`](../../doc/models/software-package.md)

## Example Usage

```python
account = '0000123456-00001'
distribution_type = 'HTTP'

result = software_controller.get_available_software_list(account, distribution_type)
```

## Example Response *(as JSON)*

```json
[
  {
    "softwareName": "FOTA_Verizon_Model-A_02To03_HF",
    "launchDate": "2020-08-31",
    "releaseNote": "",
    "model": "Model-A",
    "make": "Verizon",
    "distributionType": "HTTP",
    "devicePlatformId": "IoT"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

