# algocash-sdk
This is a Algocash API

- API version: 1.0.0
- Package version: 1.0.0

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install
pip install algocash_sdk

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
invoice_id = '12312213' # str | 
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

## Documentation for API Endpoints

Swagger: https://app.swaggerhub.com/apis-docs/gitdevstar/Algocash/1.0.0

BASE_URL: https://testapi2.algorithmic.cash/  for dev

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DepositApi* | [**create_deposit**](docs/DepositApi.md#create_deposit) | **POST** /payin | create a deposit
*PayoutApi* | [**create_payout**](docs/PayoutApi.md#create_payout) | **POST** /payout | create payout

## Documentation For Models

 - [Address](docs/Address.md)
 - [Bank](docs/Bank.md)
 - [CallbackPayload](docs/CallbackPayload.md)
 - [DepositRequest](docs/DepositRequest.md)
 - [DepositSuccess](docs/DepositSuccess.md)
 - [Error](docs/Error.md)
 - [Payer](docs/Payer.md)
 - [PayoutRequest](docs/PayoutRequest.md)
 - [PayoutSuccess](docs/PayoutSuccess.md)
 - [Url](docs/Url.md)

 ### Author
https://github.com/gitdevstar