from django.db import models
from django.contrib.auth.models import AbstractUser


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.username, filename)

class UserProfile(AbstractUser):
    is_manager = models.BooleanField(default=False)
    profile_pic = models.ImageField(upload_to=user_directory_path)

    def user_is_manager(self):
        return self.is_manager

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "UserProfile"
        verbose_name_plural = "Userprofile's"


