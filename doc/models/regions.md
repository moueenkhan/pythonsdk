
# Regions

Information representing a certain geographical or logical area where MEC resources and services are provided.

## Structure

`Regions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region_id` | `string` | Optional | The unique identifier of the region. |
| `name` | `string` | Optional | A relevant and identifiable region name.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9_]{3,32}$` |
| `country_code` | `string` | Optional | A two-character alpha code for a country, based on ISO 3166-1 alpha-2. This is future functionality, so the value returned is 'null'.<br>**Constraints**: *Maximum Length*: `3`, *Pattern*: `^[A-Za-z0-9]{2,3}$` |
| `metro` | `string` | Optional | The metropolitan area or 'City' value.  This is future functionality, so the value returned is 'null'.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |
| `area` | `string` | Optional | This is a sub-set of  'City' and is similar to 'Zone'. This is future functionality, so the value returned is 'null'.<br>**Constraints**: *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Example (as JSON)

```json
{
  "regionId": null,
  "name": null,
  "countryCode": null,
  "metro": null,
  "area": null
}
```

