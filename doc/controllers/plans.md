# Plans

Get a list of service plans in an account.

```python
plans_controller = client.plans
```

## Class Name

`PlansController`


# Get Service Plan List Using GET

Returns a list of all data service plans that are associated with a specified billing account. When you send a request to /devices/actions/activate to activate a line of service you must specify the code for one of the service plans associated with your account.

```python
def get_service_plan_list_using_get(self,
                                   aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |

## Response Type

[`List of ServicePlanResponse`](../../doc/models/service-plan-response.md)

## Example Usage

```python
aname = '0252012345-00001'

result = plans_controller.get_service_plan_list_using_get(aname)
```

## Example Response *(as JSON)*

```json
[
  {
    "name": "2MSHR5GB",
    "code": "M2MSHR5GB",
    "sizeKb": 0,
    "carrierServicePlanCode": "84638"
  },
  {
    "name": "TNTL200TALK",
    "code": "NTL200TALK",
    "sizeKb": 0,
    "carrierServicePlanCode": "74644"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

