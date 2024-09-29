# trades/urls.py

from trades import trades, dashboard, utils, charts
from django.urls import path

urlpatterns = [
        path("", dashboard.get_dashboard, name='dashboard'),
        path("all_trades/", trades.get_all_trades, name='all_trades'),
        path("import_trades/", trades.import_trades, name='import_trades'),
        path("edit_trade/<pk>/", trades.edit_trade, name='edit_trade'),
        path("delete_trade/<pk>/", trades.delete_trade, name='delete_trade'),
        
        path('charts/eqcurve', charts.equity_curve.as_view()),

        path("settings/", utils.get_or_set_settings, name='settings'),
]
