from django.db import models
from dashboard.models import Item
from django.urls import reverse

# Create your models here.


class Solution(Item):
    chapter = models.CharField(max_length = 50)  

    class Meta:
        ordering = [
            '-standard',
            'chapter'
        ]

    def __str__(self):
        return str(self.standard)+' ' +'Class '+self.chapter+' ' +'solutions'

    def get_absolute_url(self):
        return reverse("solution_detail", kwargs={"pk": self.pk})
