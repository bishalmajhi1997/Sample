# Generated by Django 4.1.4 on 2022-12-24 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app2", "0004_alter_student_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="address",
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
