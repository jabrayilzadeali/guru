from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.


def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/profile_image.png'


def get_default_profile_image():
    return f'profile_images/default_img.png'


class Account(AbstractBaseUser):
    email = models.EmailField(max_length=70, unique=True)
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, unique=True)
    last_name = models.CharField(max_length=50, unique=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    profile_image = models.ImageField(
        max_length=255,
        upload_to=get_profile_image_filepath,
        blank=True,
        null=True,
        default=get_default_profile_image
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
