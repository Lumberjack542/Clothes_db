from django.db import models

# Create your models here.


class Shoes(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=120)
    SHOES_CHOICES_CUT = [
        ('SN', 'Sneakers'),
        ('BO', 'Boots'),
        ('SH', 'SHOES'),
        ('SL', 'Slippers'),
    ]
    cut = models.CharField(max_length=2, choices=SHOES_CHOICES_CUT, null=True)
    
    def __str__(self):
        return f'{self.title}'

