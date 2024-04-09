from django.db import models
from dashboard.models import Item
from django.urls import reverse

# Create your models here.


class Mcq(Item):
    chapter = models.CharField(max_length = 50)  

    class Meta:
        ordering = [
            '-standard',
            'chapter'
        ]

    def __str__(self):
        return str(self.standard)+' ' +'Class '+self.chapter

    def get_absolute_url(self):
        return reverse("mcq_detail", kwargs={"pk": self.pk})
