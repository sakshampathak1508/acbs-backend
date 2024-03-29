# Generated by Django 4.1.5 on 2023-05-16 16:36

from django.db import migrations, models
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0010_rename_facebook_membercountries_email_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.TextField(blank=True)),
                ("bank_details", models.TextField(blank=True)),
                ("name1", models.CharField(blank=True, max_length=200, null=True)),
                ("email1", models.EmailField(blank=True, max_length=200, null=True)),
                ("name2", models.CharField(blank=True, max_length=200, null=True)),
                ("email2", models.EmailField(blank=True, max_length=200, null=True)),
                ("name3", models.CharField(blank=True, max_length=200, null=True)),
                ("email3", models.EmailField(blank=True, max_length=200, null=True)),
                ("name4", models.CharField(blank=True, max_length=200, null=True)),
                ("email4", models.EmailField(blank=True, max_length=200, null=True)),
                ("is_active", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "Contact Us",
                "verbose_name_plural": "Contact Us",
            },
        ),
        migrations.CreateModel(
            name="Download",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=200)),
                (
                    "file",
                    models.FileField(blank=True, null=True, upload_to="home/files"),
                ),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Download Files",
                "verbose_name_plural": "Download Files",
            },
        ),
        migrations.CreateModel(
            name="PastChampion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=200)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="rule/images"),
                ),
                (
                    "caption",
                    models.CharField(blank=True, default="", max_length=100, null=True),
                ),
                ("content", models.TextField(blank=True, null=True)),
                ("slug", models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Rule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", django_quill.fields.QuillField(blank=True)),
            ],
            options={
                "verbose_name": "About Us",
                "verbose_name_plural": "About Us",
            },
        ),
    ]
