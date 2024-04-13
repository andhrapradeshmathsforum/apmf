from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# Create your models here.
class News(models.Model):
    heading = models.CharField(max_length=200)
    body = RichTextField()
    image = models.ImageField('photo', upload_to='images', blank= True)
    attachment = models.FileField(upload_to='files', blank=True)
    date_added = models.DateTimeField(auto_now_add = True)
    date_updated = models.DateTimeField(auto_now = True) 
    uploaded_by = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)   

    class Meta:
       ordering = ['-date_added']

    def __str__(self):
        return self.heading

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"pk": self.pk})

