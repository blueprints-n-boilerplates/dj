import sendgrid

from django.conf import settings
from python_http_client.exceptions import UnauthorizedError

from sendgrid.helpers.mail import Mail, Content, To, Email

from apps.common.response import UNAUTHORIZED_ERROR_MSG


class SendgridHelper:
    DEFAULT_CONTENT_TYPE = "text/plain"

    def __init__(self, api_key=settings.SG_API_KEY):
        self.sendgrid_client = self.__build_client(api_key)
        super(SendgridHelper, self).__init__()

    def __build_client(self, api_key):
        return sendgrid.SendGridAPIClient(api_key=api_key)

    def mail_builder(self, from_email: str, to_email: str, subject: str, msg: str,
                     content_type: str) -> Mail:
        # build header
        from_email = Email(from_email)
        to_email = To(to_email)
        # build mail
        content = Content(content_type, msg)
        mail = Mail(from_email, to_email, subject, content)
        return mail

    def get_response(self, mail: Mail):
        try:
            # from python_http_client.client import Response
            response = self.sendgrid_client.client.mail.send.post(request_body=mail.get())

        except UnauthorizedError:
            return UNAUTHORIZED_ERROR_MSG

        else:
            # print(response.status_code)
            # print(response.body)
            # print(response.headers)
            return response

        finally:
            pass

    def send_mail(self, from_email: str, to_email: str, subject: str, msg: str, content_type=DEFAULT_CONTENT_TYPE):
        mail = self.mail_builder(from_email, to_email, subject, msg, content_type)
        return self.get_response(mail)
