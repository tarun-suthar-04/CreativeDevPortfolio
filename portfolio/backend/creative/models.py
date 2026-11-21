from django.db import models


class Work(models.Model):
    CATEGORIES = [("Personal", "Personal"), ("Stories", "Stories")]
    COLORS = [
        ("blue", "Blue"), ("grad", "Gradient"), ("night", "Burgundy"),
        ("black", "Black"), ("white", "Cream"),
    ]
    ASPECTS = [("3/4", "3:4"), ("1/1", "1:1"), ("4/5", "4:5"), ("16/10", "16:10")]

    title = models.CharField(max_length=120)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    color = models.CharField(max_length=10, choices=COLORS, default="blue")
    aspect = models.CharField(max_length=6, choices=ASPECTS, default="1/1")
    image = models.ImageField(upload_to="works/", blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title