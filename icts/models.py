from django.db import models
from dashboard.models import Item
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Ict(models.Model):
    title = models.CharField(max_length = 100)  
    link = models.URLField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')


    class Meta:
        verbose_name = 'ICT and Simulation Site'
        verbose_name_plural = 'ICT and Simulation Sites'
        ordering = [
            '-date_added'
        ]

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("ict_detail", kwargs={"pk": self.pk})
