# Generated by Django 4.1.5 on 2023-05-06 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_show_on_front'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]