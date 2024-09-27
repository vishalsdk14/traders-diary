# trades/urls.py

from django.urls import path
from trades import trades, dashboard

urlpatterns = [
        path("", dashboard.get_dashboard, name='dashboard'),
        path("all_trades/", trades.get_all_trades, name='all_trades'),
]
