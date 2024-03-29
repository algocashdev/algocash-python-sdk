# coding: utf-8

"""
    Algocash API

    This is a Algocash API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: loganph.work@gmail.com
    
"""

from __future__ import absolute_import

import copy
import logging
import multiprocessing
import sys
import urllib3
import hashlib
import json
import hmac

import six
from six.moves import http_client as httplib


class TypeWithDefault(type):
    def __init__(cls, name, bases, dct):
        super(TypeWithDefault, cls).__init__(name, bases, dct)
        cls._default = None

    def __call__(cls):
        if cls._default is None:
            cls._default = type.__call__(cls)
        return copy.copy(cls._default)

    def set_default(cls, default):
        cls._default = copy.copy(default)


class Configuration(six.with_metaclass(TypeWithDefault, object)):
    """.

    Ref: https://github.com/swagger-api/swagger-codegen
    Do not edit the class manually.
    """

    def __init__(self):
        """Constructor"""
        self.devmode = False
        # Default Base url
        self.host = "https://testapi2.algorithmic.cash" if self.devmode else "https://apiv2.algorithmic.cash"
        # Temp file folder for downloading files
        self.temp_folder_path = None

        # Authentication Settings
        # generate signature
        self.api_access_token = ""
        # merchant_key for HTTP basic authentication
        self.merchant_key = ""
        # merchant_secret for HTTP basic authentication
        self.merchant_secret = ""
        
        self.header_params = {}
        # HTTP header `Accept`
        self.header_params['Accept'] = 'application/json'

        # HTTP header `Content-Type`
        self.header_params['Content-Type'] = 'application/json'

        # Authentication setting
        self.auths = ['basicAuth', 'signatureAuth']  # noqa: E501
        
        # Logging Settings
        self.logger = {}
        self.logger["package_logger"] = logging.getLogger("algocash_sdk")
        self.logger["urllib3_logger"] = logging.getLogger("urllib3")
        # Log format
        self.logger_format = '%(asctime)s %(levelname)s %(message)s'
        # Log stream handler
        self.logger_stream_handler = None
        # Log file handler
        self.logger_file_handler = None
        # Debug file location
        self.logger_file = None
        # Debug switch
        self.debug = False

        # SSL/TLS verification
        # Set this to false to skip verifying SSL certificate when calling API
        # from https server.
        self.verify_ssl = True
        # Set this to customize the certificate file to verify the peer.
        self.ssl_ca_cert = None
        # client certificate file
        self.cert_file = None
        # client key file
        self.key_file = None
        # Set this to True/False to enable/disable SSL hostname verification.
        self.assert_hostname = None

        # urllib3 connection pool's maximum number of connections saved
        # per pool. urllib3 uses 1 connection as default value, but this is
        # not the best value when you are making a lot of possibly parallel
        # requests to the same host, which is often the case here.
        # cpu_count * 5 is used as default value to increase performance.
        self.connection_pool_maxsize = multiprocessing.cpu_count() * 5

        # Proxy URL
        self.proxy = None
        # Safe chars for path_param
        self.safe_chars_for_path_param = ''

    @property
    def logger_file(self):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        return self.__logger_file

    @logger_file.setter
    def logger_file(self, value):
        """The logger file.

        If the logger_file is None, then add stream handler and remove file
        handler. Otherwise, add file handler and remove stream handler.

        :param value: The logger_file path.
        :type: str
        """
        self.__logger_file = value
        if self.__logger_file:
            # If set logging file,
            # then add file handler and remove stream handler.
            self.logger_file_handler = logging.FileHandler(self.__logger_file)
            self.logger_file_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_file_handler)
                if self.logger_stream_handler:
                    logger.removeHandler(self.logger_stream_handler)
        else:
            # If not set logging file,
            # then add stream handler and remove file handler.
            self.logger_stream_handler = logging.StreamHandler()
            self.logger_stream_handler.setFormatter(self.logger_formatter)
            for _, logger in six.iteritems(self.logger):
                logger.addHandler(self.logger_stream_handler)
                if self.logger_file_handler:
                    logger.removeHandler(self.logger_file_handler)

    @property
    def debug(self):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        return self.__debug

    @debug.setter
    def debug(self, value):
        """Debug status

        :param value: The debug status, True or False.
        :type: bool
        """
        self.__debug = value
        if self.__debug:
            # if debug status is True, turn on debug logging
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.DEBUG)
            # turn on httplib debug
            httplib.HTTPConnection.debuglevel = 1
        else:
            # if debug status is False, turn off debug logging,
            # setting log level to default `logging.WARNING`
            for _, logger in six.iteritems(self.logger):
                logger.setLevel(logging.WARNING)
            # turn off httplib debug
            httplib.HTTPConnection.debuglevel = 0

    @property
    def logger_format(self):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        return self.__logger_format

    @logger_format.setter
    def logger_format(self, value):
        """The logger format.

        The logger_formatter will be updated when sets logger_format.

        :param value: The format string.
        :type: str
        """
        self.__logger_format = value
        self.logger_formatter = logging.Formatter(self.__logger_format)

    def get_basic_auth_token(self):
        """Gets HTTP basic authentication header (string).

        :return: The token for basic HTTP authentication.
        """
        if self.merchant_key == '' or self.merchant_secret == '':
            raise ValueError("Missing the required merchant_key and merchant_secret")
        
        return urllib3.util.make_headers(
            basic_auth=self.merchant_key + ':' + self.merchant_secret
        ).get('authorization')
    
    def generateSignature(self, post_params):
        
        if self.api_access_token == '':
            raise ValueError("Missing the required api_access_token")
        
        signature = hmac.new(self.api_access_token.encode('utf-8'), json.dumps(post_params, separators=(',', ':')).encode('utf-8'), hashlib.sha256).hexdigest()
        return signature
    
    def get_host(self):
        return "https://testapi2.algorithmic.cash" if self.devmode else self.host

    def auth_settings(self, auth, post_params):
        """Gets Auth Settings dict for api client.

        :return: The Auth Settings information dict.
        """
        
        return {
                    'type': 'basic',
                    'in': 'header',
                    'key': 'Authorization',
                    'value': self.get_basic_auth_token()
                } if auth == 'basicAuth' else {
                        'type': 'api_key',
                        'in': 'header',
                        'key': 'Signature',
                        'value': self.generateSignature(post_params)
                    }
                

    def to_debug_report(self):
        """Gets the essential information for debugging.

        :return: The report for debugging.
        """
        return "Python SDK Debug Report:\n"\
               "OS: {env}\n"\
               "Python Version: {pyversion}\n"\
               "Version of the API: 1.0.0\n"\
               "SDK Package Version: 1.0.0".\
               format(env=sys.platform, pyversion=sys.version)
