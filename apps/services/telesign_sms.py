from __future__ import print_function

import binascii

import requests.exceptions
from django.conf import settings

from telesign.util import random_with_n_digits
from telesign.messaging import MessagingClient
from telesign.score import ScoreClient

from apps.common.response import GENERIC_ERROR_MSG, UNAUTHORIZED_ERROR_MSG, CONNECTION_ERROR_MSG

# status codes
TELESIGN_SUCCESS_CODE = 290

# msg types
ARN = "ARN"
OTP = "OTP"

# messages
TELESIGN_MSG_WRONG_PHONENO_FORMAT = {"err": "Invalid value for parameter phone_number.", "hints": "Remove + sign."}

# account lifecycle events
TELESIGN_LIFECYCLE_CREATE = "create"


class TeleSignHelper:
    VALID_CODE_MSG = "Your code is valid."
    INVALID_CODE_MSG = "Your code is invalid."

    def __init__(self, customer_id=settings.TELESIGN_CUSTOMER_ID, api_key=settings.TELESIGN_API_KEY):
        self.__messaging_client = self.create_messaging_client(customer_id, api_key)

    def create_messaging_client(self, customer_id: str, api_key: str):
        return MessagingClient(customer_id, api_key)

    def send_msg(self, phone_number, msg, msg_type=ARN):
        try:
            response = self.__messaging_client.message(phone_number, msg, msg_type)

        except binascii.Error:  # Incorrect padding
            return UNAUTHORIZED_ERROR_MSG

        except requests.exceptions.ConnectionError:
            return CONNECTION_ERROR_MSG

        except Exception as err:
            print(err)  # telesign.rest.RestClient.Response object
            return GENERIC_ERROR_MSG

        else:
            # success: response.body
            # {"reference_id": "36051CAB471406689190881F864D0C93", "external_id": null, "status": {"code": 290, "description": "Message in progress"}}

            # fail: response.body
            # {'external_id': None, 'status': {'code': 11000, 'description': 'Invalid value for parameter phone_number.'}}

            return response.json if response.ok else TELESIGN_MSG_WRONG_PHONENO_FORMAT

    # def check_phone_fraud_risk(self, phone_number):
    #     # TODO: add test cases
    #     account_lifecycle_event = "create"
    #
    #     data = ScoreClient(settings.TELESIGN_CUSTOMER_ID, settings.TELESIGN_API_KEY)
    #     response = data.score(phone_number, account_lifecycle_event)
    #
    #     if response.ok:
    #         print("Phone number {} has a '{}' risk level and the recommendation is to '{}' the transaction.".format(
    #             phone_number,
    #             response.json['risk']['level'],
    #             response.json['risk']['recommendation']))

    # TODO: Create own verification tool
    # def send_verification_code(self, phone_number, msg_type=OTP):
    #     verification_code = random_with_n_digits(5)
    #     msg = "Your code is {}".format(verification_code)
    #     return self.send_msg(phone_number, msg, msg_type)

    # def verify_input_code(self, input_code, verification_code):
    #     return self.VALID_CODE_MSG if verification_code == input_code else self.INVALID_CODE_MSG
