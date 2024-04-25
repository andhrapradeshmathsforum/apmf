from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class Rp(models.Model):
    GENDER_CHOICES = [
        ('male','MALE'),
        ('female','FEMALE')
    ]
    FIELD_CHOICES = [
        ('ICT IN EDUCATION','ICT IN EDUCATION'),
        ('IF PANELS','IF PANELS'),
        ('BYJUS TABS','BYJUS TABS'),
        ('MODULE WRITING','MODULE WRITING'),
        ('ACADEMIC CALENDAR','ACADEMIC CALENDAR'),
        ('QUESTION PAPER PREPARATION','QUESTION PAPER PREPARATION'),
        ('SIMULATIONS','SIMULATIONS'),
        ('VIDEO PREPARATION','VIDEO PREPARATION'),
        ('OTHERS','OTHERS'),

    ]
    name = models.CharField('your name', max_length=100 )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    email = models.EmailField('email address',blank=True)
    school = models.CharField(max_length=100, blank=True)
    village = models.CharField('Village/town', max_length=100, blank=True)
    mandal = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    field = models.CharField(max_length=100, choices=FIELD_CHOICES)
    others = models.CharField('If others, specify area', max_length=200, blank=True)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name = 'Resource person'
        verbose_name_plural = 'Resource persons'
        ordering = ['district','mandal','field']
    
    def __str__(self) -> str:
        return self.name

