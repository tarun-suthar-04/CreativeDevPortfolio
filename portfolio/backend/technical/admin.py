from django.contrib import admin
from .models import SkillGroup, Project, Education, Credential

admin.site.register(SkillGroup)
admin.site.register(Project)
admin.site.register(Education)
admin.site.register(Credential)