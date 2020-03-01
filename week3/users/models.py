from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail

# Create your models here.

class AbstractUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=30,
        unique=True,
        validators=[username_validator],
        error_messages={
            'unique': _("This username is already taken"),
            'max_length': _("Too many characters"),
        }
    )
    first_name = models.CharField(
        _('first_name'),
        max_length=30,
        blank=True
    )
    last_name = models.CharField(
        _('last_name'),
        max_length=30,
        blank=True
    )
    email = models.EmailField(
        _('email'),
        blank=True
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False
    )
    is_active = models.BooleanField(
        _('active'),
        default=True
    )

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        abstract = True

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


class CustomUser(AbstractUser):
    pass