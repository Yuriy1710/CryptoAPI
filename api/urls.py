from django.urls import path
from . import views

urlpatterns = [
    path('api/customer/<id>/', views.get_customer_invoices_paid),
    path('api/customer-np/<id>/', views.get_customer_invoices_not_paid),
    path('api/users/', views.ListUsers.as_view()),
    path('api/token/auth/', views.CustomAuthToken.as_view()),
]
