# Subscriptions

Get an account's location service subscription status and usage

```python
subscriptions_controller = client.subscriptions
```

## Class Name

`SubscriptionsController`

## Methods

* [Create a Subscription](../../doc/controllers/subscriptions.md#create-a-subscription)
* [Query a Subscription](../../doc/controllers/subscriptions.md#query-a-subscription)
* [Delete a Subscription](../../doc/controllers/subscriptions.md#delete-a-subscription)
* [Get Diagnostics Subscription](../../doc/controllers/subscriptions.md#get-diagnostics-subscription)
* [Get Location Subscription Status](../../doc/controllers/subscriptions.md#get-location-subscription-status)
* [Get Billable Usage Stats for Accounts](../../doc/controllers/subscriptions.md#get-billable-usage-stats-for-accounts)
* [Subscription Query Using GET](../../doc/controllers/subscriptions.md#subscription-query-using-get)
* [License Query Using GET](../../doc/controllers/subscriptions.md#license-query-using-get)
* [Get Fota Subscription](../../doc/controllers/subscriptions.md#get-fota-subscription)
* [Get a Fota Subscription](../../doc/controllers/subscriptions.md#get-a-fota-subscription)


# Create a Subscription

Create a subscription to define a streaming channel that sends data from devices in the account to an endpoint defined in a target resource.

```python
def create_a_subscription(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateASubscriptionRequest`](../../doc/models/create-a-subscription-request.md) | Body, Required | The request body provides the details of the subscription that you want to create. |

## Response Type

[`SubscriptionResponse`](../../doc/models/subscription-response.md)

## Example Usage

```python
body = CreateASubscriptionRequest()
body.accountidentifier = Accountidentifier()
body.accountidentifier.billingaccountid = '1223334444-00001'
body.email = 'me@mycompany.com'
body.billingaccountid = '1223334444-00001'
body.streamkind = 'ts.event'
body.targetid = '{target ID}'
body.name = 'Account subscription 1'
body.allowaggregation = False

result = subscriptions_controller.create_a_subscription(body)
```

## Example Response *(as JSON)*

```json
{
  "configurationfailures": 0,
  "createdon": "2018-12-21T05:05:02.134Z",
  "delegateid": "00000000-0000-0000-0000-000000000000",
  "id": "d8c145dd-6948-67ec-ed9b-6a298806bb4a",
  "kind": "ts.subscription",
  "laststreamingstatus": "",
  "laststreamingtime": "0001-01-01T00:00:00Z",
  "lastupdated": "2018-12-21T05:22:12.178Z",
  "networkfailures": 0,
  "streamfailures": 0,
  "streamkind": "ts.event",
  "targetid": "4e211a0e-e39d-6c32-e15b-d6f07f9e2ec8",
  "version": "1.0",
  "versionid": "5ed6063f-04e0-11e9-8279-02420a5e1b0b"
}
```


# Query a Subscription

Search for subscriptions by property values. Returns an array of all matching subscription resources.

```python
def query_a_subscription(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`QueryASubscriptionRequest`](../../doc/models/query-a-subscription-request.md) | Body, Required | The request body specifies fields and values to match. |

## Response Type

[`List of SubscriptionResponse`](../../doc/models/subscription-response.md)

## Example Usage

```python
body = QueryASubscriptionRequest()
body.accountidentifier = Accountidentifier()
body.accountidentifier.billingaccountid = '1223334444-00001'
body.resourceidentifier = ListString()
body.resourceidentifier.id = 'dd1682d3-2d80-cefc-f3ee-25154800beff'

result = subscriptions_controller.query_a_subscription(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "configurationfailures": 0,
    "createdon": "2019-02-13T23:13:24.689Z",
    "delegateid": "00000000-0000-0000-0000-000000000000",
    "disabled": false,
    "email": "me@mycompany.com",
    "id": "98015aed-e984-62be-f049-1d895d2d1812",
    "kind": "ts.subscription",
    "laststreamingstatus": "success",
    "laststreamingtime": "2019-02-20T18:20:45.865Z",
    "lastupdated": "2019-02-13T23:13:24.689Z",
    "networkfailures": 0,
    "streamfailures": 0,
    "streamkind": "ts.event",
    "targetid": "4e112cb3-da1d-6ece-f2c6-bb8700b20b09",
    "targettype": "Amazon Web Services",
    "version": "1.0",
    "versionid": "f68b8862-2fe4-11e9-85fd-02420a4c170d"
  }
]
```


# Delete a Subscription

Remove a subscription from a ThingSpace account.

```python
def delete_a_subscription(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteaSubscriptionRequest`](../../doc/models/deletea-subscription-request.md) | Body, Required | The request body identifies the subscription to delete. |

## Response Type

`void`

## Example Usage

```python
body = DeleteaSubscriptionRequest()
body.accountidentifier = Accountidentifier()
body.accountidentifier.billingaccountid = '1223334444-00001'
body.resourceidentifier = ListString()
body.resourceidentifier.id = 'f8b112df-739c-6236-f059-106c67bafd99'

result = subscriptions_controller.delete_a_subscription(body)
```


# Get Diagnostics Subscription

This endpoint retrieves a diagnostics subscription by account

```python
def get_diagnostics_subscription(self,
                                account_name)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Query, Required | Account identifier |

## Response Type

[`Subscription`](../../doc/models/subscription.md)

## Example Usage

```python
account_name = '0000123456-00001'

result = subscriptions_controller.get_diagnostics_subscription(account_name)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "TestQAAccount",
  "skuName": "TS-BUNDLE-KTO-DIAGNOSTIC-MRC",
  "totalAllowed": 100,
  "totalUsed": 50,
  "createdOn": "2019-08-29T00:47:59.240Z",
  "lastUpdated": "2019-08-29T00:47:59.240Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Location Subscription Status

This subscriptions endpoint retrieves an account's current location subscription status.

```python
def get_location_subscription_status(self,
                                    account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |

## Response Type

[`Subscription1`](../../doc/models/subscription-1.md)

## Example Usage

```python
account = '0000123456-00001'

result = subscriptions_controller.get_location_subscription_status(account)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "2024009649-00001",
  "locType": "TS-LOC-COARSE-CellID-5K",
  "maxAllowance": "5000",
  "purchaseTime": "2017-05-10 06:25:25.171 +0000 UTC"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Billable Usage Stats for Accounts

This endpoint allows user to search for billable usage for accounts based on the provided date range

```python
def get_billable_usage_stats_for_accounts(self,
                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UsageRequest`](../../doc/models/usage-request.md) | Body, Required | bill usage request |

## Response Type

`object`

## Example Usage

```python
body = UsageRequest()
body.account_name = '1234567890-00001'
body.start_date = '04-01-2018'
body.end_date = '04-30-2018'
body.usage_for_all_accounts = True

result = subscriptions_controller.get_billable_usage_stats_for_accounts(body)
```

## Example Response

```
{
  "accountName": "1223334444-00001",
  "usageForAllAcounts": false,
  "skuName": "TS-LOC-COARSE-CellID-Aggr",
  "transactionsAllowed": "5000",
  "totalTransactionCount": "350",
  "PrimaryAccount": {
    "accountName": "1223334444-00001",
    "transactionsCount": "125"
  },
  "ManagedAccounts": []
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Subscription Query Using GET

This subscriptions endpoint retrieves an account's current Software Management Service subscription status.

```python
def subscription_query_using_get(self,
                                account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |

## Response Type

[`SubscriptionQueryResponse`](../../doc/models/subscription-query-response.md)

## Example Usage

```python
account = '0402196254-00001'

result = subscriptions_controller.subscription_query_using_get(account)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0402196254-00001",
  "purchaseType": "TS-HFOTA-EVNT,TS-HFOTA-MRC",
  "licenseCount": 9000,
  "licenseUsedCount": 1000,
  "updateTime": "2018-03-02T16:03:06.000Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# License Query Using GET

Returns information about an account's Software Management Services licenses and a list of licensed devices.

```python
def license_query_using_get(self,
                           account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier in "##########-#####" |

## Response Type

[`LicenseQueryResponse`](../../doc/models/license-query-response.md)

## Example Usage

```python
account = '0402196254-00001'

result = subscriptions_controller.license_query_using_get(account)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0402196254-00001",
  "totalLicenses": 5000,
  "assignedLicenses": 4319,
  "hasMoreData": true,
  "lastSeenDeviceId": 1000,
  "deviceList": [
    {
      "deviceId": "990003425730535",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000473475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990000347475989",
      "assignmentTime": "2017-11-29T16:03:42.000Z"
    },
    {
      "deviceId": "990007303425535",
      "assignmentTime": "2016-11-29T15:03:36.000Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get Fota Subscription

This endpoint retrieves a fota subscription by account.

```python
def get_fota_subscription(self,
                         account)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |

## Response Type

[`SubscriptionQueryResponse`](../../doc/models/subscription-query-response.md)

## Example Usage

```python
account = '0000123456-00001'

result = subscriptions_controller.get_fota_subscription(account)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "00000000000-123345",
  "purchaseType": "TS-HFOTA-EVNT,TS-HFOTA-MRC",
  "licenseCount": 500,
  "licenseUsedCount": 400,
  "updateTime": "2020-09-17T21:11:32.170Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Get a Fota Subscription

This endpoint retrieves a fota subscription by account

```python
def get_a_fota_subscription(self,
                           acc)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |

## Response Type

[`SubscriptionQueryResponse`](../../doc/models/subscription-query-response.md)

## Example Usage

```python
acc = '0000123456-00001'

result = subscriptions_controller.get_a_fota_subscription(acc)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-000001",
  "purchaseType": "TS-HFOTA-EVNT,TS-HFOTA-MRC",
  "licenseCount": 500,
  "licenseUsedCount": 400,
  "updateTime": "2020-09-17T21:11:32.170Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |

