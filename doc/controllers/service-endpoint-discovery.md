# Service Endpoint Discovery

```python
service_endpoint_discovery_controller = client.service_endpoint_discovery
```

## Class Name

`ServiceEndpointDiscoveryController`


# Get-Service-Endpoints

Returns a list of optimal Service Endpoints that client devices can connect to. **Note:** If a query is sent with all of the parameters, it will fail with a "400" error. You can search based on the following parameter combinations - Region plus Service Endpoints IDs and Subscriber density (density is optional but recommended), Region plus Service Endpoints IDs and UEIdentity(Including UEIdentity Type) and Service Endpoints IDs plus UEIdentity(Including UEIdentity Type).

```python
def get_service_endpoints(self,
                         region=None,
                         subscriber_density=None,
                         ue_identity_type=None,
                         ue_identity=None,
                         service_endpoints_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region` | `string` | Query, Optional | MEC region name. Current valid values are US_WEST_2 and US_EAST_1. |
| `subscriber_density` | `int` | Query, Optional | Minimum number of 4G/5G subscribers per square kilometer.<br>**Constraints**: `>= 1`, `<= 100` |
| `ue_identity_type` | [`TypesUEIdentityTypeEnum`](../../doc/models/types-ue-identity-type-enum.md) | Query, Optional | Type of User Equipment identifier used in `UEIdentity`. |
| `ue_identity` | `string` | Query, Optional | The identifier value for User Equipment. The type of identifier is defined by the 'UEIdentityType' parameter. The`IPAddress`format can be IPv4 or IPv6. |
| `service_endpoints_ids` | `string` | Query, Optional | A system-defined string identifier representing one or more registered Service Endpoints. |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`GetServiceEndpointsResponse`](../../doc/models/get-service-endpoints-response.md)

## Example Usage

```python
region = 'US_WEST_2'
ue_identity_type = TypesUEIdentityTypeEnum.IPADDRESS
ue_identity = '2600:1010:b1d0:0000:0000:0000:0000:0012'
service_endpoints_ids = '43f3f7bb-d6c5-4bad-b081-9a3a0df2db98'

result = service_endpoint_discovery_controller.get_service_endpoints(region, None, ue_identity_type, ue_identity, service_endpoints_ids)
```

## Example Response *(as JSON)*

```json
{
  "serviceEndpoints": [
    {
      "ern": "LASVEGAS_NV_WL",
      "serviceEndpoint": {
        "URI": "http://base_path/some_segment/id",
        "FQDN": "thingtest.verizon.com",
        "IPv4Address": "192.168.11.10",
        "IPv6Address": "2001:0db8:85a3:0000:0000:8a2e:0370:1234",
        "port": 1234
      },
      "applicationServerProviderId": "AWS",
      "applicationId": "IogspaceJan15",
      "serviceDescription": "ThieIt"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |

