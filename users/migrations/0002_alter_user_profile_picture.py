# Generated by Django 4.0.4 on 2022-05-08 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_picture',
            field=models.ImageField(upload_to='users/static/users/images'),
        ),
    ]