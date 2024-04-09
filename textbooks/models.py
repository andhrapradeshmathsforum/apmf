from django.db import models
from dashboard.models import Item
from django.urls import reverse

# Create your models here.


class Textbook(Item):
    SEMESTER_CHOICES = (
        ('semester 1','Semester 1'),
        ('semester 2', 'Semester 2'),
        ('complete', 'Complete'),
    )
    semester = models.CharField(max_length = 20, choices = SEMESTER_CHOICES)
    title = models.CharField(max_length = 50)  

    class Meta:
        ordering = [
            ("-standard"),
        ]

    def __str__(self):
        return str(self.standard)+' ' +'Class '+self.semester+' ' +self.title

    def get_absolute_url(self):
        return reverse("Textbook_detail", kwargs={"pk": self.pk})
