from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

from service.valid import is_valid_email


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, password, **extra_fields):
        if extra_fields['email']:
            email = extra_fields['email']
            if not is_valid_email(email):
                raise TypeError('Email not valid')
        if not password:
            raise ValueError('Password must be provided')

        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, password=None, **extra_fields):
        return self._create_user(password, **extra_fields)

    def create_superuser(self, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    objects = UserAccountManager()

    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff', default=False)

    email = models.EmailField('email', unique=True, blank=False)
    name = models.CharField('name', max_length=24, blank=False, null=True)

    created_at = models.DateTimeField('Created', auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)

    @property
    def access(self):
        return str(RefreshToken.for_user(self).access_token)

    @property
    def refresh(self):
        return str(RefreshToken.for_user(self))

    def __str__(self):
        return self.name if self.name else str(self.id)
