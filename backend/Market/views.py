from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from drf_spectacular.utils import extend_schema

from .models import Market

from .serializer import MarketSerializer


@extend_schema(
  tags = ['market'],
  
  responses = {200: MarketSerializer (many = True)},
)

class MarketListView(ListAPIView):
    
    queryset = Market.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None
    
    
@extend_schema(
  tags = ['market'],
  
  request = MarketSerializer(),
  
  responses = {201: MarketSerializer (many = True)},
)

class MarketCreateView(ListAPIView):
    
    queryset = Market.objects.all()
    
    permission_classes = [IsAuthenticated]
    
    pagination_class = None