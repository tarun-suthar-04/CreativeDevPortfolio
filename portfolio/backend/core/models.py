from django.db import models

class SiteSettings(models.Model):
    name = models.CharField(max_length=80, default="Tarun Suthar")
    location = models.CharField(max_length=80, default="Indore, IN")
    creative_bio = models.TextField(blank=True)
    technical_bio = models.TextField(blank=True)
    creative_email = models.EmailField(blank=True)
    technical_email = models.EmailField(blank=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    fiverr = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "Site settings"

    def __str__(self):
        return self.name

