from django.shortcuts import render

def get_all_trades(request):
    return render(request, "pages/all_trades.html", {})
