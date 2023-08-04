import uuid
from django.db import models


STATUS = [
  (1, 'created, not paid'),
  (2, 'created, paid'),
  (3,'created, timeouted'),
]

CURRENCY = [
  ('TON','toncoin'),
  ('BTN', 'bitcoin'),
  ('ETH', 'ethereum'),
]


class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    balance = models.DecimalField(max_digits=12, decimal_places=6)
    
    def __str__(self):
        return self.name
    
    
    
class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(Customer, related_name="sender", on_delete=models.CASCADE, blank=False, null=False)
    receiver = models.ForeignKey(Customer, related_name="receiver", on_delete=models.CASCADE, blank=False, null=False)
    date = models.DateTimeField(auto_now_add=True)
    network = models.CharField(max_length=250)
    currency = models.CharField(max_length=50, choices=CURRENCY, default='TON')
    status = models.CharField(max_length=50, choices=STATUS, default=1)
    currency_amount = models.DecimalField(max_digits=12, decimal_places=6)
    cryptocurrency_amount = models.DecimalField(max_digits=12, decimal_places=6)
    transaction_id = models.CharField(max_length=250)
    
    def __str__(self):
        return self.transaction_id, self.name
    
