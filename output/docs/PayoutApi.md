# algocash_sdk.PayoutApi

All URIs are relative to *https://virtserver.swaggerhub.com/gitdevstar/Algocash/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payout**](PayoutApi.md#create_payout) | **POST** /payout | create payout

# **create_payout**
> PayoutSuccess create_payout(body)

create payout

create a payout

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
api_instance = algocash_sdk.PayoutApi(algocash_sdk.ApiClient(configuration))
body = algocash_sdk.PayoutRequest() # PayoutRequest | Payout request body

try:
    # create payout
    api_response = api_instance.create_payout(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutApi->create_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PayoutRequest**](PayoutRequest.md)| Payout request body | 

### Return type

[**PayoutSuccess**](PayoutSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth), [signatureAuth](../README.md#signatureAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

