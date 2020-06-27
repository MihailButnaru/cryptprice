from unittest import TestCase

from django.conf import settings

from cryptprice.utilities import validate_verification_token, verification_challenge


class TestValidators(TestCase):
    def setUp(self) -> None:
        self.input_data = {"token": "test", "type": "url_verification"}
        settings.SLACK_VERIFICATION_TOKEN = "test"

    def test_validate_verification_token(self):
        self.assertTrue(validate_verification_token(data=self.input_data))

    def test_validate_verification_token_failed(self):
        settings.SLACK_VERIFICATION_TOKEN = "error"

        self.assertFalse(validate_verification_token(data=self.input_data))

    def test_verification_challenge(self):
        self.assertTrue(verification_challenge(data=self.input_data))

    def test_verification_challenge_failed(self):
        self.input_data["type"] = "error"

        self.assertFalse(verification_challenge(data=self.input_data))
