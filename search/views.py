from django.shortcuts import render
from django.views.generic import ListView
from . import models
from django.db.models import Q


# Create your views here.


class SearchResultListView(ListView):
    model = models.Textbook
    context_object_name = 'textbooks'       
    template_name="search/list.html"
    

    def get_queryset(self):
        query = self.request.GET.get('q')
        return models.Textbook.objects.filter(
            Q(standard__icontains=query) | Q(semester__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  |Q(title__icontains=query) 
        )
    def get_context_data(self, **kwargs):
        query = self.request.GET.get('q')
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        
        context['worksheets'] = models.Worksheet.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        context['videos'] = models.Video.objects.filter(
            Q(title__icontains=query) | Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        context['tlms'] = models.Tlm.objects.filter(
            Q(title__icontains=query) |Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['teachingvideos'] = models.Teachingvideo.objects.filter(
            Q(title__icontains=query)  |Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['solutions'] = models.Solution.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['quizzes'] = models.Quiz.objects.filter(
            Q(standard__icontains=query) | Q(topic__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(sub_topic__icontains=query)  )
        
        context['questionpapers'] = models.Questionpaper.objects.filter(
            Q(standard__icontains=query) | Q(exam__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['projects'] = models.Project.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query) | Q(exam__icontains=query) )
        
        context['ppts'] = models.Ppt.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['otherbooks'] = models.Otherbook.objects.filter(
            Q(title__icontains=query)  |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['notes'] = models.Notes.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['nmmsQuestionpapers'] = models.NmmsQuestionpaper.objects.filter(
            Q(title__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['nmmsMaterials'] = models.NmmsMaterial.objects.filter(
            Q(title__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['mindmaps'] = models.Mindmap.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(title__icontains=query)  )
        

        context['mcqs'] = models.Mcq.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        

        context['lessonplans'] = models.Lessonplan.objects.filter(
            Q(standard__icontains=query) | Q(chapter__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        

        context['labs'] = models.Lab.objects.filter(
            Q(standard__icontains=query) | Q(title__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        

        context['keys'] = models.Key.objects.filter(
            Q(standard__icontains=query) | Q(exam__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query) |Q(year__icontains=query) |
            Q(title__icontains=query)  )
        
        context['ifps'] = models.Ifp.objects.filter(
            Q(title__icontains=query)  |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        context['icts'] = models.Ict.objects.filter(
            Q(title__icontains=query) | 
            Q(uploaded_by__name__icontains=query) 
            )
        
        context['hots'] = models.Hot.objects.filter(
            Q(standard__icontains=query) | Q(title__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        

        context['handbook'] = models.Handbook.objects.filter(
            Q(standard__icontains=query) | Q(title__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        

        context['examplarmaths'] = models.Examplarmath.objects.filter(
            Q(standard__icontains=query) | Q(title__icontains=query) |
            Q(uploaded_by__name__icontains=query) |
            Q(description__icontains=query)  )
        
        
        return context