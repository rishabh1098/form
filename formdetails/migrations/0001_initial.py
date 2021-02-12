# Generated by Django 3.0.5 on 2021-02-11 18:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentdetails',
            fields=[
                ('student_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('school', models.CharField(max_length=60)),
                ('board', models.CharField(max_length=60)),
                ('standard', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('category', models.CharField(default='', max_length=200)),
                ('number', models.CharField(max_length=20)),
                ('registerdate', models.DateTimeField(default=datetime.datetime(2021, 2, 11, 18, 0, 50, 425133, tzinfo=utc))),
            ],
        ),
    ]