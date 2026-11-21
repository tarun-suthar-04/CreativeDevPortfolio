from django.shortcuts import render
from .models import SiteSettings


def landing(request):
    return render(request, "landing.html", {"site": SiteSettings.objects.first()})