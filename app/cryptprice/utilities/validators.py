from django.conf import settings

__author__ = "Mihail Butnaru"
__copyright__ = "2020 All rights reserved!"


def validate_verification_token(data: dict) -> bool:
    """ Validates the verification token from slack """
    return data.get("token") == settings.SLACK_VERIFICATION_TOKEN


def verification_challenge(data: dict) -> bool:
    """ Slack sends a verification challenge in order to
    connect with their slack platform (verification done)"""
    return data.get("type") == "url_verification"
