# Generated by Django 4.1.7 on 2023-03-02 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_cart', '0009_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
    ]