# Generated by Django 4.1.5 on 2023-01-28 19:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_aboutus_alter_annoucement_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annoucement',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 28, 19, 35, 10, 531673, tzinfo=datetime.timezone.utc)),
        ),
    ]