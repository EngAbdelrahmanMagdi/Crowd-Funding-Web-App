<<<<<<< HEAD
# Generated by Django 4.0.4 on 2022-05-07 14:17
=======
# Generated by Django 4.0.4 on 2022-05-06 22:41
>>>>>>> d1c3a4bae26781d098bcc255bf3f83e9727418b8

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ('projects', '0006_merge_20220507_1617'),
=======
        ('projects', '0006_merge_20220507_0015'),
>>>>>>> d1c3a4bae26781d098bcc255bf3f83e9727418b8
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='donations',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=19),
        ),
    ]
