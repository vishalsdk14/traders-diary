from django.db import models

# Create your models here.


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
