from django.db import models

# Create your models here.
class Quote (models.Model):
    quote = models.TextField()
    author = models.CharField(max_length = 50)
    date_added = models.DateTimeField(auto_now_add = True)

    

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.quote

    
