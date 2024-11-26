from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):

    LICENSE_TYPE_CHOICES = (
        ("Learner", "Learners License Student"),
        ("Driver", "Drivers License Student"),
    )

    LICENSE_CODE_CHOICES = (
        (None, "License Codes"),
        (1, "Code A"),
        (2, "Code B"),
        (3, "Code C"),
        (4, "Code E"),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=60, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    license_type = models.CharField(max_length=50, choices=LICENSE_TYPE_CHOICES, null=True)
    license_code = models.IntegerField(choices=LICENSE_CODE_CHOICES, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'license_type', 'license_code']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

