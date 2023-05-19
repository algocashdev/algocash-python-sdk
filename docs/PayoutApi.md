# algocash_sdk.PayoutApi

All URIs are relative to *https://virtserver.swaggerhub.com/gitdevstar/Algocash/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payout**](PayoutApi.md#create_payout) | **POST** /payout | create payout

# **create_payout**
> PayoutSuccess create_payout(invoice_id, amount, payer, payment_method, bank_account, url)

create payout

create a payout

### Example
```python
from __future__ import print_function
import time
import algocash_sdk
from algocash_sdk.rest import ApiException
from pprint import pprint
import json

configuration = algocash_sdk.Configuration()
configuration.merchant_key = 'MERCHANT_KEY'
configuration.merchant_secret = 'MERCHANT_SECRET'
configuration.api_access_token = 'API_ACCESS_TOKEN'
configuration.devmode = True # if production, False

# create an instance of the API class
api_instance = algocash_sdk.PayoutApi(algocash_sdk.ApiClient(configuration))
invoice_id = '123412' # str | 
amount = '12' # str | 
payer = algocash_sdk.Payer('email', 'phone number') # Payer | 
payment_method = 'UPI' # str | 
bank_account = algocash_sdk.Bank('bank_account_number', 'bank_code', 'bank_beneficiary') # Bank | 
url = algocash_sdk.Url('callback_url') # Url | 

try:
    # create payout
    api_response = api_instance.create_payout(invoice_id, amount, payer, payment_method, bank_account, url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutApi->create_payout: %s\n" % e)
    pprint(json.loads(e.body))
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | 
 **amount** | **str**|  | 
 **payer** | [**Payer**](.md)|  | 
 **payment_method** | **str**|  | 
 **bank_account** | [**Bank**](.md)|  | 
 **url** | [**Url**](.md)|  | 

### Return type

[**PayoutSuccess**](PayoutSuccess.md)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

