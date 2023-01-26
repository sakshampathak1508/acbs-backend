# Generated by Django 4.1.5 on 2023-01-21 05:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='sponser/image')),
                ('url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='annoucements',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 21, 5, 50, 12, 894722, tzinfo=datetime.timezone.utc)),
        ),
    ]
