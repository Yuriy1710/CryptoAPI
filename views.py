from rest_framework import viewsets, status
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import *
from .models import *


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
    
    

def get_customer_invoices_not_paid(request, id):
    customer = Customer.objects.get(id=id)
    customer_invoices_np = customer.sender.filter(status="CNP")
    data = list(customer_invoices_np.values())
    return JsonResponse (data, safe=False, status=status.HTTP_200_OK)       
    
     
def get_customer_invoices_paid(request, id):
    customer = Customer.objects.get(id=id)
    customer_invoices = customer.sender.filter(status="CP")
    data = list(customer_invoices.values())
    return JsonResponse (data, safe=False, status=status.HTTP_200_OK)    
    
   
    
class ListUsers(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        emails = [user.email for user in User.objects.all()]
        return Response(emails)   



class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })