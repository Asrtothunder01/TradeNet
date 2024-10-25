from rest_framework import serializers

from .models import Currency

class CurrencySerializer (serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        
        fields = ['id','base_currency','quote_currency','symbol','created_at','updated_at']
        
        read_only_fields = ['id','created_at','updated_at']
        
        