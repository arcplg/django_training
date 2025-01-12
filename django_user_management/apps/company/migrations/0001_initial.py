# Generated by Django 5.1.4 on 2025-01-11 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("email", models.CharField(max_length=150)),
                ("username", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=255)),
            ],
            options={
                "db_table": "companies",
            },
        ),
    ]