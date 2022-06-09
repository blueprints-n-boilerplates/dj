import unittest

from django.conf import settings

from apps.common.response import UNAUTHORIZED_ERROR_MSG
from apps.services.telesign_sms import ARN, OTP, TeleSignHelper, TELESIGN_MSG_WRONG_PHONENO_FORMAT, \
    TELESIGN_SUCCESS_CODE


class TestTeleSignSMS(unittest.TestCase):
    test_msg = "You're scheduled for a dentist appointment at 2:30PM."

    def setUp(self) -> None:
        self._telesign_helper = TeleSignHelper()
        super(TestTeleSignSMS, self).setUp()

    def test_send_success(self):
        self.assertTrue(True)
        response = self._telesign_helper.send_msg(settings.TEST_PHONE_NUMBER, self.test_msg, ARN)
        self.assertEqual(response["status"]["code"], TELESIGN_SUCCESS_CODE)

    def test_send_unauthorized(self):
        api_key = "wrongAPIkey"
        telesign_helper = TeleSignHelper(api_key=api_key)
        response = telesign_helper.send_msg(settings.TEST_PHONE_NUMBER, self.test_msg, ARN)
        self.assertEqual(response, UNAUTHORIZED_ERROR_MSG)

    def test_invalid_phoneno_format(self):
        phone_number = "xxxxxxxxx"
        response = self._telesign_helper.send_msg(phone_number, self.test_msg, ARN)
        self.assertEqual(response, TELESIGN_MSG_WRONG_PHONENO_FORMAT)

    # TODO: Create own verification tool
    # def test_verify_success(self):
    #     response = self._telesign_helper.send_verification_code(settings.TEST_PHONE_NUMBER)
    #     print(response)

        # self.assertEqual(response, response)

    # def test_verify_fail(self):
    #     response = self._telesign_helper.send_verification_code(settings.TEST_PHONE_NUMBER)
    #     print(response)
    #
    #     self.assertIsNot(response, None)


if __name__ == '__main__':
    unittest.main()
