# Generated by Django 4.1.1 on 2023-09-01 21:37

from django.db import migrations, models
import django.db.models.deletion
import series.models


class Migration(migrations.Migration):

    dependencies = [
        ("series", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comments",
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
                ("comment", models.CharField(max_length=255)),
                ("created_at", series.models.DateTimeWithoutTZField(auto_now_add=True)),
                ("updated_at", series.models.DateTimeWithoutTZField(auto_now=True)),
                (
                    "episode",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="series.episode"
                    ),
                ),
                (
                    "season",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="series.season"
                    ),
                ),
            ],
        ),
    ]
