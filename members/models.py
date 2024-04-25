from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth import get_user_model

# Create your models here.


class Member(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField('Designation in APMF', max_length=100)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    school = models.CharField( max_length=100, blank=True)
    mandal = models.CharField( max_length=100, blank=True)
    district = models.CharField( max_length=100, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    uploaded_by =models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField('Photo', upload_to='images')

    class Meta:
        verbose_name = 'APMF Member'
        verbose_name_plural = 'APMF Members'
        ordering = [
            '-date_added'
        ]

    def __str__(self) -> str:
        return self.name
    


    