# Generated by Django 4.1.5 on 2023-04-30 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_acbs_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='show_on_front',
            field=models.BooleanField(default=False),
        ),
    ]