# Generated by Django 4.2.4 on 2023-08-07 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_customer_invoices_alter_invoice_sender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='currency',
            field=models.CharField(choices=[('CP', 'Created, paid'), ('CNP', 'Created, not paid'), ('CT', 'Created, timeouted')], default='TON', max_length=50),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='api.customer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='api.customer'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('CP', 'Created, paid'), ('CNP', 'Created, not paid'), ('CT', 'Created, timeouted')], default='CP', max_length=50),
        ),
    ]