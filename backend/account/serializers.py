from rest_framework import serializers

from .models import Account

class AccountSerializer (serializers.ModelSerializer):
    
    user = UserSerializer (read_only = True)
    
    class Meta:
        model = Account
        
        fields = ['id','user','balance','currency','created_at','updated_at']
        
        read_only_fields = ['id','user','created_at','updated_at']
        
        