from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import *


router = DefaultRouter()
router.register(r'customer', CustomerViewset, basename="customer")
router.register(r'invoice', InvoiceViewset, basename="invoice")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
