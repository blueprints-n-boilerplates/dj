from django.conf import settings
from unittest import TestCase, main
from python_http_client.client import Response

from apps.common.response import UNAUTHORIZED_ERROR_MSG
from apps.services.sg import SendgridHelper


class TestSendgridHelper(TestCase):
    test_subject = "Sending with SendGrid is Fun"
    test_content_msg = "and easy to do anywhere, even with Python"

    def test_send(self):
        sg_helper = SendgridHelper()
        test_from_email = settings.TEST_FROM_EMAIL
        test_to_email = settings.TEST_TO_EMAIL
        test_send_mail = sg_helper.send_mail(test_from_email, test_to_email, self.test_subject, self.test_content_msg)
        self.assertTrue(isinstance(Response, test_send_mail))

    def test_unauthorized(self):
        sg_helper = SendgridHelper(api_key="SG.test")
        test_from_email = settings.TEST_FROM_EMAIL
        test_to_email = settings.TEST_TO_EMAIL
        test_send_mail = sg_helper.send_mail(test_from_email, test_to_email, self.test_subject, self.test_content_msg)
        self.assertEqual(test_send_mail, UNAUTHORIZED_ERROR_MSG)


if __name__ == "__main__":
    main()
