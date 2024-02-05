from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("Users must have an email address.")

        if not username:
            raise ValueError("Users must have an username.")
        
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)




def get_profile_image_filepath(instance, filename):
    return f'profile_images/{instance.email}/{filename}'


def get_default_profile_image():
    return f'profile_images/default_img.png'


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=128, unique=True)
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64, unique=True)
    last_name = models.CharField(max_length=64, unique=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    profile_image = models.ImageField(
        max_length=255,
        upload_to=get_profile_image_filepath,
        default=get_default_profile_image,
        blank=True,
        null=True
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    class Meta:
        ordering = ["-date_joined"]
        verbose_name = "User"
        verbose_name_plural = "Users"
    
    def __str__(self):
        return self.username
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
