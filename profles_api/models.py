from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """Model Manager for UserProfile Model"""

    def create_user(self, email, name, password=None):
        """Creates a user for a profile"""
        if not email and not name:
            raise ValueError("Email or name is not valid")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """Creates a super user for a profile"""
        super_user = self.create_user(email, name, password)
        super_user.is_superuser = True
        super_user.is_staff = True
        super_user.save(using=self._db)
        return super_user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Django Model for User Profiles"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """ Returns name of User Profile"""
        return self.name

    def get_short_name(self):
        """Return name of User Profile"""
        return self.name

    def __str__(self):
        """String of User Profile Model"""
        return self.email
