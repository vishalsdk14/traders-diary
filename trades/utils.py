from django.shortcuts import redirect, render
from trades.forms import AccountForm
from trades.models import AccountData, Tradedata
from datetime import datetime
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

def update_buy_avg(entry, tupple):
    value = (entry.OpenPos * entry.AvgPrice) + (tupple[9] * tupple[10])
    entry.AvgPrice = value / (entry.OpenPos + tupple[9])

def update_sell_avg(entry, tupple):
    if entry.SoldPos == 0:
        entry.SoldPos += tupple[9]
        entry.AvgSellPrice = tupple[10]
        return

    entry.SoldPos += tupple[9]
    value = (entry.SoldPos * entry.AvgSellPrice) + (tupple[9] * tupple[10])
    entry.AvgSellPrice = value / (entry.SoldPos + tupple[9])


def create_new_trade_entry(tupple):
    TradeEntry = Tradedata(
                    BuyDate = datetime.strptime(tupple[3], '%Y-%m-%d').date(),
                    Symbol = tupple[1],
                    OpenPos = tupple[9],
                    )  
    TradeEntry.AvgPrice = tupple[10]
    TradeEntry.save()

def update_trade_entry(entry, tupple):
    if tupple[7] == 'buy':
        update_buy_avg(entry, tupple)
        entry.OpenPos += tupple[9]
    else:
        entry.OpenPos -= tupple[9]
        update_sell_avg(entry, tupple)

    if entry.OpenPos == 0:
        entry.SellDate = datetime.strptime(tupple[3], '%Y-%m-%d').date()
        entry.Update_PnL()
        entry.UnrealisedPnl = 0
        entry.MaxLoss = 0

    entry.save()

def get_or_create_trade_entry(tupple):
    try:
        entry = Tradedata.objects.filter(Symbol=tupple[1]).exclude(OpenPos=0).order_by('-id')[0]
        update_trade_entry(entry, tupple)
    except Exception as e:
        create_new_trade_entry(tupple)
