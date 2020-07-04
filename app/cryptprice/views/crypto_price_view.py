import logging

from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from slack import WebClient

from cryptprice.adapters import get_crypto_currency_price
from cryptprice.utilities import (
    validate_verification_token,
    CRYPTO_CURRENCY,
    verification_challenge
)

__author__ = "Mihail Butnaru"
__copyright__ = "2020 All rights reserved!"

_logger = logging.getLogger(__name__)

Client = WebClient(settings.SLACK_BOT_USER_OAUTH_ACCESS_TOKEN)


class CryptoPriceView(APIView):
    def post(self, request):
        """CryptoPriceView will get the data from third party provider and will
        notify the user with the latest live price of the currency chosen """
        input_data = request.data

        token = validate_verification_token(data=input_data)

        if not token:
            return Response(status=status.HTTP_403_FORBIDDEN)

        verification = verification_challenge(data=input_data)

        if verification:
            return Response(status=status.HTTP_200_OK, data=input_data)

        # necessary in order to get the message from each event
        events = input_data.get("event", None)

        if not events:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        slack_message = events.get("text", None)

        if not slack_message:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Client.chat_postEphemeral(
            user=events["user"],
            channel=events["channel"],
            text=f"Choose what crypto-currency price you want to see ['BTC', 'ETH', 'XRP']",
        )

        if slack_message.upper() in CRYPTO_CURRENCY:
            Client.chat_postMessage(
                text=f"Thank you for choosing to see the price of {slack_message}!",
                channel=events["channel"],
            )

            usd_price = get_crypto_currency_price(
                crypto_currency=slack_message, currency="USD"
            )

            Client.chat_postMessage(
                text=f"Current price in USD of the {slack_message.upper()}: ${usd_price}",
                channel=events["channel"],
            )

            gbp_price = get_crypto_currency_price(
                crypto_currency=slack_message, currency="GBP"
            )
            Client.chat_postMessage(
                text=f"Current price in GBP of the {slack_message.upper()}: £{gbp_price}",
                channel=events["channel"],
            )

            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_200_OK)
