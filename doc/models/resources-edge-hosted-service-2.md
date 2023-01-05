
# Resources Edge Hosted Service 2

Edge hosted service represented by Service Endpoint definition

## Structure

`ResourcesEdgeHostedService2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_endpoint` | [`ResourcesServiceEndpoint`](../../doc/models/resources-service-endpoint.md) | Optional | Service Endpoint path, address, and port |
| `application_id` | `string` | Optional | Unique ID representing the Edge Application<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `service_description` | `string` | Optional | Description of the Service Endpoint<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `application_server_provider_id` | `string` | Optional | Unique ID representing the Edge Application Provider<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `ern` | `string` | Optional | Edge Resource Name. A string identifier for a set of edge resources.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9-]{3,32}$` |
| `service_profile_id` | `string` | Optional | The system assigned ID of the service profile |

## Example (as JSON)

```json
{
  "serviceEndpoint": null,
  "applicationId": null,
  "serviceDescription": null,
  "applicationServerProviderId": null,
  "ern": null,
  "serviceProfileID": null
}
```

