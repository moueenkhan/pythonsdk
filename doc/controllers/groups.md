# Groups

Manage device groups.

```python
groups_controller = client.groups
```

## Class Name

`GroupsController`

## Methods

* [Create Device Group Using POST](../../doc/controllers/groups.md#create-device-group-using-post)
* [Get List Using GET](../../doc/controllers/groups.md#get-list-using-get)
* [Get Device Group Info Using GET](../../doc/controllers/groups.md#get-device-group-info-using-get)
* [Update Device Group Using PUT](../../doc/controllers/groups.md#update-device-group-using-put)
* [Delete Device Group Using DELETE](../../doc/controllers/groups.md#delete-device-group-using-delete)


# Create Device Group Using POST

Create a new device group and optionally add devices to the group. Device groups can make it easier to manage similar devices and to get reports on their usage.

```python
def create_device_group_using_post(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateDevGroupRequest`](../../doc/models/create-dev-group-request.md) | Body, Required | Request |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
body = CreateDevGroupRequest()
body.account_name = '10001234-0001'
body.devices_to_add = []

body.devices_to_add.append(DeviceId())
body.devices_to_add[0].id = '990003420535537'
body.devices_to_add[0].kind = 'imei'

body.group_description = 'Nevada tank level monitors'
body.group_name = 'NV tanks'

result = groups_controller.create_device_group_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Get List Using GET

Returns a list of all device groups in a specified account.

```python
def get_list_using_get(self,
                      aname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |

## Response Type

[`List of GroupResponse`](../../doc/models/group-response.md)

## Example Usage

```python
aname = '0252012345-00001'

result = groups_controller.get_list_using_get(aname)
```

## Example Response *(as JSON)*

```json
[
  {
    "name": "Unassigned Devices",
    "description": "All devices that are not in another device group.",
    "isDefaultGroup": true,
    "extendedAttributes": []
  },
  {
    "name": "West Coast Devices",
    "description": "",
    "isDefaultGroup": false,
    "extendedAttributes": []
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Get Device Group Info Using GET

When HTTP status is 202, a URL will be returned in the Location header of the form /groups/{aname}/name/{gname}/?next={token}. This URL can be used to request the next set of groups.

```python
def get_device_group_info_using_get(self,
                                   aname,
                                   gname,
                                   next=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |
| `gname` | `string` | Template, Required | Group name |
| `next` | `long\|int` | Query, Optional | Continue the previous query from the pageUrl pagetoken |

## Response Type

[`GroupListResponse`](../../doc/models/group-list-response.md)

## Example Usage

```python
aname = '0252012345-00001'
gname = 'gname2'

result = groups_controller.get_device_group_info_using_get(aname, gname)
```

## Example Response *(as JSON)*

```json
{
  "name": "Nebraska Trucks",
  "description": "All service trucks in Nebraska",
  "hasMoreData": false,
  "devices": [
    {
      "deviceIds": [
        {
          "id": "12345",
          "kind": "meid"
        },
        {
          "id": "54321",
          "kind": "mdn"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Update Device Group Using PUT

Make changes to a device group, including changing the name and description, and adding or removing devices.

```python
def update_device_group_using_put(self,
                                 aname,
                                 gname,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |
| `gname` | `string` | Template, Required | Group name |
| `body` | [`GroupUpdateRequest`](../../doc/models/group-update-request.md) | Body, Required | Request |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
aname = '0252012345-00001'
gname = 'gname2'
body = GroupUpdateRequest()
body.devices_to_add = []

body.devices_to_add.append(DeviceId())
body.devices_to_add[0].id = '990003420535537'
body.devices_to_add[0].kind = 'imei'

body.new_group_description = 'All western region tank level monitors'
body.new_group_name = 'Western region tanks'

result = groups_controller.update_device_group_using_put(aname, gname, body)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Delete Device Group Using DELETE

Deletes a device group from the account. Devices in the group are moved to the default device group and are not deleted from the account.

```python
def delete_device_group_using_delete(self,
                                    aname,
                                    gname)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `string` | Template, Required | Account name |
| `gname` | `string` | Template, Required | Group name |

## Response Type

[`SuccessResponse`](../../doc/models/success-response.md)

## Example Usage

```python
aname = '0252012345-00001'
gname = 'gname2'

result = groups_controller.delete_device_group_using_delete(aname, gname)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

