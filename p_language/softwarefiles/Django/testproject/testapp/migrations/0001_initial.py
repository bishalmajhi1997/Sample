# Generated by Django 4.0.3 on 2022-04-14 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=200)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=200)),
            ],
        ),
    ]
