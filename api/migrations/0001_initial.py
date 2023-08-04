# Generated by Django 4.2.4 on 2023-08-04 08:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('balance', models.DecimalField(decimal_places=6, max_digits=12)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('network', models.CharField(max_length=250)),
                ('currency', models.CharField(choices=[('TON', 'toncoin'), ('BTN', 'bitcoin'), ('ETH', 'ethereum')], default='TON', max_length=50)),
                ('status', models.CharField(choices=[(1, 'created, not paid'), (2, 'created, paid'), (3, 'created, timeouted')], default=1, max_length=50)),
                ('currency_amount', models.DecimalField(decimal_places=6, max_digits=12)),
                ('cryptocurrency_amount', models.DecimalField(decimal_places=6, max_digits=12)),
                ('transaction_id', models.CharField(max_length=250)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='api.customer')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='api.customer')),
            ],
        ),
    ]
