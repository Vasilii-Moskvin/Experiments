# Generated by Django 2.0.2 on 2018-05-06 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workWithNote', '0003_auto_20180506_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='dt',
            field=models.DateField(auto_now=True),
        ),
    ]