from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class Address(models.Model):
    address_line_1 = models.CharField(max_length=50, default="")
    address_line_2 = models.CharField(max_length=50, default="", blank=True)
    city_town = models.CharField(max_length=50, default="")
    state_province = models.CharField(max_length=50, default="")
    country = models.CharField(max_length=50, default="")
    zip = models.CharField(max_length=50, default="")

    class Meta:
        verbose_name_plural = "addresses"

    def get_complete_address(self):
        return f"{self.address_line_1} {self.address_line_2}, " \
               f"{self.city_town}, {self.state_province}, {self.country}, {self.zip}"


class User(AbstractBaseUser, PermissionsMixin):
    # GENDER
    FEMALE = "F"
    MALE = "M"
    NON_BINARY = "NB"
    GENDER_CHOICES = [
        (FEMALE, "Female"),
        (MALE, "Male"),
        (NON_BINARY, "Non-binary"),
    ]

    first_name = models.CharField(default="", blank=True, max_length=50)
    middle_name = models.CharField(default="", blank=True, max_length=50)
    last_name = models.CharField(default="", blank=True, max_length=50)
    email = models.EmailField(blank=False, null=True, unique=True, max_length=100)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    # set to false if user is terminated or prohibited to access the site and ifreelance services
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False, blank=True,)
    last_login = models.DateTimeField(null=True, blank=True)
    date_registered = models.DateTimeField(auto_now_add=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    gender = models.CharField(max_length=2, default="", blank=True, choices=GENDER_CHOICES, )
    primary_address = models.ForeignKey(
        "users.Address",
        related_name="primary_address",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    objects = UserManager()

    def get_absolute_url(self):
        return f"/users/{self.pk}"


class AccountSettings(models.Model):
    enable_2fa = models.BooleanField(default=False)
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "account settings"

