from django.db import models
from dashboard.models import Item
from django.urls import reverse
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Tlm(models.Model):
    title = models.CharField(max_length = 100)  
    description = models.CharField(max_length = 100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField('TLM Photo', upload_to='images')
    image_thumbnail = ImageSpecField(source='image',
                                      processors=[ResizeToFill(100, 50)],
                                      format='JPEG',
                                      options={'quality': 60})

    

    class Meta:
        verbose_name = ("TLM Photo")
        verbose_name_plural = ("TLM Photos")

    def __str__(self):
        return self.title

    

    