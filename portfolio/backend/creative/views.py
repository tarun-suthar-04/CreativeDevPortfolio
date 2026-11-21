from django.shortcuts import render
from core.models import SiteSettings
from .models import Work


def creative(request):
    return render(request, "creative.html", {
        "site": SiteSettings.objects.first(),
        "works": Work.objects.all(),
    })