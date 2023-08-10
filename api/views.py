from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

#Работает
class CustomerViewset(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
 
    
class InvoiceViewset(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all()
    
    
    
class InvoiceViewsetPaid(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    def get_queryset(self):
        return Invoice.objects.filter(status="CP")
        
        
    
class InvoiceViewsetNotPaid(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    def get_queryset(self):
        return Invoice.objects.filter(status="CNP")
    
  
#Работает, но только рендер   
def get_customer_invoices_paid(request, id):
    customer = Customer.objects.get(id=id)
    customer_invoices = customer.sender.filter(status="CP")
    return render(request, 'customers.html', {"customer_invoices": customer_invoices})


def get_customer_invoices_not_paid(request, id):
    customer = Customer.objects.get(id=id)
    customer_invoices_np = customer.sender.filter(status="CNP")
    return render(request, 'customers.html', {"customer_invoices_np": customer_invoices_np})        
    
    
    
#Не работает    
# def get_customer_invoices_paid(request, id):
#     customer = Customer.objects.get(id=id)
#     customer_invoices = customer.sender.filter(status="CP")
#     return Response (request, customer_invoices)    
    
    
    
    
    
