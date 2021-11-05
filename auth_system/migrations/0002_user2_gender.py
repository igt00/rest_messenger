# Generated by Django 3.2.2 on 2021-11-05 17:57

from django.db import migrations, models
from django_add_default_value import AddDefaultValue


class Migration(migrations.Migration):

    dependencies = [
        ('auth_system', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user2',
            name='gender',
            field=models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], default='male', max_length=20),
        ),
        AddDefaultValue(
            model_name='user2',
            name='gender',
            value='male',
        ),
    ]