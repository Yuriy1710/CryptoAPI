# Generated by Django 4.1.3 on 2023-08-04 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_customer_invoices_customer_invoices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='invoices',
            field=models.ManyToManyField(to='api.invoice'),
        ),
    ]
