# lt_user_client.ApiTokenApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_token_create**](ApiTokenApi.md#api_token_create) | **POST** /api-token/ | 
[**api_token_refresh_create**](ApiTokenApi.md#api_token_refresh_create) | **POST** /api-token/refresh | 
[**api_token_verify_create**](ApiTokenApi.md#api_token_verify_create) | **POST** /api-token/verify | 

# **api_token_create**
> TokenObtainPair api_token_create(body)



Takes a set of user credentials and returns an access and refresh JSON web token pair to prove the authentication of those credentials.

### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lt_user_client.ApiTokenApi()
body = lt_user_client.TokenObtainPairRequest() # TokenObtainPairRequest | 

try:
    api_response = api_instance.api_token_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->api_token_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenObtainPairRequest**](TokenObtainPairRequest.md)|  | 

### Return type

[**TokenObtainPair**](TokenObtainPair.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_refresh_create**
> TokenRefresh api_token_refresh_create(body)



Takes a refresh type JSON web token and returns an access type JSON web token if the refresh token is valid.

### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lt_user_client.ApiTokenApi()
body = lt_user_client.TokenRefreshRequest() # TokenRefreshRequest | 

try:
    api_response = api_instance.api_token_refresh_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiTokenApi->api_token_refresh_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenRefreshRequest**](TokenRefreshRequest.md)|  | 

### Return type

[**TokenRefresh**](TokenRefresh.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_token_verify_create**
> api_token_verify_create(body)



Takes a token and indicates if it is valid.  This view provides no information about a token's fitness for a particular use.

### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = lt_user_client.ApiTokenApi()
body = lt_user_client.TokenVerifyRequest() # TokenVerifyRequest | 

try:
    api_instance.api_token_verify_create(body)
except ApiException as e:
    print("Exception when calling ApiTokenApi->api_token_verify_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TokenVerifyRequest**](TokenVerifyRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

