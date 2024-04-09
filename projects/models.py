from django.db import models
from dashboard.models import Item
from django.urls import reverse

# Create your models here.


class Project(Item): 
    EXAMCHOICES = (
        ('FA1','FA1'),
        ('FA2','FA2'),
        ('FA3','FA3'),
        ('FA4','FA4'),
    )   
    exam = models.CharField(max_length = 5, choices=EXAMCHOICES)
    chapter = models.CharField(max_length = 50)  

    class Meta:
        ordering = [
            ("-standard"),
        ]

    def __str__(self):
        return str(self.standard)+' ' +'Class '+self.exam+' ' +self.chapter

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
