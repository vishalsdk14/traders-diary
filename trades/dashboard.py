from trades.models import Tradedata, TradeStats, AccountData
from django.shortcuts import render
from django.db.models import Sum

def get_stats():
    stats = TradeStats()

    stats.TotalTrades = Tradedata.objects.count()
    if stats.TotalTrades == 0:
        return

    stats.TotalProfit = Tradedata.objects.aggregate(Sum('Pnl'))['Pnl__sum']
    stats.NoOfWins = Tradedata.objects.filter(Pnl__gt=0).count()

    query = (Tradedata.objects.filter(PerPnL__gt=0).aggregate(Sum('PerPnL')))['PerPnL__sum']
    stats.TotalPosPer = query if query != None else 0

    stats.AvgProfit = stats.TotalPosPer/stats.NoOfWins if stats.NoOfWins != 0 else 0

    query = (Tradedata.objects.filter(PerPnL__lt=0).aggregate(Sum('PerPnL')))['PerPnL__sum']
    stats.TotalNegPer = query if query != None else 0

    stats.NoOfLoss = Tradedata.objects.filter(Pnl__lt=0).count()
    stats.AvgLoss = stats.TotalNegPer/stats.NoOfLoss if stats.NoOfLoss !=0 else 0
    stats.BatAvg = (stats.NoOfWins/stats.TotalTrades) * 100 if stats.TotalTrades > 0 else 0


    if stats.NoOfWins > 0:
        stats.Avgprofitwrtcap = (Tradedata.objects.filter(Pnl__gt=0).aggregate(Sum('Pnl')))['Pnl__sum'] / Tradedata.objects.filter(Pnl__gt=0).count()
    if stats.NoOfLoss > 0:
        stats.Avglosswrtcap = (Tradedata.objects.filter(Pnl__lt=0).aggregate(Sum('Pnl')))['Pnl__sum'] / Tradedata.objects.filter(Pnl__lt=0).count()

    stats.Avgholdtime = Tradedata.objects.filter(TradeDuration__gt=0).aggregate(Sum('TradeDuration'))['TradeDuration__sum']/Tradedata.objects.exclude(TradeDuration=0).count()
    stats.WintoLossRatio = (stats.NoOfLoss * stats.Avgprofitwrtcap) / abs((stats.NoOfLoss * stats.Avglosswrtcap))

    stats.Avgprofitwrtcap = (stats.Avgprofitwrtcap / AccountData.get_capital()) * 100
    stats.Avglosswrtcap = (stats.Avglosswrtcap / AccountData.get_capital()) * 100

    return stats

def get_dashboard(request):
    if  Tradedata.objects.count() == 0:
        return render(request, "pages/dashboard.html", {})

    stats = get_stats()

    ctx = {
            'stats': stats,
    }

    return render(request, "pages/dashboard.html", ctx)
