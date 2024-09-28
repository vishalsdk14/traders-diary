from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from trades.utils import get_or_create_trade_entry
from django.shortcuts import render, get_object_or_404, redirect
from trades.models import Tradedata
from trades.forms import TradeForm
import pandas as pd

view="grid"

def get_all_trades(request):
    global view

    query = request.GET.get("query", None)
    objects = Tradedata.get_objects(query)
    default_page = 1

    if request.GET.get("view_type") == "list_view":
        view="list"
    elif request.GET.get("view_type") == "grid_view":
        view="grid"

    page = request.GET.get('page', default_page)
    if view == "grid":
        items_per_page = 8
    elif view=="list":
        items_per_page = 10

    paginator = Paginator(objects, items_per_page)
    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    ctx = {
            'objects' : items_page,
            'view_type': view,
    }

    return render(request, "pages/all_trades.html", ctx)

def import_trades(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        data = pd.read_csv(request.FILES['tradebook'])
        #TODO: Need to check whether correct file is uploaded or not

        for row in data.itertuples():
            get_or_create_trade_entry(row)

    return render(request, "pages/import_trades.html", {})

def edit_trade(request, pk):
    entry = get_object_or_404(Tradedata, pk=pk)
    form = TradeForm(request.POST, request.FILES, instance=entry)

    if request.POST and form.is_valid():
        entry.Update_PnL()
        entry.Update_MaxLoss()
        form.save()
        return redirect('all_trades') 
    else :
        form=TradeForm(instance=entry)

    ctx = {
            'form': form,
            'entry' : entry,
    }

    return render(request, "pages/edit_trade.html", ctx)

def delete_trade(request, pk):
    entry = get_object_or_404(Tradedata, pk=pk)
    entry.delete()
    return redirect('all_trades') 
