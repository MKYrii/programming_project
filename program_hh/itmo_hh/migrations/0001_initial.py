# Generated by Django 4.2.11 on 2024-04-09 14:07

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Napravlenie",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Sphere",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Startapps_and_projects",
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
                ("time_published", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=255)),
                (
                    "photo",
                    models.ImageField(
                        blank=True, default="#", upload_to="images/%Y/%m/%d/"
                    ),
                ),
                ("header", models.CharField(max_length=255)),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("no_experience", "Нет опыта"),
                            ("1-3", "1-3 года"),
                            ("3-5", "3-5 лет"),
                            ("5", "5+"),
                        ],
                        max_length=30,
                    ),
                ),
                (
                    "education_level",
                    models.CharField(
                        choices=[
                            ("bakalavriat", "Бакалавриат"),
                            ("magistr", "Магистратура"),
                            ("aspirantyra", "Аспирантура"),
                        ],
                        max_length=100,
                    ),
                ),
                ("content", models.TextField(blank=True)),
                ("file", models.FileField(upload_to="uploads/%Y/%m/%d/")),
                (
                    "applied_users",
                    django.contrib.postgres.fields.ArrayField(
                        base_field=models.IntegerField(blank=True, null=True),
                        blank=True,
                        null=True,
                        size=None,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="itmo_hh.category",
                    ),
                ),
                (
                    "sphere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="itmo_hh.sphere"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Resumes",
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
                ("tittle", models.CharField(max_length=255)),
                ("time_published", models.DateTimeField(auto_now_add=True)),
                ("FIO", models.CharField(max_length=255)),
                ("sex", models.CharField(max_length=30)),
                ("birthday", models.DateField()),
                (
                    "education_level",
                    models.CharField(
                        choices=[
                            ("bakalavriat", "Бакалавриат"),
                            ("magistr", "Магистратура"),
                            ("aspirantyra", "Аспирантура"),
                        ],
                        max_length=100,
                    ),
                ),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("no_experience", "Нет опыта"),
                            ("1-3", "1-3 года"),
                            ("3-5", "3-5 лет"),
                            ("5", "5+"),
                        ],
                        max_length=30,
                    ),
                ),
                ("content", models.TextField(blank=True)),
                ("file", models.FileField(upload_to="uploads/%Y/%m/%d/")),
                (
                    "napravlenie",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="itmo_hh.napravlenie",
                    ),
                ),
                (
                    "sphere",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="itmo_hh.sphere"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="My_otclics_and_offers",
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
                ("time_published", models.DateTimeField(auto_now_add=True)),
                ("status", models.BooleanField(default=False)),
                (
                    "id_offer_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="offer_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "id_to_whom_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="to_whom_user",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Love",
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
                (
                    "id_love_proj",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="itmo_hh.startapps_and_projects",
                    ),
                ),
                (
                    "id_love_res",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="itmo_hh.resumes",
                    ),
                ),
            ],
        ),
    ]
