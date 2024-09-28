from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from trades.utils import get_or_create_trade_entry
from django.shortcuts import render
from trades.models import Tradedata
import pandas as pd


def get_all_trades(request):
    query = request.GET.get("query", None)
    objects = Tradedata.get_objects(query)

    default_page = 1

    page = request.GET.get('page', default_page)
    items_per_page = 8
    paginator = Paginator(objects, items_per_page)

    try:
        items_page = paginator.page(page)
    except PageNotAnInteger:
        items_page = paginator.page(default_page)
    except EmptyPage:
        items_page = paginator.page(paginator.num_pages)

    ctx = {
            'objects' : items_page,
    }

    return render(request, "pages/all_trades.html", ctx)

def import_trades(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        data = pd.read_csv(request.FILES['tradebook'])
        #TODO: Need to check whether correct file is uploaded or not

        for row in data.itertuples():
            get_or_create_trade_entry(row)

    return render(request, "pages/import_trades.html", {})
