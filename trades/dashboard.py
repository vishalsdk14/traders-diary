from django.shortcuts import render

def get_dashboard(request):
    return render(request, "pages/dashboard.html", {})
