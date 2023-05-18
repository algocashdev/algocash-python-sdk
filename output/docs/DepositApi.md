# algocash_sdk.DepositApi

All URIs are relative to *https://virtserver.swaggerhub.com/gitdevstar/Algocash/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deposit**](DepositApi.md#create_deposit) | **POST** /payin | create a deposit

# **create_deposit**
> DepositSuccess create_deposit(body)

create a deposit

create a deposit

### Example
```python
from __future__ import print_function
import time
import algocash_sdk
from algocash_sdk.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = algocash_sdk.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: signatureAuth
configuration = algocash_sdk.Configuration()
configuration.api_key['API_ACCESS_TOKEN'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['API_ACCESS_TOKEN'] = 'Bearer'

# create an instance of the API class
api_instance = algocash_sdk.DepositApi(algocash_sdk.ApiClient(configuration))
body = algocash_sdk.DepositRequest() # DepositRequest | Deposit request body

try:
    # create a deposit
    api_response = api_instance.create_deposit(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepositApi->create_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DepositRequest**](DepositRequest.md)| Deposit request body | 

### Return type

[**DepositSuccess**](DepositSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth), [signatureAuth](../README.md#signatureAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

