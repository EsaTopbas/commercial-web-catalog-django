# Generated by Django 4.0.2 on 2022-03-04 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_product_variant_images_alter_product_main_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='variant_images',
        ),
    ]
