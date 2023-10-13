# Generated by Django 4.2.6 on 2023-10-12 14:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0003_contact"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                ("order_id", models.AutoField(primary_key=True, serialize=False)),
                ("items_json", models.CharField(default="", max_length=5000)),
                ("name", models.CharField(default="", max_length=200)),
                ("email", models.CharField(default="", max_length=200)),
                ("address", models.CharField(default="", max_length=200)),
                ("city", models.CharField(default="", max_length=200)),
                ("state", models.CharField(default="", max_length=200)),
                ("zip_code", models.CharField(default="", max_length=200)),
                ("phone", models.CharField(default="", max_length=15)),
            ],
        ),
    ]