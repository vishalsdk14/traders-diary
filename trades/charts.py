from rest_framework.response import Response 
from django.db.models.functions import Trunc
from rest_framework.views import APIView 
from django.db.models import Sum, Count
from trades.models import Tradedata 

class equity_curve(APIView): 
    def get(self, request, format = None):
        Entry = Tradedata.objects.all()[0]
        PnLPerMonth = Tradedata.objects.filter(BuyDate__gte=Entry.BuyDate)\
                    .annotate( monthly=Trunc('BuyDate', 'month')) \
                    .order_by('monthly')\
                    .values('monthly')\
                    .annotate(Profit=Sum('Pnl'))

        chartLabel = "Equity Curve"
        label = [sub["monthly"] for sub in PnLPerMonth]
        chartdata = [sub["Profit"] for sub in PnLPerMonth]

        value = 0
        for index,x in enumerate(chartdata):
            value += x
            chartdata[index] = value

        data ={
                     "labels":label,
                     "chartLabel":chartLabel,
                     "chartdata":chartdata,
                     "backgroundColor": 'lightgreen',
                     "linecolor": 'black',
             }
        return Response(data)

