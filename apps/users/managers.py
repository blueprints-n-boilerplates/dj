from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError("Email is a required field for users!")
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            last_login=now,
            is_active=True,
            date_registered=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

    # Get

    def get_obj_by_id(self, user_id):
        try:
            user = self.get(id=user_id)

        except self.model.DoesNotExist:
            return None

        else:
            return user

    def get_obj_by_email(self, user_email):
        try:
            user = self.get(email=user_email)

        except self.model.DoesNotExist:
            return None

        else:
            return user
