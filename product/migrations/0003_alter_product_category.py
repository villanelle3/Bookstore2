# Generated by Django 5.0 on 2023-12-13 01:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0002_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ManyToManyField(
                default="Sem categoria", to="product.category"
            ),
        ),
    ]
