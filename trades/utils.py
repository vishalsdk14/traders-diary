from django.shortcuts import get_object_or_404, reverse, redirect, render
from django.shortcuts import render
from trades.forms import AccountForm
from trades.models import AccountData
import logging

logger = logging.getLogger("trades")

def get_or_set_settings(request):
    try:
        entry = AccountData.objects.all()[0]
    except Exception as e:
        entry = AccountData()

    acc_data = AccountForm(request.POST, request.FILES, instance=entry)
    if request.POST and acc_data.is_valid():
        acc_data.save()
        return redirect('dashboard')

    acc_data = AccountForm(instance=entry)
    ctx = {
            'form': acc_data,
    }

    return render(request, "pages/settings.html", ctx)

def get_capital(self):
    try:
        acc_data = AccountData.objects.all()[0]
        return acc_data.Capital
    except Exception as e:
        logger.debug("Account details not set. Returning 0")
        return 0

def get_max_pos_size(self):
    try:
        acc_data = AccountData.objects.all()[0]
        return acc_data.MaxPosSizePerTrade
    except Exception as e:
        logger.debug("Account details not set. Returning 0")
        return 0

def get_max_risk_per_trade(self):
    try:
        acc_data = AccountData.objects.all()[0]
        return acc_data.MaxPosSizePerTrade
    except Exception as e:
        logger.debug("Account details not set. Returning 0")
        return 0
