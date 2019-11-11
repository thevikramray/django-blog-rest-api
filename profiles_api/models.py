from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.conf import settings


"""
    by default all models have manager class i.e. YOURMODEL.objects is defailt manager for all model
"""

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

"""
    null=True sets NULL (versus NOT NULL) on the column in your DB. Blank values for Django field types 
    such as DateTimeField or ForeignKey will be stored as NULL in the DB.

    blank=True determines whether the field will be required in forms. This includes the 
    admin and your own custom forms. If blank=True then the field will not be required, whereas 
    if it's False the field cannot be blank.
    The combo of the two is so frequent because typically if you're going to allow a field 
    to be blank in your form, you're going to also need your database to allow NULL values
    for that field. The exception is CharFields and TextFields, which in Django are never 
    saved as NULL. Blank values are stored in the DB as an empty string ('').
"""

"""
        As currently implemented, setting auto_now(update everytime if the obj is edited, means it will also be created when the obj i also created or auto_now_add(will be only be created at start) to True will cause the field to have 
        editable=False and blank=True set.
"""
class UserBlogpostModel(models.Model):
    """Model for user saving user Blogpost """
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=256, blank=False, null=False)
    content = models.CharField(max_length=10000, blank=False, null=False)
