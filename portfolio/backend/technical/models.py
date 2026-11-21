from django.db import models


class SkillGroup(models.Model):
    KINDS = [
        ("used", "Used in my projects"),
        ("foundation", "Foundational knowledge"),
        ("learning", "Currently learning"),
    ]
    kind = models.CharField(max_length=12, choices=KINDS)
    items = models.TextField(help_text="One skill per line")

    def skill_list(self):
        return [s for s in self.items.splitlines() if s.strip()]

    def __str__(self):
        return self.get_kind_display()


class Project(models.Model):
    name = models.CharField(max_length=100)
    meta = models.CharField(max_length=120, blank=True)
    summary = models.TextField()
    bullets = models.TextField(blank=True, help_text="One bullet per line")
    tech = models.CharField(max_length=200, help_text="Comma separated")
    note = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def bullet_list(self):
        return [b for b in self.bullets.splitlines() if b.strip()]

    def tech_list(self):
        return [t.strip() for t in self.tech.split(",") if t.strip()]

    def __str__(self):
        return self.name


class Education(models.Model):
    qualification = models.CharField(max_length=120)
    institution = models.CharField(max_length=160)
    year = models.CharField(max_length=20)
    result = models.CharField(max_length=40, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Education"

    def __str__(self):
        return self.qualification


class Credential(models.Model):
    KINDS = [("cert", "Certification"), ("ach", "Achievement")]
    kind = models.CharField(max_length=5, choices=KINDS)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text