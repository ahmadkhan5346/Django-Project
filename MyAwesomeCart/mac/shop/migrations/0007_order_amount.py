# Generated by Django 4.2.6 on 2023-10-25 06:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0006_orderupdate_alter_product_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="amount",
            field=models.IntegerField(default=0),
        ),
    ]
