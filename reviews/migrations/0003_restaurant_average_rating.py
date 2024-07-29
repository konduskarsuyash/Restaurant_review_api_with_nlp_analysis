# Generated by Django 5.0.7 on 2024-07-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0002_review_sentiment_alter_review_rating"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="average_rating",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3),
        ),
    ]
