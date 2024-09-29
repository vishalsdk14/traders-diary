from django.db import models
from django.db.models import Q
import logging
logger = logging.getLogger("trades")

# Create your models here.

BUY_REASON_CHOICES = (
                ('1', 'LongBase_BO'),
                ('2', 'CnH_BO'),
                ('3', 'IHnS_BO'),
                ('4', 'Bottoms_BO'),
                ('5', 'Pennants_BO'),
                ('6', 'Gapfillings_BO'),
                ('7', 'SAUCER_BO'),
                ('8', 'VCP_BO'),
                ('9', 'POCKET_PICOT_BO'),
            )

SELL_REASON_CHOICES = (
                ('1', 'SL_Hit'),
                ('2', 'TSL_Hit'),
                ('3', 'ManualExit'),
                ('4', '315TP'),
                ('5', 'Event'),
                ('6', 'TimeStop'),
            )


"""
    Model to store account details

    Capital                 : Initial account capital
    MaxPosSizePerTrade      : Maximum position size percentrade per Trade
    MaxRiskPerTrade         : Maximum risk/Stop loss percentage per trade 
"""
class AccountData(models.Model):
    Capital             = models.IntegerField(default=1000000)      # Capital
    MaxPosSizePerTrade  = models.FloatField(default=20)  # Max Position size per trade
    MaxRiskPerTrade     = models.FloatField(default=5)    # Max Risk Per trade.

    def get_capital():
        try:
            acc_data = AccountData.objects.all()[0]
            return acc_data.Capital
        except Exception as e:
            logger.debug("Account details not set. Returning 0")
            return 0

    def get_max_pos_size():
        try:
            acc_data = AccountData.objects.all()[0]
            return acc_data.MaxPosSizePerTrade
        except Exception as e:
            logger.debug("Account details not set. Returning 0")
            return 0

    def get_max_risk_per_trade():
        try:
            acc_data = AccountData.objects.all()[0]
            return acc_data.MaxPosSizePerTrade
        except Exception as e:
            logger.debug("Account details not set. Returning 0")
            return 0

"""
    Tradedata : This models stores the information of the trade.
"""

class Tradedata(models.Model):
    Ltp             = models.FloatField(default=0)                  # Last Trading Price of the SYMBOL
    BuyDate         = models.DateField(blank=True, null=True)       # Buy Date
    SellDate        = models.DateField(blank=True, null=True)       # Sell Date
    Symbol          = models.CharField(max_length=25)               # Stock Symbol
    OpenPos         = models.IntegerField(default=0)                # Open position
    AvgPrice        = models.FloatField(default=0)                  # Average buy price
    SoldPos         = models.IntegerField(default=0)                # How many positions sold
    PerPosSize      = models.FloatField(default=0)                  # Percentage position size w.r.t capital
    AvgSellPrice    = models.FloatField(default=0)                  # Average sell price
    TradeDuration   = models.IntegerField(default=0)                # Total trade duration in days
    Pnl             = models.FloatField(default=0)                  # Realised Profir/loss
    PerPnL          = models.FloatField(default=0)                  # Profit/Loss in percentage
    PerPnLwrtCap    = models.FloatField(default=0)                  # Profit/Loss in percentage w.r.t capital
    UnrealisedPnl   = models.FloatField(default=0)                  # Unrealised profit/loss.
    BuyReason       = models.CharField(                             # What is the reason to enter this trade?
                        choices=BUY_REASON_CHOICES,
                        max_length=50,
                        blank=True
                        )
    BaseDays        = models.IntegerField(default=0)                # What is the base width(in days) of the chart pattern
    SellReason      = models.CharField(                             # What is the reason to exit this trade
                        choices=SELL_REASON_CHOICES,
                        max_length=50,
                        blank=True
                        )
    StopLoss        = models.FloatField(default=0)                  # What is the Stoploss of this trade
    PerStopLoss     = models.FloatField(default=0)                  # Percentage Stoptloss 
    MaxLoss         = models.FloatField(default=0)                  # What is the MaxLoss if StopLoss is hit

    def get_objects(query):
        if query == None:
            return Tradedata.objects.all()

        objects = Tradedata.objects.filter(
                    Q(Symbol__icontains=query)
                    #| Q(Notes__icontains=query) 
        )
        return objects

    def Update_PnL(self):
        Capital = AccountData.get_capital()
        if Capital == 0:
            return

        self.Pnl = (self.AvgSellPrice - self.AvgPrice) * self.SoldPos
        self.PerPnL = ((self.AvgSellPrice - self.AvgPrice) / self.AvgPrice) * 100
        self.PerPosSize = ((self.AvgPrice * self.SoldPos) / Capital) * 100
        self.PerPnLwrtCap = (self.Pnl / Capital) * 100
        if self.OpenPos == 0:
            self.TradeDuration = (self.SellDate - self.BuyDate).days
        self.save()

    def Update_MaxLoss(self):
        self.MaxLoss = (self.StopLoss - self.AvgPrice) * self.OpenPos
        self.PerStopLoss = ((self.AvgPrice - self.StopLoss)/self.AvgPrice) * 100

    def __str__(self):
        return self

class TradeStats(models.Model):
    TotalProfit         = models.IntegerField(default=0)
    NoOfWins            = models.IntegerField(default=0)
    NoOfLoss            = models.IntegerField(default=0)
    AvgProfit           = models.FloatField(default=0)
    AvgLoss             = models.FloatField(default=0)
    TotalTrades         = models.IntegerField(default=0)
    BatAvg              = models.FloatField(default=0)
    TotalPosPer         = models.FloatField(default=0)
    TotalNegPer         = models.FloatField(default=0)
    Avgholdtime         = models.IntegerField(default=0)
    WintoLossRatio      = models.FloatField(default=0)
    Avgprofitwrtcap     = models.IntegerField(default=0)
    Avglosswrtcap       = models.IntegerField(default=0)

    def __str__(self):
        return self
