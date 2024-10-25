import uuid

from django.db import models

from django.contrib.auth.models import User

class BaseModel (models.Model):
    id = models.UUIDField(unique = True, editable = True, primary_key = True, default = uuid.uuid4)
    
    created_at = models.DateTimeField(auto_now_add = True)
    
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        abstract = True
        

class Account(BaseModel):
    
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    
    balance = models.DecimalField(max_length = 15, decimal_places = 2, default = 0.00)
    
    currency = models.CharField(max_length = 3, default = 'USD')
    
    def __str__(self):
        return f"Account of {self.user.username}|Balance:{self.balance}{self.currency}"