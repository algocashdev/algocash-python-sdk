# algocash-sdk
This is a Algocash API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import algocash_sdk 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import algocash_sdk
```

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

# create an instance of the API class
api_instance = algocash_sdk.DepositApi(algocash_sdk.ApiClient(configuration))
invoice_id = 'invoice_id_example' # str | 
amount = 'amount_example' # str | 
payer = algocash_sdk.Payer() # Payer | 
payment_method = 'payment_method_example' # str | 
url = algocash_sdk.Url() # Url | 

try:
    # create a deposit
    api_response = api_instance.create_deposit(invoice_id, amount, payer, payment_method, url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DepositApi->create_deposit: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/gitdevstar/Algocash/1.0.0*

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