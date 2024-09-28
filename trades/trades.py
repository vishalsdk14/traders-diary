from django.shortcuts import render
import pandas as pd
from trades.utils import get_or_create_trade_entry

def get_all_trades(request):
    return render(request, "pages/all_trades.html", {})

def import_trades(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        data = pd.read_csv(request.FILES['tradebook'])
        #TODO: Need to check whether correct file is uploaded or not

        for row in data.itertuples():
            get_or_create_trade_entry(row)

    return render(request, "pages/import_trades.html", {})
