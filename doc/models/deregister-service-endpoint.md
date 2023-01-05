
# Deregister Service Endpoint

Response to deregister an application's Service Endpoint from one or more Multi-access Edge Compute (MEC) Platforms.

## Structure

`DeregisterServiceEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status` | `string` | Optional | HTTP status code.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `message` | `string` | Optional | EdgeAppServicesID that are deleted or error details in case of an error.<br>**Constraints**: *Maximum Length*: `32` |

## Example (as JSON)

```json
{
  "status": null,
  "message": null
}
```

