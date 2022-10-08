# Generated by Django 4.0.3 on 2022-06-08 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('home_group', models.CharField(max_length=5)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
