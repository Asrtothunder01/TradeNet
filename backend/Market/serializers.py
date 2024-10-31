from rest_framework import serializers

from .models import Currency

class MarketSerializer (serializers.ModelSerializer):
    
    currency = CurrencySerializer (read_only = True)
    
    class Meta:
        model = Currency
        
        fields = ['id','currency','bid_price','ask_price','timestamp','created_at','updated_at']
        
        read_only_fields = ['id','user','created_at','updated_at']
        
        