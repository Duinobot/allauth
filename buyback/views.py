from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Buyback
# Create your views here.


class BuybackListView(ListView):

    model = Buyback

    template_name = 'buyback/buyback_listview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
