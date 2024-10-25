from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from .models import Account

from .serializer import AccountSerializer


@extend_schema(
  tags = ['Account'],
  
  responses = {200: AccountSerializer (many = True)},
)

class AccountListView(ListAPIView):
    
    queryset = Account.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
@extend_schema(
  tags = ['Account'],
  
  request = AccountSerializer(),
  
  responses = {201: AccountSerializer (many = True)},
)

class AccountCreateView(ListAPIView):
    
    queryset = Account.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None