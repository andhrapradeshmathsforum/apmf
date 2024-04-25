from django.db import models
from dashboard.models import Item

# Create your models here.

class Hot(Item):
    chapter = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)

    class Meta:        
        verbose_name = 'Case study & hot question'
        verbose_name_plural = 'Case study & hot questions'
        ordering = ['-standard']

    

    def __str__(self) -> str:
        return self.title
