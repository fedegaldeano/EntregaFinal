from django.db import models
from django.contrib.auth.models import User

def avatar_upload_path(instance, filename):
    return f'avatars/user_{instance.user_id}/{filename}'

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to=avatar_upload_path, blank=True, null=True)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'
