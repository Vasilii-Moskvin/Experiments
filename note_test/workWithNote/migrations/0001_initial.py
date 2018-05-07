# Generated by Django 2.0.2 on 2018-05-06 13:48

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('username', models.CharField(max_length=64)),
                ('category', models.CharField(max_length=32)),
                ('dt', models.DateField(default=datetime.date.today)),
                ('text', models.TextField()),
            ],
        ),
    ]
