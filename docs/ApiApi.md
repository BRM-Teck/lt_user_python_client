# lt_user_client.ApiApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_category_create**](ApiApi.md#api_category_create) | **POST** /api/category/ | 
[**api_category_destroy**](ApiApi.md#api_category_destroy) | **DELETE** /api/category/{id}/ | 
[**api_category_list**](ApiApi.md#api_category_list) | **GET** /api/category/ | 
[**api_category_partial_update**](ApiApi.md#api_category_partial_update) | **PATCH** /api/category/{id}/ | 
[**api_category_retrieve**](ApiApi.md#api_category_retrieve) | **GET** /api/category/{id}/ | 
[**api_category_update**](ApiApi.md#api_category_update) | **PUT** /api/category/{id}/ | 
[**api_document_create**](ApiApi.md#api_document_create) | **POST** /api/document/ | 
[**api_document_destroy**](ApiApi.md#api_document_destroy) | **DELETE** /api/document/{id}/ | 
[**api_document_list**](ApiApi.md#api_document_list) | **GET** /api/document/ | 
[**api_document_partial_update**](ApiApi.md#api_document_partial_update) | **PATCH** /api/document/{id}/ | 
[**api_document_retrieve**](ApiApi.md#api_document_retrieve) | **GET** /api/document/{id}/ | 
[**api_document_type_create**](ApiApi.md#api_document_type_create) | **POST** /api/document-type/ | 
[**api_document_type_destroy**](ApiApi.md#api_document_type_destroy) | **DELETE** /api/document-type/{id}/ | 
[**api_document_type_list**](ApiApi.md#api_document_type_list) | **GET** /api/document-type/ | 
[**api_document_type_partial_update**](ApiApi.md#api_document_type_partial_update) | **PATCH** /api/document-type/{id}/ | 
[**api_document_type_retrieve**](ApiApi.md#api_document_type_retrieve) | **GET** /api/document-type/{id}/ | 
[**api_document_type_update**](ApiApi.md#api_document_type_update) | **PUT** /api/document-type/{id}/ | 
[**api_document_update**](ApiApi.md#api_document_update) | **PUT** /api/document/{id}/ | 
[**api_search_create**](ApiApi.md#api_search_create) | **POST** /api/search/ | 
[**api_search_destroy**](ApiApi.md#api_search_destroy) | **DELETE** /api/search/{id}/ | 
[**api_search_list**](ApiApi.md#api_search_list) | **GET** /api/search/ | 
[**api_search_metadata_retrieve**](ApiApi.md#api_search_metadata_retrieve) | **GET** /api/search/{id}/metadata/ | 
[**api_search_partial_update**](ApiApi.md#api_search_partial_update) | **PATCH** /api/search/{id}/ | 
[**api_search_retrieve**](ApiApi.md#api_search_retrieve) | **GET** /api/search/{id}/ | 
[**api_search_update**](ApiApi.md#api_search_update) | **PUT** /api/search/{id}/ | 

# **api_category_create**
> Category api_category_create(body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.CategoryRequest() # CategoryRequest | 

try:
    api_response = api_instance.api_category_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_category_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryRequest**](CategoryRequest.md)|  | 

### Return type

[**Category**](Category.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_category_destroy**
> api_category_destroy(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this category.

try:
    api_instance.api_category_destroy(id)
except ApiException as e:
    print("Exception when calling ApiApi->api_category_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this category. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_category_list**
> PaginatedCategoryList api_category_list(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.api_category_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_category_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedCategoryList**](PaginatedCategoryList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_category_partial_update**
> Category api_category_partial_update(id, body=body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this category.
body = lt_user_client.PatchedCategoryRequest() # PatchedCategoryRequest |  (optional)

try:
    api_response = api_instance.api_category_partial_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_category_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this category. | 
 **body** | [**PatchedCategoryRequest**](PatchedCategoryRequest.md)|  | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_category_retrieve**
> Category api_category_retrieve(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this category.

try:
    api_response = api_instance.api_category_retrieve(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_category_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this category. | 

### Return type

[**Category**](Category.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_category_update**
> Category api_category_update(body, id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.CategoryRequest() # CategoryRequest | 
id = 56 # int | A unique integer value identifying this category.

try:
    api_response = api_instance.api_category_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_category_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryRequest**](CategoryRequest.md)|  | 
 **id** | **int**| A unique integer value identifying this category. | 

### Return type

[**Category**](Category.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_create**
> Document api_document_create(body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.DocumentRequest() # DocumentRequest | 

try:
    api_response = api_instance.api_document_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentRequest**](DocumentRequest.md)|  | 

### Return type

[**Document**](Document.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_destroy**
> api_document_destroy(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document.

try:
    api_instance.api_document_destroy(id)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_list**
> PaginatedDocumentList api_document_list(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


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

[**PaginatedDocumentList**](PaginatedDocumentList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_partial_update**
> Document api_document_partial_update(id, body=body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document.
body = lt_user_client.PatchedDocumentRequest() # PatchedDocumentRequest |  (optional)

try:
    api_response = api_instance.api_document_partial_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document. | 
 **body** | [**PatchedDocumentRequest**](PatchedDocumentRequest.md)|  | [optional] 

### Return type

[**Document**](Document.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_retrieve**
> Document api_document_retrieve(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document.

try:
    api_response = api_instance.api_document_retrieve(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document. | 

### Return type

[**Document**](Document.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_type_create**
> DocumentType api_document_type_create(body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.DocumentTypeRequest() # DocumentTypeRequest | 

try:
    api_response = api_instance.api_document_type_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_type_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentTypeRequest**](DocumentTypeRequest.md)|  | 

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_type_destroy**
> api_document_type_destroy(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document type.

try:
    api_instance.api_document_type_destroy(id)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_type_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document type. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_type_list**
> PaginatedDocumentTypeList api_document_type_list(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
limit = 56 # int | Number of results to return per page. (optional)
offset = 56 # int | The initial index from which to return the results. (optional)

try:
    api_response = api_instance.api_document_type_list(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_type_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results to return per page. | [optional] 
 **offset** | **int**| The initial index from which to return the results. | [optional] 

### Return type

[**PaginatedDocumentTypeList**](PaginatedDocumentTypeList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_type_partial_update**
> DocumentType api_document_type_partial_update(id, body=body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document type.
body = lt_user_client.PatchedDocumentTypeRequest() # PatchedDocumentTypeRequest |  (optional)

try:
    api_response = api_instance.api_document_type_partial_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_type_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document type. | 
 **body** | [**PatchedDocumentTypeRequest**](PatchedDocumentTypeRequest.md)|  | [optional] 

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_type_retrieve**
> DocumentType api_document_type_retrieve(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this document type.

try:
    api_response = api_instance.api_document_type_retrieve(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_type_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this document type. | 

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_type_update**
> DocumentType api_document_type_update(body, id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.DocumentTypeRequest() # DocumentTypeRequest | 
id = 56 # int | A unique integer value identifying this document type.

try:
    api_response = api_instance.api_document_type_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_type_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentTypeRequest**](DocumentTypeRequest.md)|  | 
 **id** | **int**| A unique integer value identifying this document type. | 

### Return type

[**DocumentType**](DocumentType.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_document_update**
> Document api_document_update(body, id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.DocumentRequest() # DocumentRequest | 
id = 56 # int | A unique integer value identifying this document.

try:
    api_response = api_instance.api_document_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_document_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DocumentRequest**](DocumentRequest.md)|  | 
 **id** | **int**| A unique integer value identifying this document. | 

### Return type

[**Document**](Document.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_create**
> Search api_search_create(body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.SearchRequest() # SearchRequest | 

try:
    api_response = api_instance.api_search_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**Search**](Search.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_destroy**
> api_search_destroy(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search request.

try:
    api_instance.api_search_destroy(id)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_destroy: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search request. | 

### Return type

void (empty response body)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_list**
> PaginatedSearchList api_search_list(limit=limit, offset=offset)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


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

[**PaginatedSearchList**](PaginatedSearchList.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_metadata_retrieve**
> Search api_search_metadata_retrieve(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search request.

try:
    api_response = api_instance.api_search_metadata_retrieve(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_metadata_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search request. | 

### Return type

[**Search**](Search.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_partial_update**
> Search api_search_partial_update(id, body=body)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search request.
body = lt_user_client.PatchedSearchRequest() # PatchedSearchRequest |  (optional)

try:
    api_response = api_instance.api_search_partial_update(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_partial_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search request. | 
 **body** | [**PatchedSearchRequest**](PatchedSearchRequest.md)|  | [optional] 

### Return type

[**Search**](Search.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_retrieve**
> Search api_search_retrieve(id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
id = 56 # int | A unique integer value identifying this search request.

try:
    api_response = api_instance.api_search_retrieve(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_retrieve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| A unique integer value identifying this search request. | 

### Return type

[**Search**](Search.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_search_update**
> Search api_search_update(body, id)



### Example
```python
from __future__ import print_function
import time
import lt_user_client
from lt_user_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = lt_user_client.ApiApi(lt_user_client.ApiClient(configuration))
body = lt_user_client.SearchRequest() # SearchRequest | 
id = 56 # int | A unique integer value identifying this search request.

try:
    api_response = api_instance.api_search_update(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->api_search_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)|  | 
 **id** | **int**| A unique integer value identifying this search request. | 

### Return type

[**Search**](Search.md)

### Authorization

[jwtAuth](../README.md#jwtAuth)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded, multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

