from django.db import models
from dashboard.models import Item
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.


class Otherbook(models.Model):
    title = models.CharField(max_length = 100)  
    description = models.CharField(max_length = 100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

    class Meta:
        ordering = [
            'dated_added'
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("otherbook_detail", kwargs={"pk": self.pk})
