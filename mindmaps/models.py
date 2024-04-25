from django.db import models
from dashboard.models import Item

# Create your models here.

class Mindmap(Item):
    chapter = models.CharField(max_length=50, blank=True)
    title = models.CharField(max_length=50)

    class Meta:        
        verbose_name = 'Mindmap'
        verbose_name_plural = 'Mindmaps'
        ordering = ['-standard']

    

    def __str__(self) -> str:
        return self.title
