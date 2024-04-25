from django.db import models
from dashboard.models import Item
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Quiz(Item):
    STANDARD_CHOICES = (
        (10,10),
        (9,9),
        (8,8),
        (7,7),
        (6,6),
        (5,5),
        (4,4),
        (3,3),
        (2,2),
        (1,1),
        (11,11),
        (12,12),
    )
    standard = models.IntegerField("class", choices= STANDARD_CHOICES)
    topic = models.CharField(verbose_name='chapter / topic',max_length=100)    
    sub_topic = models.CharField(max_length = 50,blank=True)  
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    link = models.URLField(max_length=200)
    topic = models.CharField(verbose_name='chapter / topic',max_length=100)    
    sub_topic = models.CharField(max_length = 50,blank=True)  

    class Meta:
        ordering = [
            "-standard",
            "topic"
        ]

    def __str__(self):
        return str(self.standard)+' ' +'Class '+self.topic+' ' +self.sub_topic

    def get_absolute_url(self):
        return reverse("quiz_detail", kwargs={"pk": self.pk})
