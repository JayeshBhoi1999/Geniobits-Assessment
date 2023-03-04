# Generated by Django 4.1.7 on 2023-03-01 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=50)),
                ('p_img_1', models.ImageField(default='', upload_to='static/images/')),
                ('product_price', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]