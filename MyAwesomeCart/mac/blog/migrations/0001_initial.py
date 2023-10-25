# Generated by Django 4.2.6 on 2023-10-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=100)),
                ("post", models.CharField(max_length=1000)),
                ("heading", models.CharField(max_length=500)),
                ("sub_heading", models.CharField(max_length=500)),
                ("pub_date", models.DateField()),
                ("thumbnail", models.ImageField(default="", upload_to="shop/images")),
            ],
        ),
    ]