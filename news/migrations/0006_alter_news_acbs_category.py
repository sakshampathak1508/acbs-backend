# Generated by Django 4.1.5 on 2023-01-28 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_news_acbs_category_alter_news_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='acbs_category',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Snooker'), (2, 'Billiards'), (3, '10Red'), (4, '6Red'), (5, 'Team'), (6, 'Juniors'), (7, '8Ball Pool'), (8, '9Ball Pool'), (9, '10Ball Pool'), (10, 'World Cup')], null=True),
        ),
    ]
