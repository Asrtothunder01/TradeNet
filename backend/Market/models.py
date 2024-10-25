import uuid

from django.db import models

from currency.models import Currency

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Market(BaseModel):
    
    currency = models.ForeignKey(Currency,on_delete = models.CASCADE)
    
    bid_price = models.CharField(max_digits = 7, decimal_places = 5)
    
    ask_price = models.CharField(max_digits = 7, decimal_places = 5)
    
    timestamp = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.currency.symbol}|Bid: {self.bid_price}, Ask: {self.ask_price} at {self.timestamp}"
        
