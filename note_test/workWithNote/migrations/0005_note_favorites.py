# Generated by Django 2.0.2 on 2018-05-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workWithNote', '0004_auto_20180506_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='favorites',
            field=models.BooleanField(default=False),
        ),
    ]
