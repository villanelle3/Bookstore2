# Generated by Django 5.0 on 2023-12-13 01:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(blank=True, null=True, to="product.category"),
        ),
    ]
