# Generated by Django 4.1.5 on 2023-01-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=120)),
                ('cut', models.CharField(choices=[('SN', 'Sneakers'), ('BO', 'Boots'), ('SH', 'SHOES'), ('SL', 'Slippers')], max_length=2, null=True)),
            ],
        ),
    ]
