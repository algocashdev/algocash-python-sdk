# coding: utf-8

"""
    Algocash API

    This is a Algocash API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: loganph.work@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from algocash_sdk.api_client import ApiClient


class DepositApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_deposit(self, **kwargs):  # noqa: E501
        """create a deposit  # noqa: E501

        create a deposit  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_deposit(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id:
        :param str amount:
        :param Payer payer:
        :param str payment_method:
        :param Url url:
        :return: DepositSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_deposit_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_deposit_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_deposit_with_http_info(self, **kwargs):  # noqa: E501
        """create a deposit  # noqa: E501

        create a deposit  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_deposit_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str invoice_id:
        :param str amount:
        :param Payer payer:
        :param str payment_method:
        :param Url url:
        :return: DepositSuccess
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['invoice_id', 'amount', 'payer', 'payment_method', 'url']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_deposit" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'invoice_id' in params:
            form_params.append(('invoice_id', params['invoice_id']))  # noqa: E501
        if 'amount' in params:
            form_params.append(('amount', params['amount']))  # noqa: E501
        if 'payer' in params:
            form_params.append(('payer', params['payer']))  # noqa: E501
        if 'payment_method' in params:
            form_params.append(('payment_method', params['payment_method']))  # noqa: E501
        if 'url' in params:
            form_params.append(('url', params['url']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeyAuth', 'basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/payin', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DepositSuccess',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
