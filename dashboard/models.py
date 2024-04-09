from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Item(models.Model):
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
    description = models.CharField(max_length = 100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now = True)
    uploaded_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')

    class Meta:
        abstract = True