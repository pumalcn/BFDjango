from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models

class MainUser(AbstractUser):

    is_store_admin = models.BooleanField(default=False)
    is_guest = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):

        return f'{self.id}: {self.username}'


class Profile(models.Model):
    user = models.OneToOneField(MainUser, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500)
    address = models.CharField(max_length=300)
    avatar = models.FileField(null=True)

    def __str__(self):
        return self.user.username