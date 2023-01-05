# Triggers

Set the threshold of notification for anomalies detected.

```python
triggers_controller = client.triggers
```

## Class Name

`TriggersController`

## Methods

* [Create Anomaly Trigger](../../doc/controllers/triggers.md#create-anomaly-trigger)
* [Update Anomaly Trigger](../../doc/controllers/triggers.md#update-anomaly-trigger)
* [Get Anomaly Trigger](../../doc/controllers/triggers.md#get-anomaly-trigger)


# Create Anomaly Trigger

Creates the trigger to identify an anomaly.

```python
def create_anomaly_trigger(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List of Creattriggerchunk`](../../doc/models/creattriggerchunk.md) | Body, Required | Create Trigger Request |

## Response Type

[`TriggerResponse`](../../doc/models/trigger-response.md)

## Example Usage

```python
body = []

body.append(Creattriggerchunk())

body.append(Creattriggerchunk())


result = triggers_controller.create_anomaly_trigger(body)
```

## Example Response *(as JSON)*

```json
{
  "triggerId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RestErrorResponseError1Exception`](../../doc/models/rest-error-response-error-1-exception.md) |


# Update Anomaly Trigger

Updates an existing trigger using the account name.

```python
def update_anomaly_trigger(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`List of Creattriggerchunk1`](../../doc/models/creattriggerchunk-1.md) | Body, Required | Update Trigger Request |

## Response Type

[`RequestResponse1`](../../doc/models/request-response-1.md)

## Example Usage

```python
body = []

body.append(Creattriggerchunk1())

body.append(Creattriggerchunk1())


result = triggers_controller.update_anomaly_trigger(body)
```

## Example Response *(as JSON)*

```json
{
  "status": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RestErrorResponseError1Exception`](../../doc/models/rest-error-response-error-1-exception.md) |


# Get Anomaly Trigger

Retrieves the values for a specific trigger ID

```python
def get_anomaly_trigger(self,
                       trigger_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_id` | `string` | Template, Required | The trigger ID of a specific trigger |

## Response Type

[`TriggerValueResponse`](../../doc/models/trigger-value-response.md)

## Example Usage

```python
trigger_id = 'be1b5958-3e11-41db-9abd-b1b7618c0035'

result = triggers_controller.get_anomaly_trigger(trigger_id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RestErrorResponseError1Exception`](../../doc/models/rest-error-response-error-1-exception.md) |

