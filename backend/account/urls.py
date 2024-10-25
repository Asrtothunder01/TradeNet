rom django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
  
  path('v1/',views.AccountListView.as_view(), name = 'Account_list'),
  path('v2/',views.AccountCreateView.as_view(), name = 'Account_create'),
  
]