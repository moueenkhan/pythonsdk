
# ERN Response Item

## Structure

`ERNResponseItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `uuid\|string` | Optional | - |
| `name` | `string` | Optional | User display name for<br>**Constraints**: *Maximum Length*: `500`, *Pattern*: `^[\w\d_\.\#\$\%\|^\&\*\@\!\-]{1,64}$` |
| `name_space` | [`List of NamespaceIdItem`](../../doc/models/namespace-id-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": null,
  "name": null,
  "nameSpace": null
}
```

