from django.contrib import admin
from django.urls import path, include
from .views import BuybackListView

urlpatterns = [
    path('', BuybackListView.as_view(), name='buyback'),
]
