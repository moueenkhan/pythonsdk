
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `vz_m2m_token` | `string` | M2M Session Token |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `oauth_client_id` | `string` | OAuth 2 Client ID |
| `oauth_client_secret` | `string` | OAuth 2 Client Secret |
| `oauth_token` | `OauthToken` | Object for storing information about the OAuth token |
| `oauth_scopes` | `OauthScopeEnum` |  |

The API client can be initialized as follows:

```python
from mergedapi.mergedapi_client import MergedapiClient
from mergedapi.configuration import Environment

client = MergedapiClient(
    vz_m2m_token='VZ-M2M-Token',
    oauth_client_id='OAuthClientId',
    oauth_client_secret='OAuthClientSecret',
    oauth_scopes = [OauthScopeEnum.DISCOVERYREAD, OauthScopeEnum.SERVICEPROFILEREAD],
    environment=Environment.PRODUCTION,)
```

## Merged API Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| m_5g_edge_platform_discovery | Gets M5gEdgePlatformDiscoveryController |
| service_endpoint_discovery | Gets ServiceEndpointDiscoveryController |
| service_profiles | Gets ServiceProfilesController |
| service_registry | Gets ServiceRegistryController |
| m_5g_mec_performance_api | Gets M5gMECPerformanceAPIController |
| mec_sites | Gets MECSitesController |
| service_profile | Gets ServiceProfileController |
| service_request | Gets ServiceRequestController |
| service_instance_operations | Gets ServiceInstanceOperationsController |
| files | Gets FilesController |
| category | Gets CategoryController |
| tags | Gets TagsController |
| repository | Gets RepositoryController |
| service_onboarding | Gets ServiceOnboardingController |
| csp_profile | Gets CSPProfileController |
| service_management | Gets ServiceManagementController |
| claims | Gets ClaimsController |
| targets | Gets TargetsController |
| subscriptions | Gets SubscriptionsController |
| observations | Gets ObservationsController |
| history | Gets HistoryController |
| settings | Gets SettingsController |
| callbacks | Gets CallbacksController |
| locations | Gets LocationsController |
| exclusions | Gets ExclusionsController |
| license_management | Gets LicenseManagementController |
| firmware_upgrades | Gets FirmwareUpgradesController |
| callback_notifications | Gets CallbackNotificationsController |
| reports | Gets ReportsController |
| licenses | Gets LicensesController |
| license_cancellation_candidate_devices_list | Gets LicenseCancellationCandidateDevicesListController |
| campaigns | Gets CampaignsController |
| software | Gets SoftwareController |
| devices | Gets DevicesController |
| client_logging | Gets ClientLoggingController |
| server_logging | Gets ServerLoggingController |
| firmware | Gets FirmwareController |
| accounts | Gets AccountsController |
| groups | Gets GroupsController |
| sms | Gets SmsController |
| session | Gets SessionController |
| requests | Gets RequestsController |
| plans | Gets PlansController |
| device_management | Gets DeviceManagementController |
| triggers | Gets TriggersController |
| device_service_controller | Gets DeviceServiceController |
| account_service_controller | Gets AccountServiceController |
| oauth_authorization | Gets OauthAuthorizationController |

