from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    username = models.CharField(max_length=120, unique=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    register_data = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.username}, {self.first_name}  {self.last_name}'


