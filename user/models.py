from enum import unique
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
   
    def create_user(self, *args, **kwargs):
        email = kwargs.get('email')
        
        if not email:
            raise ValueError('no email address was given!')
        
        email = self.normalize_email(email)

        user = self.model(
                        username=kwargs.get('username'),
                        name=kwargs.get('name'),
                        email=email
                    )
        user.set_password(kwargs.get('password'))
        user.save(using=self._db)

        return user

    def create_superuser(self, *args, **kwargs):
        user = self.create_user(*args,**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, null=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username