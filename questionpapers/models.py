from django.db import models
from dashboard.models import Item
from django.urls import reverse

# Create your models here.


class Questionpaper(Item):
    EXAM_CHOICES = (
        ('FA1', 'FA1'),
        ('FA2', 'FA2'),
        ('FA3', 'FA3'),
        ('FA4', 'FA4'),
        ('SA1', 'SA1'),
        ('SA2', 'SA2'),
        ('PREFINAL', 'PREFINAL'),
        ('PUBLIC', 'PUBLIC'),
        ('REVISION','REVISION'),
        ('OTHERS', 'OTHERS')
    )
    exam = models.CharField(max_length=20, choices = EXAM_CHOICES)  
    class Meta:
        ordering = [
            "-standard",
            "exam",
        ]

    def __str__(self):
        return str(self.standard)+' ' +'Class '+self.exam+' ' +"question paper"

    def get_absolute_url(self):
        return reverse("questionpaper_detail", kwargs={"pk": self.pk})
