# Generated by Django 5.0.3 on 2024-04-23 10:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_for', models.CharField(choices=[('text_book', 'TEXT BOOK'), ('other_book', 'OTHER BOOK'), ('lesson_plan', 'LESSON PLAN'), ('project', 'PROJECT WORK'), ('question_paper', 'QUESTION PAPER'), ('notes', 'TEACHING NOTES'), ('solutions', 'SOLUTIONS'), ('ppt', 'PPTs'), ('teaching_video', 'TEACHING VIDEOS'), ('other_video', 'OTHER VIDEOS'), ('worksheet', 'WORKSHEETS'), ('mcq', 'MCQs'), ('examplar_math', 'EXAMPLAR MATHS'), ('nmms_material', 'NMMS MATERIAL'), ('nmms_question_paper', 'NMMS QUESTION PAPER'), ('ict', 'ICT AND SIMULATIONS'), ('ifp_usage', 'IFP USAGE VIDEO'), ('teacher_hand_book', 'TEACHER HAND BOOKS'), ('tlm_photos', 'TLM PHOTOS'), ('lab_manuals', 'LAB MANUALS'), ('keys', 'PRINCIPLES OF VALUATION / KEYS'), ('hot', 'CASE STUDY & HOT QUESTIONS'), ('mind_maps', 'MIND MAPS'), ('quiz', 'QUIZZES'), ('other', 'OTHERS')], max_length=100)),
                ('message', models.TextField(verbose_name='your message')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(regex='^(\\+?\\d{1,3})?[-.\\s]?\\(?\\d{3}\\)?[-.\\s]?\\d{3}[-.\\s]?\\d{4}$')])),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Teahcers request',
                'verbose_name_plural': 'Teachers requests',
                'ordering': ['date_added'],
            },
        ),
    ]
