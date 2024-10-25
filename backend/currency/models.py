import uuid

from django.db import models

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Currency(BaseModel):
    
    base_currency = models.CharField(max_length = 3)
    
    quote_currency = models.CharField(max_length = 3)
    
    symbol = models.CharField(max_length = 7, unique = True)
    
    def __str__(self):
        return f"{self.base_currency}/{self.quote_currency}"
        
