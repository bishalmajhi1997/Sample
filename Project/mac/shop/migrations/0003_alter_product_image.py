# Generated by Django 3.2 on 2022-09-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220907_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
    ]
