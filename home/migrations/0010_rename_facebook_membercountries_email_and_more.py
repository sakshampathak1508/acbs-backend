# Generated by Django 4.1.5 on 2023-04-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_executive_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membercountries',
            old_name='facebook',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='executive',
            name='origin_country',
        ),
        migrations.RemoveField(
            model_name='membercountries',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='membercountries',
            name='twitter',
        ),
        migrations.AddField(
            model_name='executive',
            name='email',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='executive',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='membercountries',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='membercountries',
            name='president',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='executives'),
        ),
        migrations.AlterField(
            model_name='executive',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='executive',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='membercountries',
            name='flag',
            field=models.ImageField(blank=True, null=True, upload_to='countries'),
        ),
        migrations.AlterField(
            model_name='membercountries',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
