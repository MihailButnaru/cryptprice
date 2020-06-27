from django.conf import settings

__author__ = "Mihail Butnaru"
__copyright__ = "2020 All rights reserved!"


def validate_verification_token(data: dict) -> bool:
    return data.get("token") == settings.SLACK_VERIFICATION_TOKEN


def verification_challenge(data: dict) -> bool:
    return data.get("type") == "url_verification"
