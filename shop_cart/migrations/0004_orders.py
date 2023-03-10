# Generated by Django 4.1.7 on 2023-03-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_cart', '0003_product_desc_product_product_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('Email', models.CharField(max_length=90)),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=90)),
                ('state', models.CharField(max_length=90)),
                ('zipcode', models.CharField(max_length=90)),
            ],
        ),
    ]
