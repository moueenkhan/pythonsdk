# Devices

Device information for an account

```python
devices_controller = client.devices
```

## Class Name

`DevicesController`

## Methods

* [Get Account Devices Information](../../doc/controllers/devices.md#get-account-devices-information)
* [Account Device Information](../../doc/controllers/devices.md#account-device-information)
* [Account Device Information for Devices](../../doc/controllers/devices.md#account-device-information-for-devices)
* [Active Using POST](../../doc/controllers/devices.md#active-using-post)
* [Add Using POST](../../doc/controllers/devices.md#add-using-post)
* [Update Contact Info Using PUT](../../doc/controllers/devices.md#update-contact-info-using-put)
* [Update Custom Fields Using PUT](../../doc/controllers/devices.md#update-custom-fields-using-put)
* [Deactive Using POST](../../doc/controllers/devices.md#deactive-using-post)
* [Delete Using POST](../../doc/controllers/devices.md#delete-using-post)
* [List Using POST](../../doc/controllers/devices.md#list-using-post)
* [Imei Iccid Mismatch List Using POST](../../doc/controllers/devices.md#imei-iccid-mismatch-list-using-post)
* [Move Using Put](../../doc/controllers/devices.md#move-using-put)
* [Gotostate Using Put](../../doc/controllers/devices.md#gotostate-using-put)
* [Update Service Plan Using PUT](../../doc/controllers/devices.md#update-service-plan-using-put)
* [Suspend Using POST](../../doc/controllers/devices.md#suspend-using-post)
* [Restore Using POST](../../doc/controllers/devices.md#restore-using-post)
* [Device Availability List Using POST](../../doc/controllers/devices.md#device-availability-list-using-post)
* [Connection List History Using POST](../../doc/controllers/devices.md#connection-list-history-using-post)
* [Change Cost Center Using PUT](../../doc/controllers/devices.md#change-cost-center-using-put)
* [Get Extended Diags Using POST](../../doc/controllers/devices.md#get-extended-diags-using-post)
* [Provisioning History List Using POST](../../doc/controllers/devices.md#provisioning-history-list-using-post)
* [Prl List Using POST](../../doc/controllers/devices.md#prl-list-using-post)
* [Get Device Suspension Status Using POST](../../doc/controllers/devices.md#get-device-suspension-status-using-post)
* [Usage List Using POST](../../doc/controllers/devices.md#usage-list-using-post)
* [Aggregate Using POST](../../doc/controllers/devices.md#aggregate-using-post)
* [Change Device Id Using PUT](../../doc/controllers/devices.md#change-device-id-using-put)


# Get Account Devices Information

The device endpoint gets devices information of an account.

```python
def get_account_devices_information(self,
                                   account,
                                   last_seen_device_id=None,
                                   distribution_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account` | `string` | Template, Required | Account identifier |
| `last_seen_device_id` | `string` | Query, Optional | Last seen device identifier |
| `distribution_type` | `string` | Query, Optional | Filter distributionType to get specific type of devices. Values is LWM2M, OMD-DM or HTTP |

## Response Type

[`AccountDeviceList`](../../doc/models/account-device-list.md)

## Example Usage

```python
account = '0000123456-00001'
last_seen_device_id = '15-digit IMEI'
distribution_type = 'HTTP'

result = devices_controller.get_account_devices_information(account, last_seen_device_id, distribution_type)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "maxPageSize": 1000,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "mdn": "10-digit MDN",
      "model": "Model-A",
      "make": "Verizon",
      "fotaEligible": true,
      "appFotaEligible": true,
      "licenseAssigned": true,
      "distributionType": "HTTP",
      "softwareList": [
        {
          "name": "FOTA_Verizon_Model-A_02To03_HF",
          "version": "3",
          "upgradeTime": "2020-09-08T19:00:51.541Z"
        }
      ],
      "createTime": "2020-09-08T19:00:51.541Z",
      "upgradeTime": "2020-09-08T19:00:51.541Z",
      "updateTime": "2020-09-08T19:00:51.541Z",
      "refreshTime": "2020-09-08T19:00:51.541Z"
    },
    {
      "deviceId": "15-digit IMEI",
      "mdn": "10-digit MDN",
      "model": "Model-A",
      "make": "Verizon",
      "fotaEligible": true,
      "appFotaEligible": true,
      "licenseAssigned": true,
      "distributionType": "HTTP",
      "softwareList": [
        {
          "name": "FOTA_Verizon_Model-A_02To03_HF",
          "version": "3",
          "upgradeTime": "2020-09-08T19:00:51.541Z"
        }
      ],
      "createTime": "2020-09-08T19:00:51.541Z",
      "upgradeTime": "2020-09-08T19:00:51.541Z",
      "updateTime": "2020-09-08T19:00:51.541Z",
      "refreshTime": "2020-09-08T19:00:51.541Z"
    },
    {
      "deviceId": "15-digit IMEI",
      "mdn": "10-digit MDN",
      "model": "Model-A",
      "make": "Verizon",
      "fotaEligible": true,
      "appFotaEligible": true,
      "licenseAssigned": true,
      "distributionType": "HTTP",
      "softwareList": [
        {
          "name": "FOTA_Verizon_Model-A_02To03_HF",
          "version": "3",
          "upgradeTime": "2020-09-08T19:00:51.541Z"
        }
      ],
      "createTime": "2020-09-08T19:00:51.541Z",
      "upgradeTime": "2020-09-08T19:00:51.541Z",
      "updateTime": "2020-09-08T19:00:51.541Z",
      "refreshTime": "2020-09-08T19:00:51.541Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Account Device Information

Retrieve account device information such as reported firmware on the devices

```python
def account_device_information(self,
                              acc,
                              last_seen_device_id=None,
                              protocol='LWM2M')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `last_seen_device_id` | `string` | Query, Optional | Last seen device identifier |
| `protocol` | [`DevicesProtocolEnum`](../../doc/models/devices-protocol-enum.md) | Query, Optional | Filter to retrieve a specific protocol type used<br>**Default**: `'LWM2M'` |

## Response Type

[`AccountDeviceList1`](../../doc/models/account-device-list-1.md)

## Example Usage

```python
acc = '0000123456-00001'
protocol = DevicesProtocolEnum.LW_M2M

result = devices_controller.account_device_information(acc, None, protocol)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "maxPageSize": 1000,
  "hasMoreData": true,
  "lastSeenDeviceId": "15-digit IMEI",
  "deviceList": [
    {
      "deviceId": "15-digit device ID",
      "mdn": "10-digit MDN",
      "model": "NRF9160",
      "make": "NORDIC SEMICONDUCTOR ASA",
      "firmware": "e7f4d5d4-f607-43a6-b383-cfdb6d725c82",
      "licenseAssigned": true,
      "fotaEligible": "",
      "status": "Active",
      "protocol": "HTTP",
      "softwareList": [
        {
          "name": "Sample OEM App",
          "version": "nRF9160-2021-07-15-1.0",
          "upgradeTime": "2012-04-23T18:25:43.511Z"
        },
        {
          "name": "Sample OEM Application",
          "version": "nRF9160-2021-08-13-1.0",
          "upgradeTime": "2012-04-23T18:25:43.511Z"
        },
        {
          "name": "Verizon MDM IoT Nordic nRF9160",
          "version": "1.0.0.11",
          "upgradeTime": "2012-04-23T18:25:43.511Z"
        }
      ],
      "filesList": [],
      "createTime": "2012-04-23T18:25:43.511Z",
      "upgradeTime": "2012-04-23T18:25:43.511Z",
      "statusTime": "2012-04-23T18:25:43.511Z",
      "refreshTime": "2012-04-23T18:25:43.511Z",
      "lastConnectTime": "2012-04-23T18:25:43.511Z"
    },
    {
      "deviceId": "15-digit device ID",
      "mdn": "10-digit MDN",
      "model": "BG96",
      "make": "QUECTEL",
      "firmware": "BG96MAR04A04M1G",
      "licenseAssigned": false,
      "fotaEligible": "",
      "status": "Active",
      "protocol": "LWM2M",
      "softwareList": [
        {
          "name": "VZ_MDM_IOT",
          "version": "0.14",
          "upgradeTime": "2012-04-23T18:25:43.511Z"
        }
      ],
      "filesList": [],
      "createTime": "2012-04-23T18:25:43.511Z",
      "upgradeTime": "2012-04-23T18:25:43.511Z",
      "statusTime": "2012-04-23T18:25:43.511Z",
      "refreshTime": "2012-04-23T18:25:43.511Z",
      "lastConnectTime": "2012-04-23T18:25:43.511Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Account Device Information for Devices

Retrieve device information for a list of devices on an account

```python
def account_device_information_for_devices(self,
                                          acc,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acc` | `string` | Template, Required | Account identifier |
| `body` | [`LicensesAssignedRemovedRequest`](../../doc/models/licenses-assigned-removed-request.md) | Body, Required | Request device list information |

## Response Type

[`DeviceListResponse`](../../doc/models/device-list-response.md)

## Example Usage

```python
acc = '0000123456-00001'
body = LicensesAssignedRemovedRequest()
body.device_list = ['15-digit IMEI', '15-digit IMEI']

result = devices_controller.account_device_information_for_devices(acc, body)
```

## Example Response *(as JSON)*

```json
{
  "accountName": "0000123456-00001",
  "deviceCount": 1,
  "deviceList": [
    {
      "deviceId": "15-digit IMEI",
      "mdn": "10-digit MDN",
      "model": "GM01Q",
      "make": "SEQUANS COMMUNICATIONS",
      "firmware": "SR1.2.0.0-10657",
      "fotaEligible": "true",
      "licenseAssigned": true,
      "status": "Active",
      "protocol": "LWM2M",
      "createTime": "2012-04-23T18:25:43.511Z",
      "upgradeTime": "2012-04-23T18:25:43.511Z",
      "statusTime": "2012-04-23T18:25:43.511Z",
      "refreshTime": "2012-04-23T18:25:43.511Z",
      "lastConnectionTime": "2012-04-23T18:25:43.511Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Unexpected error | [`ErrorException`](../../doc/models/error-exception.md) |


# Active Using POST

If the devices do not already exist in the account, this API resource adds them before activation.

```python
def active_using_post(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierActivateRequest`](../../doc/models/carrier-activate-request.md) | Body, Required | Activate request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = CarrierActivateRequest()
body.account_name = '0868924207-00001'
body.custom_fields = []

body.custom_fields.append(KvPair())
body.custom_fields[0].key = 'CustomField2'
body.custom_fields[0].value = 'SuperVend'

body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '990013907835573'
body.devices[0].device_ids[0].kind = 'imei'

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[1].id = '89141390780800784259'
body.devices[0].device_ids[1].kind = 'iccid'


body.devices.append(DeviceList())
body.devices[1].device_ids = []

body.devices[1].device_ids.append(DeviceId())
body.devices[1].device_ids[0].id = '990013907884259'
body.devices[1].device_ids[0].kind = 'imei'

body.devices[1].device_ids.append(DeviceId())
body.devices[1].device_ids[1].id = '89141390780800735573'
body.devices[1].device_ids[1].kind = 'iccid'


body.group_name = '4G West'
body.mdn_zip_code = '98801'
body.primary_place_of_use = PlaceOfUse()
body.primary_place_of_use.address = Address()
body.primary_place_of_use.address.address_line_1 = '1600 Pennsylvania Ave NW'
body.primary_place_of_use.address.city = 'Washington'
body.primary_place_of_use.address.state = 'DC'
body.primary_place_of_use.address.zip = '20500'
body.primary_place_of_use.address.country = 'USA'
body.primary_place_of_use.customer_name = CustomerName()
body.primary_place_of_use.customer_name.title = 'President'
body.primary_place_of_use.customer_name.first_name = 'Zaffod'
body.primary_place_of_use.customer_name.last_name = 'Beeblebrox'
body.service_plan = 'm2m_4G'

result = devices_controller.active_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Add Using POST

Use this API if you want to manage some device settings before you are ready to activate service for the devices.

```python
def add_using_post(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AddDevicesRequest`](../../doc/models/add-devices-request.md) | Body, Required | Devices to Add |

## Response Type

[`List of AddDevicesResponseMessage`](../../doc/models/add-devices-response-message.md)

## Example Usage

```python
body = AddDevicesRequest()
body.account_name = '0868924207-00001'
body.custom_fields = []

body.custom_fields.append(KvPair())
body.custom_fields[0].key = 'CustomField2'
body.custom_fields[0].value = 'SuperVend'

body.devices_to_add = []

body.devices_to_add.append(DeviceList())
body.devices_to_add[0].device_ids = []

body.devices_to_add[0].device_ids.append(DeviceId())
body.devices_to_add[0].device_ids[0].id = '990013907835573'
body.devices_to_add[0].device_ids[0].kind = 'imei'

body.devices_to_add[0].device_ids.append(DeviceId())
body.devices_to_add[0].device_ids[1].id = '89141390780800784259'
body.devices_to_add[0].device_ids[1].kind = 'iccid'


body.devices_to_add.append(DeviceList())
body.devices_to_add[1].device_ids = []

body.devices_to_add[1].device_ids.append(DeviceId())
body.devices_to_add[1].device_ids[0].id = '990013907884259'
body.devices_to_add[1].device_ids[0].kind = 'imei'

body.devices_to_add[1].device_ids.append(DeviceId())
body.devices_to_add[1].device_ids[1].id = '89141390780800735573'
body.devices_to_add[1].device_ids[1].kind = 'iccid'


body.group_name = 'West Region'
body.state = 'preactive'

result = devices_controller.add_using_post(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceIds": [
      {
        "id": "89148000000800784259",
        "kind": "iccid"
      }
    ],
    "response": "Success"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Update Contact Info Using PUT

Sends a CarrierService callback message for each device in the request when the contact information has been changed, or if there was a problem and the change could not be completed.

```python
def update_contact_info_using_put(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ContactInfoUpdateRequest`](../../doc/models/contact-info-update-request.md) | Body, Required | Change contact info request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = ContactInfoUpdateRequest()
body.account_name = '0212345678-00001'
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '19110173057'
body.devices[0].device_ids[0].kind = 'ESN'

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[1].id = '19110173057'
body.devices[0].device_ids[1].kind = 'ESN'


body.primary_place_of_use = jsonpickle.decode('{"address":{"addressLine1":"9868 Scranton Rd","addressLine2":"Suite A","city":"San Diego","state":"CA","country":"USA","zip":"92121","zip4":"0001","phone":"1234567890","phoneType":"H","emailAddress":"zaffod@theinternet.com"},"customerName":{"firstName":"Zaffod","lastName":"Beeblebrox","middleName":"P","title":"President","suffix":"I"}}')

result = devices_controller.update_contact_info_using_put(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "24da9f9a-d110-4a54-86b4-93fb76aab83c"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Update Custom Fields Using PUT

Sends a CarrierService callback message for each device in the request when the custom fields have been changed, or if there was a problem and the change could not be completed.

```python
def update_custom_fields_using_put(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CustomFieldsUpdateRequest`](../../doc/models/custom-fields-update-request.md) | Body, Required | Change custom fields request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = CustomFieldsUpdateRequest()
body.custom_fields_to_update = []

body.custom_fields_to_update.append(KvPair())
body.custom_fields_to_update[0].key = 'CustomField1'
body.custom_fields_to_update[0].value = 'West Region'

body.custom_fields_to_update.append(KvPair())
body.custom_fields_to_update[1].key = 'CustomField2'
body.custom_fields_to_update[1].value = 'Distribution'

body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '89148000000800139708'
body.devices[0].device_ids[0].kind = 'iccid'



result = devices_controller.update_custom_fields_using_put(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Deactive Using POST

Deactivating service for a device may result in an early termination fee (ETF) being charged to the account, depending on the terms of the contract with Verizon. If your contract allows ETF waivers and if you want to use one for a particular deactivation, set the etfWaiver value to True.

```python
def deactive_using_post(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierDeactivateRequest`](../../doc/models/carrier-deactivate-request.md) | Body, Required | Deactivate request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = CarrierDeactivateRequest()
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '20-digit ICCID'
body.devices[0].device_ids[0].kind = 'iccid'


body.etf_waiver = True
body.reason_code = 'FF'

result = devices_controller.deactive_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Delete Using POST

Use this API to remove unneeded devices from an account

```python
def delete_using_post(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteDevicesRequest`](../../doc/models/delete-devices-request.md) | Body, Required | Devices to delete |

## Response Type

[`List of DeleteDevicesResponseMessage`](../../doc/models/delete-devices-response-message.md)

## Example Usage

```python
body = DeleteDevicesRequest()
body.devices_to_delete = []

body.devices_to_delete.append(DeviceList())
body.devices_to_delete[0].device_ids = []

body.devices_to_delete[0].device_ids.append(DeviceId())
body.devices_to_delete[0].device_ids[0].id = '09005470263'
body.devices_to_delete[0].device_ids[0].kind = 'esn'


body.devices_to_delete.append(DeviceList())
body.devices_to_delete[1].device_ids = []

body.devices_to_delete[1].device_ids.append(DeviceId())
body.devices_to_delete[1].device_ids[0].id = '85000022411113460014'
body.devices_to_delete[1].device_ids[0].kind = 'iccid'


body.devices_to_delete.append(DeviceList())
body.devices_to_delete[2].device_ids = []

body.devices_to_delete[2].device_ids.append(DeviceId())
body.devices_to_delete[2].device_ids[0].id = '85000022412313460016'
body.devices_to_delete[2].device_ids[0].kind = 'iccid'



result = devices_controller.delete_using_post(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceIds": {
      "id": "09005470263",
      "kind": "esn"
    },
    "status": "Success"
  },
  {
    "deviceIds": {
      "id": "85000022411113460014",
      "kind": "iccid"
    },
    "status": "Success"
  },
  {
    "deviceIds": [
      {
        "id": "85000022412313460016",
        "kind": "iccid"
      },
      {
        "id": "09005470263",
        "kind": "esn"
      }
    ],
    "status": "Failed",
    "message": "The device is not in deactive state."
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# List Using POST

Returns information about a single device or information about all devices that match the given parameters. Returned information includes device provisioning state, service plan, MDN, MIN, and IP address.

```python
def list_using_post(self,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceListRequest`](../../doc/models/device-list-request.md) | Body, Required | Device Query |

## Response Type

[`DeviceListResponse1`](../../doc/models/device-list-response-1.md)

## Example Usage

```python
body = DeviceListRequest()
body.device_id = DeviceId()
body.device_id.id = '20-digit ICCID'
body.device_id.kind = 'iccid'

result = devices_controller.list_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "hasMoreData": false,
  "devices": [
    {
      "accountName": "0000123456-00001",
      "billingCycleEndDate": "2020-05-09T20:00:00-04:00",
      "carrierInformations": [
        {
          "carrierName": "Verizon Wireless",
          "servicePlan": "m2m4G",
          "state": "active"
        }
      ],
      "connected": false,
      "createdAt": "2019-08-07T10:42:15-04:00",
      "deviceIds": [
        {
          "id": "10-digit MDN",
          "kind": "mdn"
        },
        {
          "id": "15-digit IMEI",
          "kind": "imei"
        }
      ],
      "groupNames": [
        "southwest"
      ],
      "ipAddress": "0.0.0.0",
      "lastActivationBy": "Joe Q Public",
      "lastActivationDate": "2019-08-07T10:42:34-04:00",
      "lastConnectionDate": "2020-03-12T04:23:37-04:00"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Imei Iccid Mismatch List Using POST

Returns a list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware) during a specified time frame.

```python
def imei_iccid_mismatch_list_using_post(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceMismatchListRequest`](../../doc/models/device-mismatch-list-request.md) | Body, Required | Device Query |

## Response Type

[`DeviceMismatchListResponse`](../../doc/models/device-mismatch-list-response.md)

## Example Usage

```python
body = DeviceMismatchListRequest()
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '8914800000080078'
body.devices[0].device_ids[0].kind = 'ICCID'

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[1].id = '5096300587'
body.devices[0].device_ids[1].kind = 'MDN'


body.filter = DateFilter()
body.filter.earliest = '2020-05-01T15:00:00-08:00Z'
body.filter.latest = '2020-07-30T15:00:00-08:00Z'
body.account_name = '0342077109-00001'

result = devices_controller.imei_iccid_mismatch_list_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "devices": [
    {
      "accountName": "0212398765-00001",
      "mdn": "5096300587",
      "activationDate": "2011-01-21T10:55:27-08:00",
      "iccid": "89148000000800784259",
      "preImei": "990003420535573",
      "postImei": "987603420573553",
      "simOtaDate": "2017-12-01T16:00:00-08:00"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Move Using Put

Move active devices from one billing account to another within a customer profile.

```python
def move_using_put(self,
                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MoveDeviceRequest`](../../doc/models/move-device-request.md) | Body, Required | Move request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = MoveDeviceRequest()
body.account_name = '0212345678-00001'
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '19110173057'
body.devices[0].device_ids[0].kind = 'ESN'


body.service_plan = 'M2M5GB'

result = devices_controller.move_using_put(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "ec682a8b-e288-4806-934d-24e7a59ed889"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Gotostate Using Put

Changes the provisioning state of one or more devices to a specified customer-defined service and state.

```python
def gotostate_using_put(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GoToStateRequest`](../../doc/models/go-to-state-request.md) | Body, Required | Move state request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = GoToStateRequest()
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '990013907835573'
body.devices[0].device_ids[0].kind = 'imei'

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[1].id = '89141390780800784259'
body.devices[0].device_ids[1].kind = 'iccid'


body.devices.append(DeviceList())
body.devices[1].device_ids = []

body.devices[1].device_ids.append(DeviceId())
body.devices[1].device_ids[0].id = '990013907884259'
body.devices[1].device_ids[0].kind = 'imei'

body.devices[1].device_ids.append(DeviceId())
body.devices[1].device_ids[1].id = '89141390780800735573'
body.devices[1].device_ids[1].kind = 'iccid'


body.service_name = 'My Service'
body.state_name = 'My State'
body.service_plan = '87641'
body.mdn_zip_code = '94203'
body.public_ip_restriction = 'unrestricted'
body.group_name = '4G West'
body.primary_place_of_use = PlaceOfUse()
body.primary_place_of_use.address = Address()
body.primary_place_of_use.address.address_line_1 = '1600 Pennsylvania Ave NW'
body.primary_place_of_use.address.city = 'Washington'
body.primary_place_of_use.address.state = 'DC'
body.primary_place_of_use.address.zip = '20500'
body.primary_place_of_use.address.country = 'USA'
body.primary_place_of_use.customer_name = CustomerName()
body.primary_place_of_use.customer_name.title = 'President'
body.primary_place_of_use.customer_name.first_name = 'Zaffod'
body.primary_place_of_use.customer_name.last_name = 'Beeblebrox'

result = devices_controller.gotostate_using_put(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Update Service Plan Using PUT

Changes the service plan for one or more devices.

```python
def update_service_plan_using_put(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ServicePlanUpdateRequest`](../../doc/models/service-plan-update-request.md) | Body, Required | Change service plan request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = ServicePlanUpdateRequest()
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = 'A100003685E561'
body.devices[0].device_ids[0].kind = 'meid'


body.service_plan = 'new_service_plan_code'

result = devices_controller.update_service_plan_using_put(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "c8de7c1d-59b9-4cf3-b969-db76cb2ce509"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Suspend Using POST

Suspends service for one or more devices.

```python
def suspend_using_post(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierActionsRequest`](../../doc/models/carrier-actions-request.md) | Body, Required | Suspend request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = CarrierActionsRequest()
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '89148000000800139708'
body.devices[0].device_ids[0].kind = 'iccid'



result = devices_controller.suspend_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Restore Using POST

Restores service to one or more suspended devices.

```python
def restore_using_post(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CarrierActionsRequest`](../../doc/models/carrier-actions-request.md) | Body, Required | Restore request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = CarrierActionsRequest()
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '89148000000800139708'
body.devices[0].device_ids[0].kind = 'iccid'



result = devices_controller.restore_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Device Availability List Using POST

Checks whether specified devices are registered by the manufacturer with the Verizon network and are available to be activated.

```python
def device_availability_list_using_post(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceRequest`](../../doc/models/device-request.md) | Body, Required | Device Query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = DeviceRequest()
body.account_name = '0212345678-00001'
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = 'A100008385E561'
body.devices[0].device_ids[0].kind = 'meid'



result = devices_controller.device_availability_list_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Connection List History Using POST

Each response includes a maximum of 500 records. To obtain more records, you can call the API multiple times, adjusting the earliest value each time to start where the previous request finished.

```python
def connection_list_history_using_post(self,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceConnectionListRequest`](../../doc/models/device-connection-list-request.md) | Body, Required | Device connection query |

## Response Type

[`ConnectionHistoryResponse`](../../doc/models/connection-history-response.md)

## Example Usage

```python
body = DeviceConnectionListRequest()
body.device_id = DeviceId()
body.device_id.id = '89141390780800784259'
body.device_id.kind = 'iccid'
body.earliest = '2015-09-16T00:00:01Z'
body.latest = '2010-09-18T00:00:01Z'

result = devices_controller.connection_list_history_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "connectionHistory": [
    {
      "connectionEventAttributes": [
        {
          "key": "BytesUsed",
          "value": "0"
        },
        {
          "key": "Event",
          "value": "Start"
        }
      ],
      "extendedAttributes": [],
      "occurredAt": "2015-12-17T14:12:36-05:00"
    },
    {
      "connectionEventAttributes": [
        {
          "key": "BytesUsed",
          "value": "419863234"
        },
        {
          "key": "Event",
          "value": "Stop"
        },
        {
          "key": "Msisdn",
          "value": "15086303371"
        }
      ],
      "extendedAttributes": [],
      "occurredAt": "2015-12-19T01:20:00-05:00"
    }
  ],
  "hasMoreData": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Change Cost Center Using PUT

Changes or removes the CostCenterCode value or customer name and address (Primary Place of Use) for one or more devices.

```python
def change_cost_center_using_put(self,
                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceCostCenterRequest`](../../doc/models/device-cost-center-request.md) | Body, Required | Change cost center request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = DeviceCostCenterRequest()
body.cost_center = 'cc12345'
body.devices = []

body.devices.append(DeviceList())
body.devices[0].device_ids = []

body.devices[0].device_ids.append(DeviceId())
body.devices[0].device_ids[0].id = '89148000000800139708'
body.devices[0].device_ids[0].kind = 'iccid'



result = devices_controller.change_cost_center_using_put(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Get Extended Diags Using POST

Returns extended diagnostic information about a specified device, including connectivity, provisioning, billing and location status.

```python
def get_extended_diags_using_post(self,
                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceExtendedDiagnosticsRequest`](../../doc/models/device-extended-diagnostics-request.md) | Body, Required | Device Query |

## Response Type

[`DeviceExtendedDiagnosticsResponse`](../../doc/models/device-extended-diagnostics-response.md)

## Example Usage

```python
body = DeviceExtendedDiagnosticsRequest()
body.account_name = '1223334444-00001'
body.device_list = []

body.device_list.append(DeviceId())
body.device_list[0].id = '10-digit MDN'
body.device_list[0].kind = 'mdn'


result = devices_controller.get_extended_diags_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "categories": [
    {
      "categoryName": "Connectivity",
      "extendedAttributes": [
        {
          "key": "Connected",
          "value": "false"
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


# Provisioning History List Using POST

Returns the provisioning history of a specified device during a specified time period.

```python
def provisioning_history_list_using_post(self,
                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceProvisioningHistoryListRequest`](../../doc/models/device-provisioning-history-list-request.md) | Body, Required | Device provisioning history query |

## Response Type

[`List of DeviceProvisioningHistoryListResponse`](../../doc/models/device-provisioning-history-list-response.md)

## Example Usage

```python
body = DeviceProvisioningHistoryListRequest()
body.device_id = DeviceId()
body.device_id.id = '89141390780800784259'
body.device_id.kind = 'iccid'
body.earliest = '2015-09-16T00:00:01Z'
body.latest = '2015-09-18T00:00:01Z'

result = devices_controller.provisioning_history_list_using_post(body)
```

## Example Response *(as JSON)*

```json
[
  {
    "provisioningHistory": [
      {
        "occurredAt": "2015-12-17T13:56:13-05:00",
        "status": "Success",
        "eventBy": "Harry Potter",
        "eventType": "Activation Confirmed",
        "servicePlan": "Tablet5GB",
        "mdn": "",
        "msisdn": "15086303371",
        "extendedAttributes": []
      }
    ],
    "hasMoreData": false
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Prl List Using POST

4G and GSM devices do not have a PRL.

```python
def prl_list_using_post(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DevicePrlListRequest`](../../doc/models/device-prl-list-request.md) | Body, Required | Device PRL query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = DevicePrlListRequest()
body.account_name = '101234-0001'
body.group_name = 'West Region'
body.service_plan = '3G 2MB'

result = devices_controller.prl_list_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Get Device Suspension Status Using POST

Returns DeviceSuspensionStatus callback messages containing the current device state and information on how many days a device has been suspended and can continue to be suspended.

```python
def get_device_suspension_status_using_post(self,
                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceSuspensionStatusRequest`](../../doc/models/device-suspension-status-request.md) | Body, Required | Device query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = DeviceSuspensionStatusRequest()
body.filter = DeviceFilterWithoutAccount()
body.filter.group_name = 'suspended devices'
body.account_name = '1223334444-00001'

result = devices_controller.get_device_suspension_status_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "904dcdc6-a590-45e4-ac76-403306f6d883"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Usage List Using POST

Returns the network data usage history of a device during a specified time period.

```python
def usage_list_using_post(self,
                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceUsageListRequest`](../../doc/models/device-usage-list-request.md) | Body, Required | Device usage query |

## Response Type

[`DeviceUsageListResponse`](../../doc/models/device-usage-list-response.md)

## Example Usage

```python
body = DeviceUsageListRequest()
body.earliest = '2018-03-20T00:00:01Z'
body.latest = '2020-12-31T00:00:01Z'

result = devices_controller.usage_list_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "hasMoreData": false,
  "usageHistory": [
    {
      "bytesUsed": 4096,
      "extendedAttributes": [
        {
          "key": "MoSms",
          "value": "0"
        }
      ],
      "smsUsed": 0,
      "source": "Raw Usage",
      "timestamp": "2020-12-01T00:00:00Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Aggregate Using POST

The information is returned in a callback response, so you must register a URL for DeviceUsage callback messages using the POST /callbacks API.

```python
def aggregate_using_post(self,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeviceAggregateUsageListRequest`](../../doc/models/device-aggregate-usage-list-request.md) | Body, Required | Aggregated usage request |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
body = DeviceAggregateUsageListRequest()
body.device_ids = []

body.device_ids.append(DeviceId())
body.device_ids[0].id = '84258000000891490087'
body.device_ids[0].kind = 'ICCID'

body.account_name = '9992330389-00001'
body.start_time = '2021-08-01T06:00:00+00:00'
body.end_time = '2021-08-30T06:00:00+00:00'

result = devices_controller.aggregate_using_post(body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "1631e200-7398-4609-b1f8-398341229176"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |


# Change Device Id Using PUT

Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this request to transfer the line of service and the MDN to new hardware, or to change the MDN.

```python
def change_device_id_using_put(self,
                              service_type,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_type` | `string` | Template, Required | Identifier type |
| `body` | [`ChangeDeviceIdRequest`](../../doc/models/change-device-id-request.md) | Body, Required | Device query |

## Response Type

[`RequestResponse`](../../doc/models/request-response.md)

## Example Usage

```python
service_type = 'serviceType6'
body = ChangeDeviceIdRequest()
body.change_4_g_option = 'ChangeICCID'
body.device_ids = []

body.device_ids.append(DeviceId())
body.device_ids[0].id = '42590078891480000008'
body.device_ids[0].kind = 'iccid'

body.device_ids_to = []

body.device_ids_to.append(DeviceId())
body.device_ids_to[0].id = '89148000000842590078'
body.device_ids_to[0].kind = 'iccid'

body.service_plan = '4G 2GB'
body.zip_code = '98802'

result = devices_controller.change_device_id_using_put(service_type, body)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "a28892ea-6503-4aa7-bfa2-4cd45d42f61b"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`RestErrorResponseException`](../../doc/models/rest-error-response-exception.md) |

