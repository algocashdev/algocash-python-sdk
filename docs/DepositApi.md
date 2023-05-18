# algocash_sdk.DepositApi

All URIs are relative to *https://virtserver.swaggerhub.com/gitdevstar/Algocash/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_deposit**](DepositApi.md#create_deposit) | **POST** /payin | create a deposit

# **create_deposit**
> DepositSuccess create_deposit(invoice_id, amount, payer, payment_method, url)

create a deposit

create a deposit

### Example
```python
from __future__ import print_function
import time
import algocash_sdk
from algocash_sdk.rest import ApiException
from pprint import pprint

configuration = algocash_sdk.Configuration()
configuration.merchant_key = 'MERCHANT_KEY'
configuration.merchant_secret = 'MERCHANT_SECRET'
configuration.api_access_token = 'API_ACCESS_TOKEN'
configuration.devmode = True # if production, False

# create an instance of the API class
api_instance = algocash_sdk.DepositApi(algocash_sdk.ApiClient(configuration))
invoice_id = '12321421' # str | 
amount = '12' # str | 
payer = algocash_sdk.Payer('email', 'phone number').to_str() # Payer 
payment_method = 'UPI' # str | 
url = algocash_sdk.Url('callback_url', 'pending_url', 'success_url', 'error_url').to_str() # Url | 

try:
    # create a deposit
    api_response = api_instance.create_deposit(invoice_id, amount, payer, payment_method, url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepositApi->create_deposit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **amount** | **str**|  | 
 **payer** | [**Payer**](.md)|  | 
 **payment_method** | **str**|  | 
 **url** | [**Url**](.md)|  | 

### Return type

[**DepositSuccess**](DepositSuccess.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)