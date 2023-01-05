
# Body

## Structure

`Body`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_type` | `string` | Optional | Authentication grant type. |
| `refresh_token` | `string` | Optional | Refresh token |
| `scope` | `string` | Optional | Authentication scopes |
| `headers` | [`Headers`](../../doc/models/headers.md) | Optional | Authentication headers |
| `host` | [`Host`](../../doc/models/host.md) | Optional | Host information. |

## Example (as JSON)

```json
{
  "grant_type": "refresh_token",
  "refresh_token": "qfeqVjZTYzMmUtZWMzZqfq4ZDUtNzFhZWVkYTlmMjk1",
  "headers": {
    "Authorization": "Basic RGFrqewfq2xpZW50QXBwVjI6YzM5YjqfqmI2LWI2MWQtNDRlZTQ5MmM1YTRk",
    "Content-Type": "application/x-www-form-urlencoded"
  },
  "host": {
    "hostandpath": "https:// myhost.com:1825"
  }
}
```

