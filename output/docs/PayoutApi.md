# algocash_sdk.PayoutApi

All URIs are relative to *https://virtserver.swaggerhub.com/gitdevstar/Algocash/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_payout**](PayoutApi.md#create_payout) | **POST** /payout | create payout

# **create_payout**
> PayoutSuccess create_payout(invoice_id=invoice_id, amount=amount, payer=payer, payment_method=payment_method, bank_account=bank_account, url=url)

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
configuration.api_key['Signature'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Signature'] = 'Bearer'

# create an instance of the API class
api_instance = algocash_sdk.PayoutApi(algocash_sdk.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str |  (optional)
amount = 'amount_example' # str |  (optional)
payer = algocash_sdk.Payer() # Payer |  (optional)
payment_method = 'payment_method_example' # str |  (optional)
bank_account = algocash_sdk.Bank() # Bank |  (optional)
url = algocash_sdk.Url() # Url |  (optional)

try:
    # create payout
    api_response = api_instance.create_payout(invoice_id=invoice_id, amount=amount, payer=payer, payment_method=payment_method, bank_account=bank_account, url=url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PayoutApi->create_payout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**|  | [optional] 
 **amount** | **str**|  | [optional] 
 **payer** | [**Payer**](.md)|  | [optional] 
 **payment_method** | **str**|  | [optional] 
 **bank_account** | [**Bank**](.md)|  | [optional] 
 **url** | [**Url**](.md)|  | [optional] 

### Return type

[**PayoutSuccess**](PayoutSuccess.md)

### Authorization

[basicAuth](../README.md#basicAuth), [signatureAuth](../README.md#signatureAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

