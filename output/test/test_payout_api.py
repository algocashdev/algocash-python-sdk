# coding: utf-8

"""
    Algocash API

    This is a Algocash API  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: loganph.work@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import algocash_sdk
from algocash_sdk.api.payout_api import PayoutApi  # noqa: E501
from algocash_sdk.rest import ApiException


class TestPayoutApi(unittest.TestCase):
    """PayoutApi unit test stubs"""

    def setUp(self):
        self.api = PayoutApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_payout(self):
        """Test case for create_payout

        create payout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
