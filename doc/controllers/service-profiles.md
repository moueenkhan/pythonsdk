# Service Profiles

```python
service_profiles_controller = client.service_profiles
```

## Class Name

`ServiceProfilesController`

## Methods

* [Create-Service-Profile](../../doc/controllers/service-profiles.md#create-service-profile)
* [Get-Service-Profiles](../../doc/controllers/service-profiles.md#get-service-profiles)
* [Get-Service-Profile-by-Profile-Id](../../doc/controllers/service-profiles.md#get-service-profile-by-profile-id)
* [Update-Service-Profile](../../doc/controllers/service-profiles.md#update-service-profile)
* [Delete-Service-Profile](../../doc/controllers/service-profiles.md#delete-service-profile)


# Create-Service-Profile

Creates a service profile that describes the resource requirements of a service.

```python
def create_service_profile(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ResourcesServiceProfile2`](../../doc/models/resources-service-profile-2.md) | Body, Required | The request body passes all of the needed parameters to create a service profile. Parameters will be edited here rather than the **Parameters** section above. The `maxLatencyMs` and `clientType` parameters are both required in the request body. **Note:** The `maxLatencyMs` value must be submitted in multiples of 5. Additionally, "GPU" is future functionality and the values are not captured. |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`PostServiceProfileResponse`](../../doc/models/post-service-profile-response.md)

## Example Usage

```python
body = ResourcesServiceProfile2()
body.client_type = ClientTypeEnum.V2X
body.ecsp_filter = 'Verizon'
body.client_schedule = 'time windows'
body.client_service_area = 'BAY AREA'
body.network_resources = TypesNetworkResources()
body.network_resources.min_bandwidth_kbits = 1
body.network_resources.service_continuity_support = True
body.network_resources.max_request_rate = 15
body.network_resources.max_latency_ms = 20
body.network_resources.min_availability = 1
body.compute_resources = TypesComputeResources()
body.compute_resources.gpu = GPU()
body.compute_resources.gpu.min_core_clock_m_hz = 1
body.compute_resources.gpu.min_memory_clock_m_hz = 35740
body.compute_resources.gpu.min_bandwidth_g_bs = 588
body.compute_resources.gpu.min_tflops = 33
body.compute_resources.min_ramgb = 1
body.compute_resources.min_storage_gb = 1

result = service_profiles_controller.create_service_profile(body)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Get-Service-Profiles

List all service profiles registered under your API key

```python
def get_service_profiles(self)
```

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`GetServiceProfilesResponse`](../../doc/models/get-service-profiles-response.md)

## Example Usage

```python
result = service_profiles_controller.get_service_profiles()
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "data": [
    "serviceProfileId"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Get-Service-Profile-by-Profile-Id

Returns a specified service profile.

```python
def get_service_profile_by_profile_id(self,
                                     service_profile_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_profile_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`ResourcesServiceProfile`](../../doc/models/resources-service-profile.md)

## Example Usage

```python
service_profile_id = 'serviceProfileId2'

result = service_profiles_controller.get_service_profile_by_profile_id(service_profile_id)
```

## Example Response *(as JSON)*

```json
{
  "serviceProfileId": "4054ea9a-593e-4776-b488-697b1bfa4f3b",
  "ecspFilter": "Verizon",
  "clientSchedule": "time windows",
  "clientServiceArea": "BAY AREA",
  "clientType": "V2X",
  "networkResources": {
    "minBandwidthKbits": 1,
    "serviceContinuitySupport": true,
    "maxRequestRate": 15,
    "maxLatencyMs": 20,
    "minAvailability": 1
  },
  "computeResources": {
    "GPU": {
      "minCoreClockMHz": 1,
      "minMemoryClockMHz": 35740,
      "minBandwidthGBs": 588,
      "minTFLOPS": 33
    },
    "minRAMGB": 1,
    "minStorageGB": 1
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Update-Service-Profile

Update the definition of a Service Profile.

```python
def update_service_profile(self,
                          service_profile_id,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_profile_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `body` | [`ResourcesServiceProfile2`](../../doc/models/resources-service-profile-2.md) | Body, Required | The request body passes the rest of the needed parameters to create a service profile. The `maxLatencyMs` and `clientType` parameters are both required in the request body. **Note:** The `maxLatencyMs` value must be submitted in multiples of 5. Additionally, "GPU" is future functionality and the values are not captured. Default values to use are shown. |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`UpdateServiceProfile`](../../doc/models/update-service-profile.md)

## Example Usage

```python
service_profile_id = 'serviceProfileId2'
body = ResourcesServiceProfile2()
body.client_type = ClientTypeEnum.V2X
body.ecsp_filter = 'Verizon'
body.client_schedule = 'time windows'
body.client_service_area = 'BAY AREA'
body.network_resources = TypesNetworkResources()
body.network_resources.min_bandwidth_kbits = 1
body.network_resources.service_continuity_support = True
body.network_resources.max_request_rate = 15
body.network_resources.max_latency_ms = 20
body.network_resources.min_availability = 1
body.compute_resources = TypesComputeResources()
body.compute_resources.gpu = GPU()
body.compute_resources.gpu.min_core_clock_m_hz = 1
body.compute_resources.min_ramgb = 1
body.compute_resources.min_storage_gb = 1

result = service_profiles_controller.update_service_profile(service_profile_id, body)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "message": "Service Profile Updated"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |


# Delete-Service-Profile

Delete Service Profile based on unique service profile ID

```python
def delete_service_profile(self,
                          service_profile_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_profile_id` | `string` | Template, Required | **Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Requires scope

`EDGEDISCOVERYREAD`, `EDGESERVICEPROFILEREAD`, `EDGESERVICEPROFILEWRITE`, `EDGESERVICEREGISTRYREAD`, `EDGESERVICEREGISTRYWRITE`, `TS_APPLICATION_RO`, `TS_MEC_FULLACCESS`, `TS_MEC_LIMITACCESS`

## Response Type

[`DeleteServiceProfile`](../../doc/models/delete-service-profile.md)

## Example Usage

```python
service_profile_id = 'serviceProfileId2'

result = service_profiles_controller.delete_service_profile(service_profile_id)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success",
  "message": "Service Profile Deleted"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | HTTP 400 Bad Request | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| 401 | HTTP 401 Unauthorized | [`TypesErrorException`](../../doc/models/types-error-exception.md) |
| Default | HTTP 500 Internal Server Error | [`TypesErrorException`](../../doc/models/types-error-exception.md) |

