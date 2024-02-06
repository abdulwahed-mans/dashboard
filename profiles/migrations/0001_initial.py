# Generated by Django 5.0.1 on 2024-02-06 01:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                    "personal_identity_number",
                    models.CharField(
                        max_length=12,
                        unique=True,
                        verbose_name="Personal Identity Number",
                    ),
                ),
                (
                    "bio",
                    models.TextField(blank=True, null=True, verbose_name="Biography"),
                ),
                (
                    "phone_number",
                    models.CharField(
                        blank=True, max_length=15, verbose_name="Phone Number"
                    ),
                ),
                (
                    "language_preference",
                    models.CharField(
                        choices=[("sv", "Swedish"), ("en", "English")],
                        default="sv",
                        max_length=10,
                        verbose_name="Language Preference",
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Address"
                    ),
                ),
                (
                    "city",
                    models.CharField(blank=True, max_length=50, verbose_name="City"),
                ),
                (
                    "postal_code",
                    models.CharField(
                        blank=True, max_length=10, verbose_name="Postal Code"
                    ),
                ),
                (
                    "profile_picture",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_pics/",
                        verbose_name="Profile Picture",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "last_updated",
                    models.DateTimeField(auto_now=True, verbose_name="Last Updated"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
            },
        ),
    ]
