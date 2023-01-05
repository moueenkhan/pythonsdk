
# Notificationarray

The notification details of the trigger.

## Structure

`Notificationarray`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `notification_type` | `string` | Optional | The type of notification, i.e. 'DailySummary'. |
| `callback` | `bool` | Optional | Whether or not the notification should be sent via callback.<br />true<br />false |
| `email_notification` | `bool` | Optional | Whether or not the notification should be sent via e-mail.<br />true<br />false |
| `notification_group_name` | `string` | Optional | Name for the notification group. |
| `notification_frequency_factor` | `int` | Optional | Frequency factor for notification. |
| `notification_frequency_interval` | `int` | Optional | Frequency interval for notification. |
| `external_email_recipients` | `string` | Optional | E-mail address(es) where the notification should be delivered. |
| `sms_notification` | `bool` | Optional | SMS notification |
| `sms_numbers` | `string` | Optional | SMS number |
| `reminder` | `bool` | Optional | Reminder |
| `severity` | `string` | Optional | Severity level associated with the notification. Examples would be:<br />Major<br />Minor<br />Critical<br />NotApplicable |

## Example (as JSON)

```json
{
  "notificationType": null,
  "callback": null,
  "emailNotification": null,
  "notificationGroupName": null,
  "notificationFrequencyFactor": null,
  "notificationFrequencyInterval": null,
  "externalEmailRecipients": null,
  "smsNotification": null,
  "smsNumbers": null,
  "reminder": null,
  "severity": null
}
```

