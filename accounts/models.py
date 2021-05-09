from django.contrib.auth.models import AbstractUser
from django.db import models


class SiteUser(AbstractUser):
    """User Model for Authentication"""
    is_admin = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

    class Meta:
        db_table = "site_user_accounts"
        ordering = ["pk"]

    def __str__(self):
        return self.username
