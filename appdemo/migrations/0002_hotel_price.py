# Generated by Django 4.1.7 on 2023-03-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("appdemo", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="hotel",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
