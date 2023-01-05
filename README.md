
# Getting Started with Merged API

## Introduction

The Verizon Edge Discovery Service API can direct your application clients to connect to the optimal service endpoints for your Multi-access Edge Computing (MEC) applications for every session. The Edge Discovery Service takes into account the current location of a device, its IP anchor location, current network traffic and other factors to determine which 5G Edge platform a device should connect to.

Verizon Terms of Service: [https://staging.5gedge.verizon.com/business/5g-edge-portal/legal.html](https://staging.5gedge.verizon.com/business/5g-edge-portal/legal.html)

## Building

You must have Python `3 >=3.7, <= 3.10` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&step=installDependencies)

## Installation

The following section explains how to use the mergedapi library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&projectName=mergedapi&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&projectName=mergedapi&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&projectName=mergedapi&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&projectName=mergedapi&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from mergedapi.mergedapi_client import MergedapiClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&projectName=mergedapi&libraryName=mergedapi.mergedapi_client&className=MergedapiClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Mergedapi-Python&projectName=mergedapi&libraryName=mergedapi.mergedapi_client&className=MergedapiClient&step=runProject)

## Test the SDK

You can test the generated SDK and the server with test cases. `unittest` is used as the testing framework and `pytest` is used as the test runner. You can run the tests as follows:

Navigate to the root directory of the SDK and run the following commands

```
pip install -r test-requirements.txt
pytest
```

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

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

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | **Default** |
| staging | - |

## Authorization

This API uses `OAuth 2 Client Credentials Grant`.

## Client Credentials Grant

Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Client Credentials Grant*. This authorization includes the following steps

The `fetch_token()` method will exchange the OAuth client credentials for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

You must pass the [scopes]($h/__authorize/Scopes) for which you need permission to access.

```python
try:
    client.auth_managers['global'].fetch_token()
except OauthProviderException as ex:
    # handle exception
except APIException as ex:
    # handle exception
```

The client can now make authorized endpoint calls.

### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the `OauthScopeEnum` enumeration.

| Scope Name | Description |
|  --- | --- |
| `DISCOVERYREAD` | Grant read-only access to discovery data |
| `SERVICEPROFILEREAD` | Grant read-only access to service profile data |
| `SERVICEPROFILEWRITE` | Grant write access to service profile data |
| `SERVICEREGISTRYREAD` | Grant read-only access to Service registry data |
| `SERVICEREGISTRYWRITE` | Grant write access to Service registry data |
| `TS_MEC_FULLACCESS` | Full access for /serviceprofiles and /serviceendpoints. |
| `TS_MEC_LIMITACCESS` | Limited access. Will not allow use of /serviceprofiles and /serviceendpoints but will allow discovery. |
| `TS_APPLICATION_RO` |  |
| `EDGEDISCOVERYREAD` |  |
| `EDGESERVICEPROFILEREAD` |  |
| `EDGESERVICEPROFILEWRITE` |  |
| `EDGESERVICEREGISTRYREAD` |  |
| `EDGESERVICEREGISTRYWRITE` |  |
| `READ` | read access |
| `WRITE` | read/write access |

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.oauth_token)
```

### Creating a client from a stored token

To authorize a client from a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = MergedapiClient()
client.config.oauth_token = load_token_from_database()
```

### Complete example

```python
from mergedapi.mergedapi_client import MergedapiClient
from mergedapi.models.oauth_scope_enum import OauthScopeEnum
from mergedapi.exceptions.oauth_provider_exception import OauthProviderException

from mergedapi.exceptions.api_exception import APIException

# function for storing token to database
def save_token_to_database(token):
    # code to save the token to database

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)
    pass

from mergedapi.mergedapi_client import MergedapiClient
from mergedapi.configuration import Environment

client = MergedapiClient(
    vz_m2m_token='VZ-M2M-Token',
    oauth_client_id='OAuthClientId',
    oauth_client_secret='OAuthClientSecret',
    oauth_scopes = [OauthScopeEnum.DISCOVERYREAD, OauthScopeEnum.SERVICEPROFILEREAD],
    environment=Environment.PRODUCTION,)
# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    client.config.oauth_token = previous_token
else:
    # obtain new access token
    try:
        token = client.auth_managers['global'].fetch_token()
        save_token_to_database(token)
    except OauthProviderException as ex:
        # handle exception
    except APIException as ex:
        # handle exception

# the client is now authorized and you can use controllers to make endpoint calls
```

## List of APIs

* [5G Edge Platform Discovery](doc/controllers/5g-edge-platform-discovery.md)
* [Service Endpoint Discovery](doc/controllers/service-endpoint-discovery.md)
* [Service Profiles](doc/controllers/service-profiles.md)
* [Service Registry](doc/controllers/service-registry.md)
* [5G MEC Performance API](doc/controllers/5g-mec-performance-api.md)
* [MEC Sites](doc/controllers/mec-sites.md)
* [Service Profile](doc/controllers/service-profile.md)
* [Service Request](doc/controllers/service-request.md)
* [Service Instance Operations](doc/controllers/service-instance-operations.md)
* [Service Onboarding](doc/controllers/service-onboarding.md)
* [CSP Profile](doc/controllers/csp-profile.md)
* [Service Management](doc/controllers/service-management.md)
* [Licensemanagement](doc/controllers/licensemanagement.md)
* [Firmwareupgrades](doc/controllers/firmwareupgrades.md)
* [Callbacknotifications](doc/controllers/callbacknotifications.md)
* [Licensecancellationcandidatedeviceslist](doc/controllers/licensecancellationcandidatedeviceslist.md)
* [Device Management](doc/controllers/device-management.md)
* [Deviceservicecontroller](doc/controllers/deviceservicecontroller.md)
* [Accountservicecontroller](doc/controllers/accountservicecontroller.md)
* [OAuth Authorization](doc/controllers/oauth-authorization.md)
* [Files](doc/controllers/files.md)
* [Category](doc/controllers/category.md)
* [Tags](doc/controllers/tags.md)
* [Repository](doc/controllers/repository.md)
* [Claims](doc/controllers/claims.md)
* [Targets](doc/controllers/targets.md)
* [Subscriptions](doc/controllers/subscriptions.md)
* [Observations](doc/controllers/observations.md)
* [History](doc/controllers/history.md)
* [Settings](doc/controllers/settings.md)
* [Callbacks](doc/controllers/callbacks.md)
* [Locations](doc/controllers/locations.md)
* [Exclusions](doc/controllers/exclusions.md)
* [Reports](doc/controllers/reports.md)
* [Licenses](doc/controllers/licenses.md)
* [Campaigns](doc/controllers/campaigns.md)
* [Software](doc/controllers/software.md)
* [Devices](doc/controllers/devices.md)
* [Client Logging](doc/controllers/client-logging.md)
* [Server Logging](doc/controllers/server-logging.md)
* [Firmware](doc/controllers/firmware.md)
* [Accounts](doc/controllers/accounts.md)
* [Groups](doc/controllers/groups.md)
* [Sms](doc/controllers/sms.md)
* [Session](doc/controllers/session.md)
* [Requests](doc/controllers/requests.md)
* [Plans](doc/controllers/plans.md)
* [Triggers](doc/controllers/triggers.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

