from unittest import TestCase
from unittest.mock import patch

from rest_framework import status

from cryptprice.adapters.crypto_price_adapter import (
    CryptoPriceAdapter,
    BITFINEX_RESOURCE_URL,
    get_crypto_currency_price,
)
from cryptprice.exceptions.app_exceptions import APPServerError
from cryptprice.utilities.mock_data import FakeRequest


class TestCryptoPriceAdapter(TestCase):
    def setUp(self) -> None:
        self.price = b"[8973.55]"
        self.crypto_adapter = CryptoPriceAdapter()

    @patch("cryptprice.adapters.crypto_price_adapter.requests")
    def test__conn_wrapper_price(self, mock_requests):
        mock_requests.post.return_value = FakeRequest(
            status_code=status.HTTP_200_OK, data=self.price
        )

        price = self.crypto_adapter._conn_wrapper_price(
            crypto_currency="BTC", currency="USD"
        )

        mock_requests.post.assert_called_once_with(
            json={"ccy1": "BTC", "ccy2": "USD"}, url=BITFINEX_RESOURCE_URL
        )

        self.assertEqual(price, float("8973.55"))

    @patch("cryptprice.adapters.crypto_price_adapter.requests")
    def test__conn_wrapper_price_error(self, mock_requests):
        mock_requests.post.return_value = FakeRequest(
            data=self.price, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

        with self.assertRaises(APPServerError) as ex:
            self.crypto_adapter._conn_wrapper_price(
                crypto_currency="TEST", currency="USD"
            )

        mock_requests.post.assert_called_once_with(
            json={"ccy1": "TEST", "ccy2": "USD"}, url=BITFINEX_RESOURCE_URL
        )

        self.assertEqual(str(ex.exception), "Internal server error!")

    @patch("cryptprice.adapters.crypto_price_adapter.requests")
    def test_get_crypto_currency_price(self, mock_requests):
        mock_requests.post.return_value = FakeRequest(
            data=self.price, status_code=status.HTTP_200_OK
        )

        price = get_crypto_currency_price(crypto_currency="BTC", currency="USD")

        mock_requests.post.assert_called_once_with(
            json={"ccy1": "BTC", "ccy2": "USD"}, url=BITFINEX_RESOURCE_URL
        )

        self.assertEqual(price, float("8973.55"))
