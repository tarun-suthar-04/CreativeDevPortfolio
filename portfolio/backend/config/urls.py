from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import landing
from creative.views import creative
from technical.views import technical

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", landing, name="landing"),
    path("creative/", creative, name="creative"),
    path("technical/", technical, name="technical"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)