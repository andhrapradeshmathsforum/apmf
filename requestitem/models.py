from django.db import models
from django.core.validators import RegexValidator


# Create your models here.

class Message(models.Model):
    REQUEST_CHOICES = (
        ('text_book','TEXT BOOK'),
        ('other_book','OTHER BOOK'),
        ('lesson_plan','LESSON PLAN'),
        ('project','PROJECT WORK'),
        ('question_paper','QUESTION PAPER'),
        ('notes','TEACHING NOTES'),
        ('solutions', 'SOLUTIONS'),
        ('ppt','PPTs'),
        ('teaching_video','TEACHING VIDEOS'),
        ('other_video','OTHER VIDEOS'),
        ('worksheet','WORKSHEETS'),
        ('mcq','MCQs'),
        ('examplar_math', 'EXAMPLAR MATHS'),
        ('nmms_material','NMMS MATERIAL'),
        ('nmms_question_paper','NMMS QUESTION PAPER'),
        ('ict','ICT AND SIMULATIONS'),
        ('ifp_usage','IFP USAGE VIDEO'),
        ('teacher_hand_book','TEACHER HAND BOOKS'),
        ('tlm_photos','TLM PHOTOS'),
        ('lab_manuals','LAB MANUALS'),
        ('keys','PRINCIPLES OF VALUATION / KEYS'),
        ('hot','CASE STUDY & HOT QUESTIONS'),
        ('mind_maps','MIND MAPS'),
        ('quiz', 'QUIZZES'),
        ('other','OTHERS'),
    )
    request_for = models.CharField(max_length=100, choices=REQUEST_CHOICES)
    message = models.TextField('your message')
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10, blank=True, validators=[RegexValidator(regex='^(\+?\d{1,3})?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$')])
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['date_added']
        verbose_name = 'Teahcers request'
        verbose_name_plural = 'Teachers requests'
    def __str__(self) -> str:
        return self.request_for +' by  '+self.name

