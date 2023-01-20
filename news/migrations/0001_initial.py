# Generated by Django 4.1.5 on 2023-01-17 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('category', models.PositiveIntegerField(choices=[(1, 'LATEST'), (2, 'FEATURED')])),
                ('acbs_category', models.PositiveIntegerField(blank=True, choices=[(1, 'World Snooker'), (2, 'World Billiards'), (3, 'World 6Reds'), (4, 'World Team'), (5, 'World U21'), (6, 'World U18'), (7, 'World U17'), (8, 'World U16'), (9, 'World Cup')], null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/images')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('year', models.CharField(max_length=4)),
                ('views', models.IntegerField(default=0)),
                ('content', models.TextField(blank=True)),
                ('slug', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
    ]
