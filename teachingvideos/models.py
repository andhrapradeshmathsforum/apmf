from django.db import models
from embed_video.fields import EmbedVideoField
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.


class Teachingvideo(models.Model):
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
    title = models.CharField(max_length=100)
    description = models.CharField(max_length = 100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    video = EmbedVideoField()  # same like models.URLField()
    class Meta:
        verbose_name = "Teaching Video"
        verbose_name_plural = "Teaching Videos"
        
        ordering = [
            'standard',
            'date_added'
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("video_detail", kwargs={"pk": self.pk})
