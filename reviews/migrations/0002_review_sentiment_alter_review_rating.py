# Generated by Django 5.0.7 on 2024-07-25 20:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="sentiment",
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name="review",
            name="rating",
            field=models.DecimalField(
                decimal_places=1,
                max_digits=3,
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
            ),
        ),
    ]
