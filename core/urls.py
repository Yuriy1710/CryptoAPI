from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *


router = DefaultRouter()
router.register(r'customer', CustomerViewset, basename="customer")
router.register(r'invoice', InvoiceViewset, basename="invoice")
router.register(r'invoice-paid', InvoiceViewsetPaid, basename="invoice_paid")
router.register(r'invoice-not-paid', InvoiceViewsetNotPaid, basename="invoice_not_paid")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('', include('api.urls')),
]
