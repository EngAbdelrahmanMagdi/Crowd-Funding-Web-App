# Generated by Django 4.0.4 on 2022-05-07 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_project_donations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='donations',
        ),
    ]