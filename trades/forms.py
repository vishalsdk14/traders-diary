from django.forms import ModelForm
from trades.models import AccountData
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
