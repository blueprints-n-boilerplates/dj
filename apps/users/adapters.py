from allauth.account.adapter import (
    DefaultAccountAdapter,
)

from django.conf import settings
from django.http import HttpRequest


class AccountAdapter(DefaultAccountAdapter):

    def __init__(self, request=None):
        super().__init__(request=request)

    def is_open_for_signup(self, request: HttpRequest):
        return getattr(settings, "ACCOUNT_ALLOW_REGISTRATION", True)

    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_username, user_email, user_field
        data = form.cleaned_data
        first_name = data.get("first_name")
        middle_name = data.get("middle_name")
        last_name = data.get("last_name")
        email = data.get("email")

        user_email(user, email)

        if first_name:
            user_field(user, "first_name", first_name)

        if middle_name:
            user_field(user, "midle_name", middle_name)

        if last_name:
            user_field(user, "last_name", last_name)

        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()

        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
            self.create_one_to_one_related_models(user)
        return user
