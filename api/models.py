import uuid
from django.db import models


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    balance = models.DecimalField(max_digits=12, decimal_places=6)
    
    def __str__(self):
        return self.name + " " + str(self.id) 
    
    
    
class Invoice(models.Model):
    class StatusChoices(models.TextChoices):
        CREATED_PAID = 'CP', 'Created, paid'
        CREATED_NOT_PAID = 'CNP', 'Created, not paid'
        CREATED_TIMEOUTED = 'CT', 'Created, timeouted'
        
    class CurrencyChoices(models.TextChoices):
        TONCOIN = 'TON', 'Toncoin'
        BITCOIN = 'BTN', 'Bitcoin'
        ETHEREUM = 'ETN', 'Ethereum'
 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Customer, related_name="sender", on_delete=models.CASCADE, blank=False, null=False)
    receiver = models.ForeignKey(Customer, related_name="customer", on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    network = models.CharField(max_length=250)
    currency = models.CharField(max_length=50, choices=CurrencyChoices.choices, default=CurrencyChoices.TONCOIN)
    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.CREATED_PAID)
    currency_amount = models.DecimalField(max_digits=12, decimal_places=6)
    cryptocurrency_amount = models.DecimalField(max_digits=12, decimal_places=6)
    transaction_id = models.CharField(max_length=250)
    
    def __str__(self):
        return self.transaction_id
    
    