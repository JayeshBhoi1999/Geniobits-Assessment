# Generated by Django 4.1.7 on 2023-03-02 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_cart', '0006_rename_email_orders_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.CharField(max_length=90),
        ),
    ]
