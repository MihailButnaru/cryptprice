import json
import logging

import requests
from rest_framework import status

from cryptprice.exceptions.app_exceptions import APPServerError

__author__ = "Mihail Butnaru"
__copyright__ = "2020 All rights reserved!"

_logger = logging.getLogger(__name__)

BITFINEX_RESOURCE_URL = "https://api.bitfinex.com/v2/calc/fx"


class CryptoPriceAdapter:
    @staticmethod
    def _conn_wrapper_price(*, crypto_currency: str, currency: str) -> float:
        """Connection wrapper to call the api"""
        body = {"ccy1": crypto_currency, "ccy2": currency}

        response = requests.post(url=BITFINEX_RESOURCE_URL, json=body)

        if response.status_code == status.HTTP_200_OK:
            return float(json.loads(response.content)[0])

        raise APPServerError(detail="Internal server error!")


crypto_price_adapter = CryptoPriceAdapter()


def get_crypto_currency_price(*, crypto_currency: str, currency: str) -> float:
    """Get the live price data of the crypto currency"""

    price = crypto_price_adapter._conn_wrapper_price(
        crypto_currency=crypto_currency, currency=currency
    )

    return price
