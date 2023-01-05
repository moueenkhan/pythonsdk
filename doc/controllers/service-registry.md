# Service Registry

```python
service_registry_controller = client.service_registry
```

## Class Name

`ServiceRegistryController`

## Methods

* [Register-Service-Endpoints](../../doc/controllers/service-registry.md#register-service-endpoints)
* [Get-Service-Endpoints-All](../../doc/controllers/service-registry.md#get-service-endpoints-all)
* [Get-Service-Endpoints-by-Service Endpoints Id](../../doc/controllers/service-registry.md#get-service-endpoints-by-service-endpoints-id)
* [Update-Service-Endpoint](../../doc/controllers/service-registry.md#update-service-endpoint)
* [Deregister-Service-Endpoint](../../doc/controllers/service-registry.md#deregister-service-endpoint)


# Register-Service-Endpoints

Register Service Endpoints of a deployed application to specified MEC Platforms.

```python
def register_service_endpoints(self,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List of ResourcesEdgeHostedService2`](../../doc/models/resources-edge-hosted-service-2.md) | Body, Required | An array of Service Endpoint data for a deployed application. The request body passes all of the needed parameters to create a service endpoint. Parameters will be edited here rather than the **Parameters** section above. The `ern`,`applicationServerProviderId`, `applicationId` and `serviceProfileID` parameters are required. **Note:** Currently, the only valid value for `applicationServerProviderId`is **AWS**. Also, if you do not know one of the optional values (i.e. URI), you can erase the line from the query by back-spacing over it.<br>**Constraints**: *Maximum Items*: `100` |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`PostServiceEndpointResponse`](../../doc/models/post-service-endpoint-response.md)

## Example Usage

```python
body = []

body.append(ResourcesEdgeHostedService2())
body[0].service_endpoint = ResourcesServiceEndpoint()
body[0].service_endpoint.uri = 'http://base_path/some_segment/id'
body[0].service_endpoint.fqdn = 'thingtest.verizon.com'
body[0].service_endpoint.i_pv_4_address = '192.168.11.10'
body[0].service_endpoint.i_pv_6_address = '2001:0db8:85a3:0000:0000:8a2e:0370:1234'
body[0].service_endpoint.port = 1234
body[0].application_id = 'IogspaceJan15'
body[0].service_description = 'ThieIt'
body[0].application_server_provider_id = 'AWS'
body[0].ern = 'us-east-1-wl1-atl-wlz-1'
body[0].service_profile_id = '4054ea9a-593e-4776-b488-697b1bfa4f3b'


result = service_registry_controller.register_service_endpoints(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Get-Service-Endpoints-All

Returns a list of all registered service endpoints.

```python
def get_service_endpoints_all(self)
```

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`GetServiceEndpointsAllResponse`](../../doc/models/get-service-endpoints-all-response.md)

## Example Usage

```python
result = service_registry_controller.get_service_endpoints_all()
```

## Example Response *(as JSON)*

```json
{
  "status": "success",
  "data": [
    "serviceEndpointsId"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Get-Service-Endpoints-by-Service Endpoints Id

Returns endpoint information for all Service Endpoints registered to a specified serviceEndpointId.

```python
def get_service_endpoints_by_service_endpoints_id(self,
                                                 service_endpoints_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_endpoints_id` | `string` | Template, Required | A system-defined string identifier representing one or more registered Service Endpoints. |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`List of ResourcesEdgeHostedService2`](../../doc/models/resources-edge-hosted-service-2.md)

## Example Usage

```python
service_endpoints_id = '43f3f7bb-d6c5-4bad-b081-9a3a0df2db98'

result = service_registry_controller.get_service_endpoints_by_service_endpoints_id(service_endpoints_id)
```

## Example Response *(as JSON)*

```json
[
  {
    "serviceEndpoint": {
      "FQDN": "thingtest.verizon.com",
      "IPv4Address": "192.168.11.10",
      "IPv6Address": "2001:0db8:85a3:0000:0000:8a2e:0370:1234",
      "port": 1234,
      "URI": "http://base_path/some_segment/id"
    },
    "applicationId": "IogspaceJan15",
    "serviceDescription": "ThieIt",
    "applicationServerProviderId": "AWS",
    "ern": "us-east-1-wl1-atl-wlz-1",
    "serviceProfileID": "4054ea9a-593e-4776-b488-697b1bfa4f3b"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Update-Service-Endpoint

Update registered Service Endpoint information.

```python
def update_service_endpoint(self,
                           service_endpoints_id,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_endpoints_id` | `string` | Template, Required | A system-defined string identifier representing one or more registered Service Endpoints. |
| `body` | [`List of ResourcesEdgeHostedService2`](../../doc/models/resources-edge-hosted-service-2.md) | Body, Required | Data needed for Service Endpoint information. The request body passes the rest of the needed parameters to create a service endpoint. Parameters other than `serviceEndpointsId` will be edited here rather than the **Parameters** section above. The `ern`,`applicationServerProviderId` and `applicationId` parameters are required. **Note:** Currently, the only valid value for `applicationServerProviderId`is **AWS**.<br>**Constraints**: *Maximum Items*: `100` |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`UpdateServiceEndpoint`](../../doc/models/update-service-endpoint.md)

## Example Usage

```python
service_endpoints_id = '43f3f7bb-d6c5-4bad-b081-9a3a0df2db98'
body = []

body.append(ResourcesEdgeHostedService2())
body[0].service_endpoint = ResourcesServiceEndpoint()
body[0].service_endpoint.uri = 'http://base_path/some_segment/id'
body[0].service_endpoint.fqdn = 'thingtest.verizon.com'
body[0].service_endpoint.i_pv_4_address = '192.168.11.10'
body[0].service_endpoint.i_pv_6_address = '2001:0db8:85a3:0000:0000:8a2e:0370:1234'
body[0].service_endpoint.port = 1234
body[0].application_id = 'IogspaceJan15'
body[0].service_description = 'ThieIt'
body[0].application_server_provider_id = 'AWS'
body[0].ern = 'us-east-1-wl1-atl-wlz-1'
body[0].service_profile_id = '4054ea9a-593e-4776-b488-697b1bfa4f3b'


result = service_registry_controller.update_service_endpoint(service_endpoints_id, body)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "message": "EdgeAppServices are updated"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Deregister-Service-Endpoint

Deregister an application's Service Endpoint from the MEC Platform(s).

```python
def deregister_service_endpoint(self,
                               service_endpoints_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_endpoints_id` | `string` | Template, Required | A system-defined string identifier representing one or more registered Service Endpoints. |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`DeregisterServiceEndpoint`](../../doc/models/deregister-service-endpoint.md)

## Example Usage

```python
service_endpoints_id = '43f3f7bb-d6c5-4bad-b081-9a3a0df2db98'

result = service_registry_controller.deregister_service_endpoint(service_endpoints_id)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "message": "EdgeAppServicesID Deleted"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |

