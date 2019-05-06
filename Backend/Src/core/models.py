from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
                                        PermissionsMixin


class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not username:
            raise ValueError

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, password):
        """Creates and saves a new super user"""
        user = self.create_user(username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    # Determines if the user is online/logged in, or not
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
