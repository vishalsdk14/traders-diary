# trades/urls.py

from django.urls import path
from trades import trades, dashboard, utils

urlpatterns = [
        path("", dashboard.get_dashboard, name='dashboard'),
        path("all_trades/", trades.get_all_trades, name='all_trades'),
        path("import_trades/", trades.import_trades, name='import_trades'),
        path("edit_trade/<pk>/", trades.edit_trade, name='edit_trade'),

        path("settings/", utils.get_or_set_settings, name='settings'),
]
