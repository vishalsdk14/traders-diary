from django.shortcuts import redirect, render
from trades.forms import AccountForm
from trades.models import AccountData
import logging

logger = logging.getLogger("trades")

def get_or_set_settings(request):
    try:
        entry = AccountData.objects.all()[0]
    except Exception as e:
        entry = AccountData()

    acc_data = AccountForm(request.POST, request.FILES, instance=entry)
    if request.POST and acc_data.is_valid():
        acc_data.save()
        return redirect('dashboard')

    acc_data = AccountForm(instance=entry)
    ctx = {
            'form': acc_data,
    }

    return render(request, "pages/settings.html", ctx)


