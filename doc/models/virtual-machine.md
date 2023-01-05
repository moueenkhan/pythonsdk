
# Virtual Machine

## Structure

`VirtualMachine`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `repository` | [`Repository`](../../doc/models/repository.md) | Required | - |
| `revision` | [`Revision`](../../doc/models/revision.md) | Optional | - |
| `template_type` | [`TemplateTypeEnum`](../../doc/models/template-type-enum.md) | Required | type of the template to be used for deployment<br>**Default**: `'Terraform'` |
| `values` | [`Repository`](../../doc/models/repository.md) | Optional | - |
| `provider` | [`CloudProviderEnum`](../../doc/models/cloud-provider-enum.md) | Optional | Cloud provider where you plan to provision and operate your Kubernetes cluster |

## Example (as JSON)

```json
{
  "repository": {
    "name": null,
    "type": null,
    "endpoint": "https://charts.bitnami.com/bitnami",
    "reacheability": null
  },
  "templateType": "Terraform"
}
```

