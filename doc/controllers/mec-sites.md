# MEC Sites

```python
mec_sites_controller = client.mec_sites
```

## Class Name

`MECSitesController`

## Methods

* [Get Mec Site Locations](../../doc/controllers/mec-sites.md#get-mec-site-locations)
* [Get Cluster Namespaces](../../doc/controllers/mec-sites.md#get-cluster-namespaces)


# Get Mec Site Locations

API to support fetching of all MEC locations so that the user can view the city

```python
def get_mec_site_locations(self,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]` |

## Response Type

[`LocationOKResponse`](../../doc/models/location-ok-response.md)

## Example Usage

```python
result = mec_sites_controller.get_mec_site_locations()
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error Response | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |


# Get Cluster Namespaces

Get list of cluster and namespaces for a given ERN

```python
def get_cluster_namespaces(self,
                          ern,
                          account_name=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ern` | `string` | Template, Required | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `account_name` | `string` | Header, Optional | **Constraints**: *Maximum Length*: `64`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |

## Response Type

[`GetClustersNamespaces`](../../doc/models/get-clusters-namespaces.md)

## Example Usage

```python
ern = 'ERN6'

result = mec_sites_controller.get_cluster_namespaces(ern)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 404 | Not found | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| 500 | Internal Server Error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |
| Default | unexpected error | [`ResponseErrorException`](../../doc/models/response-error-exception.md) |

