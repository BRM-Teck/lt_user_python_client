# lt_user_client.ApiTokenApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_token_create**](ApiTokenApi.md#api_token_create) | **POST** /api-token/ | 
[**api_token_refresh_create**](ApiTokenApi.md#api_token_refresh_create) | **POST** /api-token/refresh | 
[**api_token_verify_create**](ApiTokenApi.md#api_token_verify_create) | **POST** /api-token/verify | 


# **api_token_create**
> TokenObtainPair api_token_create(data)



Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = lt_user_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lt_user_client.ApiTokenApi(lt_user_client.ApiClient(configuration))
data = lt_user_client.TokenObtainPair() # TokenObtainPair | 

try:
    api_response = api_instance.api_token_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->api_token_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenObtainPair**](TokenObtainPair.md)|  | 

### Return type

[**TokenObtainPair**](TokenObtainPair.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_refresh_create**
> TokenRefresh api_token_refresh_create(data)



Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = lt_user_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lt_user_client.ApiTokenApi(lt_user_client.ApiClient(configuration))
data = lt_user_client.TokenRefresh() # TokenRefresh | 

try:
    api_response = api_instance.api_token_refresh_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->api_token_refresh_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenRefresh**](TokenRefresh.md)|  | 

### Return type

[**TokenRefresh**](TokenRefresh.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_verify_create**
> TokenVerify api_token_verify_create(data)



Takes a token and indicates if it is valid.  This view provides no information about a token's fitness for a particular use.

### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: Basic
configuration = lt_user_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = lt_user_client.ApiTokenApi(lt_user_client.ApiClient(configuration))
data = lt_user_client.TokenVerify() # TokenVerify | 

try:
    api_response = api_instance.api_token_verify_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->api_token_verify_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**TokenVerify**](TokenVerify.md)|  | 

### Return type

[**TokenVerify**](TokenVerify.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

