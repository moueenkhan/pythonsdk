
# Get Service

## Structure

`GetService`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_url` | `string` | Optional | url to check the status of the add service<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `request_id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `correlation_id` | `string` | Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$` |
| `status` | `string` | Optional | status of the add service<br>**Constraints**: *Maximum Length*: `15`, *Pattern*: `^[A-Za-z]{1,15}$` |
| `state` | `string` | Optional | state of the service Instance<br>**Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `service` | [`ServiceInstanceResp`](../../doc/models/service-instance-resp.md) | Optional | - |

## Example (as JSON)

```json
{
  "statusUrl": null,
  "requestId": null,
  "correlationId": null,
  "status": null,
  "state": null,
  "service": null
}
```

