# Generated by Django 4.2.5 on 2023-10-06 14:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("online_store_app", "0005_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(default="Сессия установлена.png", upload_to=""),
        ),
    ]
