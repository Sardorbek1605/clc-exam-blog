

# from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models
# from django.utils import timezone


MALE = "male"
FEMALE = "female"
OTHER = "other"
USER_GENDERS = (
    (MALE, "male"),
    (FEMALE, "female"),
    (OTHER, "other"),
)


class User(AbstractUser):
    INVALID_CODE = "######"

    full_name = models.CharField(("full name"), max_length=256)
    email = models.EmailField(
        ("email"),
        unique=True,
        error_messages={
            "error": ("Bunday email mavjud."),
        },
        null=True
    )
    created_at = models.DateTimeField(("date created"), auto_now_add=True, null=True)
    updated_at = models.DateTimeField(("date updated"), auto_now=True)
    date_of_birth = models.DateField(verbose_name="Date of birth", auto_now=True)
    website = models.CharField(max_length=120, null=True)
    location = models.CharField(max_length=255, null=True)
    bio = models.TextField
    phone = models.CharField(max_length=30, null=True)
    facebook_accaunt = models.CharField(max_length=120, null=True)
    twitter_accaunt = models.CharField(max_length=120, null=True)
    instagram_accaunt = models.CharField(max_length=120, null=True)
    followers_count = models.BigIntegerField(default=0)
    following_count = models.BigIntegerField(default=0)
    photo_avatar = models.ImageField(upload_to='user/avatar/', null=True)
    photo_bg = models.ImageField(upload_to='user/background/', null=True)
    is_active = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    gender = models.CharField(max_length=15, choices=USER_GENDERS, null=True)
    last_login = models.DateTimeField(null=True)

    # SETTINGS
    USERNAME_FIELD = "email"
    first_name = None
    last_name = None
    REQUIRED_FIELDS = ["username", "full_name"]

    def __str__(self):
        return f"{self.email}"

    class Meta:
        db_table = "user"
        swappable = "AUTH_USER_MODEL"
        verbose_name = ("user")
        verbose_name_plural = ("users")
