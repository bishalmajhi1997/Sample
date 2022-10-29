# Generated by Django 4.0.3 on 2022-06-20 08:16

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialGift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=30, verbose_name='title or name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=30, verbose_name='title or name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='gift/voucher')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoucherOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='gift.voucher')),
            ],
        ),
    ]