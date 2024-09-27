from django.db import models

# Create your models here.
class AccountData(models.Model):
    Capital             = models.IntegerField(default=1000000)      # Capital
    MaxPosSizePerTrade  = models.FloatField(default=20)  # Max Position size per trade
    MaxRiskPerTrade     = models.FloatField(default=0.5)    # Max Risk Per trade.
