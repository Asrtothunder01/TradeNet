rom django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
  
  path('v1/',views.MarketListView.as_view(), name = 'market_list'),
  path('v2/',views.MarketCreateView.as_view(), name = 'market_create'),
  
]