from .settings import *


# Sendgrid

SG_API_KEY = env("SG_API_KEY")


# TeleSign

TELESIGN_API_KEY = env("TELESIGN_API_KEY")
TELESIGN_CUSTOMER_ID = env("TELESIGN_CUSTOMER_ID")


# Twilio

# TWILIO_ACCOUNT_SID = env("TWILIO_ACCOUNT_SID", default="")
# TWILIO_AUTH_TOKEN = env("TWILIO_AUTH_TOKEN", default="")
# TWILIO_PHONE_NUMBER = env("TWILIO_PHONE_NUMBER", default="")
# TWILIO_SK_API_SID = env("TWILIO_SK_API_SID", default="")
# TWILIO_SK_API_SECRET = env("TWILIO_SK_API_SECRET", default="")
# TWILIO_PHONE_VERIFY_SERVICE_ID = env("TWILIO_PHONE_VERIFY_SERVICE_ID", default="")
# TWILIO_LOGIN_VERIFY_SERVICE_ID = env("TWILIO_LOGIN_VERIFY_SERVICE_ID", default="")
# # for non-chat participants (sms, mms, whatsapp)
# TWILIO_MSGG_SERVICE_SID = env("TWILIO_MSGG_SERVICE_SID", default="")
# TWILIO_CONVERSATIONS_SERVICE_SID = env("TWILIO_CONVERSATIONS_SERVICE_SID", default="")

# CSRF
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-hsts-include-subdomains
# TODO: set this to 60 seconds first and then to 518400 once you prove the former works
SECURE_HSTS_SECONDS = 60
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF =True
