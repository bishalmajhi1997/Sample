# Generated by Django 4.0.3 on 2022-06-20 08:16

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import event.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=30, verbose_name='title or name')),
                ('status', models.CharField(choices=[('in_review', 'In Review'), ('active', 'Active'), ('completed', 'Completed'), ('cancelled', 'Cancelled'), ('pending', 'Pending')], default='pending', max_length=15)),
                ('advance_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
                ('is_paid', models.BooleanField(default=False, help_text='check is advanced amount is paid or not')),
                ('total_invitation', models.IntegerField(default=0, help_text='is just for the record to get just idea of how many invitees are coming')),
                ('closure_date', models.DateField(blank=True, help_text='date of when the event is completed', null=True)),
                ('register_date', models.DateField(help_text='date of when the event going to occur')),
                ('approval_date', models.DateTimeField(blank=True, help_text='date time of when the event is approved', null=True)),
                ('other_event_type_title', models.CharField(blank=True, help_text='incase if the other type of the event type is we have then we store here that name', max_length=30, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventAttendingQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='event/attending-qr')),
                ('attending_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='EventGift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_gift', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
                ('voucher_gift', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
                ('special_gift', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='EventGreetings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('greetings', models.TextField(verbose_name='greeting/blessing')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('cancellation_reasons', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('event_host_type', models.CharField(choices=[('owner', 'Owner'), ('co_host', 'Co-host')], max_length=10)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=event.models.event_upload_dir)),
            ],
        ),
        migrations.CreateModel(
            name='EventPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('advance', 'Advance'), ('cash', 'Cash'), ('voucher', 'Voucher'), ('special_gift', 'Special gift')], db_index=True, max_length=15)),
                ('status', models.CharField(choices=[('success', 'Success'), ('fail', 'Fail'), ('in_progress', 'In Progress')], default='in_progress', max_length=30)),
                ('comment', models.TextField(blank=True, null=True)),
                ('date_paid', models.DateField(help_text='date of when amount is paid')),
                ('is_successful', models.BooleanField(db_index=True, default=False, help_text='after the payment gateway  successful payment make it True')),
                ('transaction_id', models.CharField(blank=True, help_text='Transaction id from the pyment gateway', max_length=100, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=50, null=True)),
                ('fpx_seller_id', models.CharField(blank=True, max_length=150, null=True)),
                ('fpx_transaction_msg', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='event/qr-code')),
                ('scan_count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventSpecialGift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
                ('collection', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
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
            name='EventVoucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentBreakUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
                ('service_tax', models.FloatField(default=event.models.get_current_service_tax, help_text='current percentage of the service tax')),
                ('service_charge', models.FloatField(default=event.models.get_current_service_charge, help_text='current percentage of the service charge')),
                ('excluded_tax_amount', models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
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
            name='SoloChargeAndTax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_tax', models.FloatField(default=1.3, help_text='percentage of the service tax')),
                ('service_charge', models.FloatField(default=1.3, help_text='percentage of the service charge')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SubEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='title or name')),
                ('event_date', models.DateField(help_text='date of when the sub event going to happen')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('end_date', models.DateField(null=True)),
                ('venue', models.CharField(help_text='venue for the event', max_length=150)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postal_code', models.IntegerField(null=True)),
                ('is_common', models.BooleanField(default=False, help_text='decide that is a common to linked event.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('veg_count', models.IntegerField(default=0)),
                ('non_veg_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_notify', models.BooleanField(default=True)),
                ('attendance', models.CharField(choices=[('attending', 'Attending'), ('kiv', 'KIV'), ('not_attending', 'Not attending')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='UserScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_scans', to='event.event')),
            ],
        ),
    ]
