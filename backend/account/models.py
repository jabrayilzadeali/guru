from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from .managers import UserManager


# Create your models here.


def get_profile_image_filepath(instance, filename):
    return f"profile_images/{instance.email}/{filename}"


def get_default_profile_image():
    return f"profile_images/default_img.png"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=128, unique=True)
    username = models.CharField(max_length=64, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    profile_image = models.ImageField(
        max_length=255,
        upload_to=get_profile_image_filepath,
        default=get_default_profile_image,
        blank=True,
        null=True,
    )

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        ordering = ["-date_joined"]
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # def save(self, *args, **kwargs):
    #     # Ensure the password is properly set when creating a new user or updating an existing user
    #     if self.pk is None or 'password' in self.__dict__:
    #         self.password = make_password(self.password)
    #     super().save(*args, **kwargs)
