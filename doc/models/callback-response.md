
# Callback Response

Aggregated Usage Report (Asynchronous).

## Structure

`CallbackResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `string` | Required | A unique string that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have the same txid. |
| `status` | [`Status2Enum`](../../doc/models/status-2-enum.md) | Optional | QUEUED or COMPLETED. Requests for IoT devices with cacheMode=0 (cached) have status=COMPLETED; all other requests are QUEUED. |

## Example (as JSON)

```json
{
  "txid": "txid2",
  "status": null
}
```

