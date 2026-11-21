from django.shortcuts import render
from core.models import SiteSettings
from .models import SkillGroup, Project, Education, Credential


def technical(request):
    return render(request, "technical.html", {
        "site": SiteSettings.objects.first(),
        "skills": SkillGroup.objects.all(),
        "projects": Project.objects.all(),
        "education": Education.objects.all(),
        "creds": Credential.objects.all(),
    })