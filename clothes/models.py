
from django.db import models

import user.models


# Create your models here.


class Shoes(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    SHOES_CHOICES_CUT = [
        ('SN', 'Sneakers'),
        ('BO', 'Boots'),
        ('SH', 'SHOES'),
        ('SL', 'Slippers'),
    ]
    cut = models.CharField(max_length=2, choices=SHOES_CHOICES_CUT, null=True)
    owner = models.ForeignKey(user.models.CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.title}'

