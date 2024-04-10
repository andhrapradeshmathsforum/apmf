from django.db import models
from dashboard.models import Item
from django.urls import reverse

# Create your models here.


class Handbook(Item):
    title = models.CharField(max_length = 100)  

    class Meta:
        ordering = [
            "-standard"
        ]

    def __str__(self):
        return str(self.standard)+' ' +'Class '+self.title

    def get_absolute_url(self):
        return reverse("handbook_detail", kwargs={"pk": self.pk})
