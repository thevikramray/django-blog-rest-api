from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

# Create your models here.

class ProfileUserManager(UserManager):
    """ Profile manager Model """
    def create_user(self, email, first_name, password=None):
        if not email:
            raise ValueError('You Must Provide an Email')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, password=None):
        """ Create a superUser , is_superuser comes from PermissionMixins , is_staff is required"""
        user = self.create_user(email, first_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class ProfileUser(AbstractBaseUser, PermissionsMixin):
    """ Model to store Profile User """
    """ This is custom user model ,add this in setting AUTH_USER_MODEL """
    email = models.EmailField(max_length=128, unique=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, blank=True)
    mobile = models.CharField(max_length=13, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = ProfileUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name']

    def get_full_name(self):
        return '{first_name} {last_name}'.format(self.first_name, self.last_name)
    
    def get_short_name(self):
        return self.first_name

    def __str__(self):
        return self.email