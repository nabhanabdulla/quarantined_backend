# Generated by Django 3.0.4 on 2020-03-15 13:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("management", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Crisis",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("active", models.BooleanField(default=True)),
                ("started_at", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Participant",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("HL", "Helper"),
                            ("AF", "Affected"),
                            ("AU", "Authorities"),
                            ("TP", "Third Parties"),
                        ],
                        max_length=2,
                    ),
                ),
                ("first_line_of_address", models.CharField(max_length=255)),
                ("second_line_of_address", models.CharField(max_length=255)),
                ("country", django_countries.fields.CountryField(max_length=2)),
                (
                    "place_id",
                    models.CharField(
                        max_length=150, verbose_name="Place id from Google"
                    ),
                ),
                (
                    "latitude",
                    models.CharField(
                        max_length=15, verbose_name="Latitude of the user"
                    ),
                ),
                (
                    "longitude",
                    models.CharField(
                        max_length=15, verbose_name="Longitude of the user"
                    ),
                ),
                (
                    "post_code",
                    models.CharField(max_length=10, verbose_name="Postal code"),
                ),
                ("city", models.CharField(max_length=40, verbose_name="City")),
                (
                    "phone",
                    phone_field.models.PhoneField(
                        blank=True, help_text="Contact phone number", max_length=31
                    ),
                ),
                ("is_available", models.BooleanField(default=True)),
                ("abilities", models.ManyToManyField(to="management.Ability")),
                (
                    "crisis",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE, to="crisis.Crisis"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]