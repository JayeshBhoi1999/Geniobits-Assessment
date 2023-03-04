# Generated by Django 4.1.7 on 2023-03-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_cart', '0015_delete_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('user', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip_code', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('grand_total', models.CharField(max_length=50)),
                ('items_json', models.CharField(max_length=120)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
