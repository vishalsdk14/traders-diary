from django.forms import ModelForm
from trades.models import AccountData, Tradedata
from django import forms

class AccountForm(ModelForm):
    class Meta:
        model = AccountData
        fields = '__all__'
        widgets = {
                'Capital' : forms.NumberInput(attrs={"class":"form-control"}),
                'MaxPosSizePerTrade': forms.NumberInput(attrs={"class":"form-control"}),
                'MaxRiskPerTrade' : forms.NumberInput(attrs={"class":"form-control"}),
        }
        labels = {
            "Capital": "Initial Capital",
            "MaxPosSizePerTrade": "Max Position Size %",
            "MaxRiskPerTrade": "Max Risk Per trade %"
        }

class TradeForm(ModelForm):
    class Meta:
        model = Tradedata
        fields = ['BuyReason', 'BaseDays', 'StopLoss', 'SellReason']
        widgets = {
                'BuyReason':forms.Select(attrs={"class":"form-control"}),
                'SellReason':forms.Select(attrs={"class":"form-control"}),
                'StopLoss':forms.NumberInput(attrs={"class":"form-control"}),
                'BaseDays':forms.NumberInput(attrs={"class":"form-control"}),
        }
