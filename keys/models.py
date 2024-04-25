from django.db import models
from dashboard.models import Item

# Create your models here.

class Key(Item):
    EXAM_CHOICES = (
        ('FA1','FA1'),
        ('FA2','FA2'),
        ('FA3','FA3'),
        ('FA4', 'FA4'),
        ('SA1', 'SA1'),
        ('SA2', 'SA2'),
        ('PREPUBLIC','PREPUBLIC'),
        ('PUBLIC', 'PUBLIC'),
    )
    YEAR_CHOICES = (
        ('2023-24','2023-24'),
        ('2024-25','2024-25'),
        ('2025-26', '2025-26'),
        ('2026-27','2026-27')
    )
    exam = models.CharField(max_length=10, choices=EXAM_CHOICES)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Principles of Valuation'
        verbose_name_plural = 'Principles of Valuation'
        ordering =[
            '-standard',
            'exam',
            'year'
        ]

    def __str__(self) -> str:
        return self.title
    
