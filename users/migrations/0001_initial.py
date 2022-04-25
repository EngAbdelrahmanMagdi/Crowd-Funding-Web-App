# Generated by Django 4.0.4 on 2022-04-25 00:44

import django.core.validators
from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32, validators=[django.core.validators.RegexValidator(message='Password must be combination of Uppercase, Lowercase, Special Characters and Digits.', regex='^(?=.*\\d)(?=.*[a-z])(?=.*[A-Z])[a-zA-Z\\d@$.!%*#?&]')])),
                ('mobile_phone', models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message='Invalid Phone Number.', regex='^01[0125][0-9]{8}$')])),
                ('profile_picture', models.ImageField(upload_to='Crowd-Funding-Web-App/users/static/images')),
                ('birthday', models.DateField(null=True)),
                ('fb_profile', models.URLField(null=True)),
                ('country', django_countries.fields.CountryField(max_length=2, null=True)),
            ],
        ),
    ]