from django.shortcuts import render
import pandas as pd

def get_all_trades(request):
    return render(request, "pages/all_trades.html", {})

def import_trades(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        data = pd.read_csv(request.FILES['tradebook'])
        #TODO: Need to check whether correct file is uploaded or not

    return render(request, "pages/import_trades.html", {})
