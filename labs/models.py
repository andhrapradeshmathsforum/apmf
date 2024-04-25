from django.db import models
from dashboard.models import Item
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Lab(Item):
    title = models.CharField(max_length = 100)  
    
    class Meta:
        verbose_name = "Lab Manual"
        verbose_name_plural = "Lab Manuals"
        ordering = [
            'standard', 
            'date_added'
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("otherbook_detail", kwargs={"pk": self.pk})
