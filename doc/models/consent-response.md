
# Consent Response

## Structure

`ConsentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `string` | Optional | Account identifier in "##########-#####" |
| `all_device` | `bool` | Optional | Exclude all devices |
| `has_more_data` | `bool` | Optional | More devices to retrieve |
| `total_count` | `int` | Optional | Total number of excluded devices in the account |
| `update_time` | `string` | Optional | Last update time |
| `exclusion` | `List of string` | Optional | Device ID list |

## Example (as JSON)

```json
{
  "accountName": "2024009649-00001",
  "allDevice": false,
  "hasMoreData": false,
  "totalCount": 4,
  "updateTime": "2018-05-18 19:20:50.076 +0000 UTC",
  "exclusion": [
    "990003420535375",
    "420535399000375",
    "A100003861E585",
    "205353759900034"
  ]
}
```

