# lt_user_client.ApiApi

All URIs are relative to *http://127.0.0.1:8000*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_document_create**](ApiApi.md#api_document_create) | **POST** /api/document/ | 
[**api_document_delete**](ApiApi.md#api_document_delete) | **DELETE** /api/document/{id}/ | 
[**api_document_list**](ApiApi.md#api_document_list) | **GET** /api/document/ | 
[**api_document_partial_update**](ApiApi.md#api_document_partial_update) | **PATCH** /api/document/{id}/ | 
[**api_document_read**](ApiApi.md#api_document_read) | **GET** /api/document/{id}/ | 
[**api_document_update**](ApiApi.md#api_document_update) | **PUT** /api/document/{id}/ | 
[**api_search_create**](ApiApi.md#api_search_create) | **POST** /api/search/ | 
[**api_search_delete**](ApiApi.md#api_search_delete) | **DELETE** /api/search/{id}/ | 
[**api_search_list**](ApiApi.md#api_search_list) | **GET** /api/search/ | 
[**api_search_metadata**](ApiApi.md#api_search_metadata) | **GET** /api/search/{id}/metadata/ | 
[**api_search_partial_update**](ApiApi.md#api_search_partial_update) | **PATCH** /api/search/{id}/ | 
[**api_search_read**](ApiApi.md#api_search_read) | **GET** /api/search/{id}/ | 
[**api_search_update**](ApiApi.md#api_search_update) | **PUT** /api/search/{id}/ | 


# **api_document_create**
> Document api_document_create(data)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
data = lt_user_client.Document() # Document | 

try:
    api_response = api_instance.api_document_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_delete**
> api_document_delete(id)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document.

try:
    api_instance.api_document_delete(id)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_list**
> InlineResponse200 api_document_list(limit=limit, offset=offset)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.api_document_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_partial_update**
> Document api_document_partial_update(id, data)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document.
data = lt_user_client.Document() # Document | 

try:
    api_response = api_instance.api_document_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document. | 
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_read**
> Document api_document_read(id)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document.

try:
    api_response = api_instance.api_document_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document. | 

### Return type

[**Document**](Document.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_update**
> Document api_document_update(id, data)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document.
data = lt_user_client.Document() # Document | 

try:
    api_response = api_instance.api_document_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document. | 
 **data** | [**Document**](Document.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_create**
> Search api_search_create(data)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
data = lt_user_client.Search() # Search | 

try:
    api_response = api_instance.api_search_create(data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | [**Search**](Search.md)|  | 

### Return type

[**Search**](Search.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_delete**
> api_search_delete(id)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search.

try:
    api_instance.api_search_delete(id)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_list**
> InlineResponse2001 api_search_list(limit=limit, offset=offset)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.api_search_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_metadata**
> Search api_search_metadata(id)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search.

try:
    api_response = api_instance.api_search_metadata(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search. | 

### Return type

[**Search**](Search.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_partial_update**
> Search api_search_partial_update(id, data)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search.
data = lt_user_client.Search() # Search | 

try:
    api_response = api_instance.api_search_partial_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search. | 
 **data** | [**Search**](Search.md)|  | 

### Return type

[**Search**](Search.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_read**
> Search api_search_read(id)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search.

try:
    api_response = api_instance.api_search_read(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search. | 

### Return type

[**Search**](Search.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_update**
> Search api_search_update(id, data)





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
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search.
data = lt_user_client.Search() # Search | 

try:
    api_response = api_instance.api_search_update(id, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search. | 
 **data** | [**Search**](Search.md)|  | 

### Return type

[**Search**](Search.md)

### Authorization

[Basic](../README.md#Basic)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

