# Generated by Django 4.1.5 on 2023-02-06 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_rename_descrtiption_wardrobe_w_descrtiption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wardrobe',
            old_name='w_descrtiption',
            new_name='description',
        ),
    ]
