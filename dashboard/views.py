from django.shortcuts import render
from django.views.generic import TemplateView
from textbooks import views as textbook_views
from lessonplans import views as lessonplan_views
from projects import views as project_views
from questionpapers import views as questionpaper_views
from notes import views as notes_views
from solutions import views as solutions_views
from ppts import views as ppts_views
from nmms_materials import views as nmms_material_views
from nmms_questionpapers import views as nmms_questionpaper_views
from videos import views as videos_views
from examplarmaths import views as examplarmath_views
from mcqs import views as mcqs_views
from icts import views as icts_views
from worksheets import views as worksheet_views
from otherbooks import views as otherbook_views
from handbooks import views as handbook_views
from ifps import views as ifp_views
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from quotes.models import Quote
from news.models import News
from django.views.generic import DetailView
from videos.models import Video
from ifps.models import Ifp




# Create your views here.

class HomeView(TemplateView):
    template_name = "dashboard/home.html"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["quotes"] = Quote.objects.all() 
        context["news"]=News.objects.latest('date_added')
        
        return context
    
    

        return context
    
    


class DashboardView(LoginRequiredMixin,TemplateView):    
    template_name = "dashboard/dashboard.html"
    login_url = 'login'


# Dashboard Textbook views
class DashboardTextbookAddView(textbook_views.TextbookAddView):
    template_name = 'dashboard/textbooks/add.html'
    success_url = reverse_lazy('dashboard_textbook_list')

class DashboardTextbookListView(textbook_views.TextbookListView):
    template_name = 'dashboard/textbooks/list.html'
    success_url = reverse_lazy('dashboard_textbook_list')

class DashboardTextbookUpdateView(textbook_views.TextbookUpdateView):
    template_name = 'dashboard/textbooks/update.html'
    success_url = reverse_lazy('dashboard_textbook_list')

class DashboardTextbookDeleteView(textbook_views.TextbookDeleteView):
    template_name = 'dashboard/textbooks/delete.html'
    success_url = reverse_lazy('dashboard_textbook_list')

# Dashboard Lessonplans views
class DashboardLessonplanAddView(lessonplan_views.LessonplanAddView):
    template_name = 'dashboard/lessonplans/add.html'
    success_url = reverse_lazy('dashboard_lessonplan_list')

class DashboardLessonplanListView(lessonplan_views.LessonplanListView):
    template_name = 'dashboard/lessonplans/list.html'
    success_url = reverse_lazy('dashboard_lessonplan_list')

class DashboardLessonplanUpdateView(lessonplan_views.LessonplanUpdateView):
    template_name = 'dashboard/lessonplans/update.html'
    success_url = reverse_lazy('dashboard_lessonplan_list')

class DashboardLessonplanDeleteView(lessonplan_views.LessonplanDeleteView):
    template_name = 'dashboard/lessonplans/delete.html'
    success_url = reverse_lazy('dashboard_lessonplan_list')


# Dashboard Lessonplans views
class DashboardProjectAddView(project_views.ProjectAddView):
    template_name = 'dashboard/projects/add.html'
    success_url = reverse_lazy('dashboard_project_list')

class DashboardProjectListView(project_views.ProjectListView):
    template_name = 'dashboard/projects/list.html'
    success_url = reverse_lazy('dashboard_project_list')

class DashboardProjectUpdateView(project_views.ProjectUpdateView):
    template_name = 'dashboard/projects/update.html'
    success_url = reverse_lazy('dashboard_project_list')

class DashboardProjectDeleteView(project_views.ProjectDeleteView):
    template_name = 'dashboard/projects/delete.html'
    success_url = reverse_lazy('dashboard_project_list')


# Dashboard Questionpapers views
class DashboardQuestionpaperAddView(questionpaper_views.QuestionpaperAddView):
    template_name = 'dashboard/questionpapers/add.html'
    success_url = reverse_lazy('dashboard_questionpaper_list')

class DashboardQuestionpaperListView(questionpaper_views.QuestionpaperListView):
    template_name = 'dashboard/questionpapers/list.html'
    success_url = reverse_lazy('dashboard_questionpaper_list')

class DashboardQuestionpaperUpdateView(questionpaper_views.QuestionpaperUpdateView):
    template_name = 'dashboard/questionpapers/update.html'
    success_url = reverse_lazy('dashboard_questionpaper_list')

class DashboardQuestionpaperDeleteView(questionpaper_views.QuestionpaperDeleteView):
    template_name = 'dashboard/questionpapers/delete.html'
    success_url = reverse_lazy('dashboard_questionpapers_list')


# Dashboard Notes views
class DashboardNotesAddView(notes_views.NotesAddView):
    template_name = 'dashboard/notes/add.html'
    success_url = reverse_lazy('dashboard_notes_list')

class DashboardNotesListView(notes_views.NotesListView):
    template_name = 'dashboard/notes/list.html'
    success_url = reverse_lazy('dashboard_notes_list')

class DashboardNotesUpdateView(notes_views.NotesUpdateView):
    template_name = 'dashboard/notes/update.html'
    success_url = reverse_lazy('dashboard_notes_list')

class DashboardNotesDeleteView(notes_views.NotesDeleteView):
    template_name = 'dashboard/notes/delete.html'
    success_url = reverse_lazy('dashboard_notes_list')



# Dashboard Solutions views
class DashboardSolutionAddView(solutions_views.SolutionAddView):
    template_name = 'dashboard/solutions/add.html'
    success_url = reverse_lazy('dashboard_solution_list')

class DashboardSolutionListView(solutions_views.SolutionListView):
    template_name = 'dashboard/solutions/list.html'
    success_url = reverse_lazy('dashboard_solution_list')

class DashboardSolutionUpdateView(solutions_views.SolutionUpdateView):
    template_name = 'dashboard/solutions/update.html'
    success_url = reverse_lazy('dashboard_solution_list')

class DashboardSolutionDeleteView(solutions_views.SolutionDeleteView):
    template_name = 'dashboard/solutions/delete.html'
    success_url = reverse_lazy('dashboard_solution_list')


# Dashboard PPTs views
class DashboardPptAddView(ppts_views.PptAddView):
    template_name = 'dashboard/ppts/add.html'
    success_url = reverse_lazy('dashboard_ppt_list')

class DashboardPptListView(ppts_views.PptListView):
    template_name = 'dashboard/ppts/list.html'
    success_url = reverse_lazy('dashboard_ppt_list')

class DashboardPptUpdateView(ppts_views.PptUpdateView):
    template_name = 'dashboard/ppts/update.html'
    success_url = reverse_lazy('dashboard_ppt_list')

class DashboardPptDeleteView(ppts_views.PptDeleteView):
    template_name = 'dashboard/ppt/delete.html'
    success_url = reverse_lazy('dashboard_ppt_list')


# Dashboard NMMS materials views
class DashboardNmmsMaterialAddView(nmms_material_views.NmmsMaterialAddView):
    template_name = 'dashboard/nmms_materials/add.html'
    success_url = reverse_lazy('dashboard_nmmsMaterial_list')

class DashboardNmmsMaterialListView(nmms_material_views.NmmsMaterialListView):
    template_name = 'dashboard/nmms_materials/list.html'
    success_url = reverse_lazy('dashboard_nmmsMaterial_list')

class DashboardNmmsMaterialUpdateView(nmms_material_views.NmmsMaterialUpdateView):
    template_name = 'dashboard/nmms_materials/update.html'
    success_url = reverse_lazy('dashboard_nmmsMaterial_list')

class DashboardNmmsMaterialDeleteView(nmms_material_views.NmmsMaterialDeleteView):
    template_name = 'dashboard/nmms_materials/delete.html'
    success_url = reverse_lazy('dashboard_nmmsMaterial_list')


# Dashboard NMMS questionpapers views
class DashboardNmmsQuestionpaperAddView(nmms_questionpaper_views.NmmsQuestionpaperAddView):
    template_name = 'dashboard/nmms_questionpapers/add.html'
    success_url = reverse_lazy('dashboard_nmmsQuestionpaper_list')

class DashboardNmmsQuestionpaperListView(nmms_questionpaper_views.NmmsQuestionpaperListView):
    template_name = 'dashboard/nmms_questionpapers/list.html'
    success_url = reverse_lazy('dashboard_nmmsQuestionpaper_list')

class DashboardNmmsQuestionpaperUpdateView(nmms_questionpaper_views.NmmsQuestionpaperUpdateView):
    template_name = 'dashboard/nmms_questionpapers/update.html'
    success_url = reverse_lazy('dashboard_nmmsQuestionpaper_list')

class DashboardNmmsQuestionpaperDeleteView(nmms_questionpaper_views.NmmsQuestionpaperDeleteView):
    template_name = 'dashboard/nmms_questionpapers/delete.html'
    success_url = reverse_lazy('dashboard_nmmsQuestionpaper_list')


# Dashboard videos views
class DashboardVideoAddView(videos_views.VideoAddView):
    template_name = 'dashboard/videos/add.html'
    success_url = reverse_lazy('dashboard_video_list')

class DashboardVideoListView(videos_views.VideoListView):
    template_name = 'dashboard/videos/list.html'
    success_url = reverse_lazy('dashboard_video_list')

class DashboardVideoUpdateView(videos_views.VideoUpdateView):
    template_name = 'dashboard/videos/update.html'
    success_url = reverse_lazy('dashboard_video_list')

class DashboardVideoDeleteView(videos_views.VideoDeleteView):
    template_name = 'dashboard/videos/delete.html'
    success_url = reverse_lazy('dashboard_video_list')


class DashboardVideoDetailView(DetailView):
    model = Video
    template_name = "dashboard/videos/details.html"
    context_object_name= 'video'

# Dashboard examplar maths views
class DashboardExamplarmathAddView(examplarmath_views.ExamplarmathAddView):
    template_name = 'dashboard/examplarmaths/add.html'
    success_url = reverse_lazy('dashboard_examplarmath_list')

class DashboardExamplarmathListView(examplarmath_views.ExamplarmathListView):
    template_name = 'dashboard/examplarmaths/list.html'
    success_url = reverse_lazy('dashboard_examplarmath_list')

class DashboardExamplarmathUpdateView(examplarmath_views.ExamplarmathUpdateView):
    template_name = 'dashboard/examplarmaths/update.html'
    success_url = reverse_lazy('dashboard_examplarmath_list')

class DashboardExamplarmathDeleteView(examplarmath_views.ExamplarmathDeleteView):
    template_name = 'dashboard/examplarmaths/delete.html'
    success_url = reverse_lazy('dashboard_examplarmath_list')
    context_object_name = 'examplarmath'

# Dashboard mcqs views
class DashboardMcqAddView(mcqs_views.McqAddView):
    template_name = 'dashboard/mcqs/add.html'
    success_url = reverse_lazy('dashboard_mcq_list')

class DashboardMcqListView(mcqs_views.McqListView):
    template_name = 'dashboard/mcqs/list.html'
    success_url = reverse_lazy('dashboard_mcq_list')

class DashboardMcqUpdateView(mcqs_views.McqUpdateView):
    template_name = 'dashboard/mcqs/update.html'
    success_url = reverse_lazy('dashboard_mcq_list')

class DashboardMcqDeleteView(mcqs_views.McqDeleteView):
    template_name = 'dashboard/mcqs/delete.html'
    success_url = reverse_lazy('dashboard_mcq_list')
    context_object_name = 'mcq'


# Dashboard icts views
class DashboardIctAddView(icts_views.IctAddView):
    template_name = 'dashboard/icts/add.html'
    success_url = reverse_lazy('dashboard_ict_list')

class DashboardIctListView(icts_views.IctListView):
    template_name = 'dashboard/icts/list.html'
    success_url = reverse_lazy('dashboard_ict_list')

class DashboardIctUpdateView(icts_views.IctUpdateView):
    template_name = 'dashboard/icts/update.html'
    success_url = reverse_lazy('dashboard_ict_list')

class DashboardIctDeleteView(icts_views.IctDeleteView):
    template_name = 'dashboard/icts/delete.html'
    success_url = reverse_lazy('dashboard_ict_list')
    context_object_name = 'ict'



# Dashboard worksheet views
class DashboardWorksheetAddView(worksheet_views.WorksheetAddView):
    template_name = 'dashboard/worksheets/add.html'
    success_url = reverse_lazy('dashboard_worksheet_list')

class DashboardWorksheetListView(worksheet_views.WorksheetListView):
    template_name = 'dashboard/worksheets/list.html'
    success_url = reverse_lazy('dashboard_worksheet_list')

class DashboardWorksheetUpdateView(worksheet_views.WorksheetUpdateView):
    template_name = 'dashboard/worksheets/update.html'
    success_url = reverse_lazy('dashboard_worksheet_list')

class DashboardWorksheetDeleteView(worksheet_views.WorksheetDeleteView):
    template_name = 'dashboard/worksheets/delete.html'
    success_url = reverse_lazy('dashboard_worksheet_list')
    context_object_name = 'worksheet'



# Dashboard other books views
class DashboardOtherbookAddView(otherbook_views.OtherbookAddView):
    template_name = 'dashboard/otherbooks/add.html'
    success_url = reverse_lazy('dashboard_otherbook_list')

class DashboardOtherbookListView(otherbook_views.OtherbookListView):
    template_name = 'dashboard/otherbooks/list.html'
    success_url = reverse_lazy('dashboard_otherbook_list')

class DashboardOtherbookUpdateView(otherbook_views.OtherbookUpdateView):
    template_name = 'dashboard/otherbooks/update.html'
    success_url = reverse_lazy('dashboard_otherbook_list')

class DashboardOtherbookDeleteView(otherbook_views.OtherbookDeleteView):
    template_name = 'dashboard/otherbooks/delete.html'
    success_url = reverse_lazy('dashboard_otherbook_list')
    context_object_name = 'otherbook'


# Dashboard ifp views
class DashboardIfpAddView(ifp_views.IfpAddView):
    template_name = 'dashboard/ifps/add.html'
    success_url = reverse_lazy('dashboard_ifp_list')

class DashboardIfpListView(ifp_views.IfpListView):
    template_name = 'dashboard/ifps/list.html'
    success_url = reverse_lazy('dashboard_ifp_list')

class DashboardIfpUpdateView(ifp_views.IfpUpdateView):
    template_name = 'dashboard/ifps/update.html'
    success_url = reverse_lazy('dashboard_ifp_list')

class DashboardIfpDeleteView(ifp_views.IfpDeleteView):
    template_name = 'dashboard/ifps/delete.html'
    success_url = reverse_lazy('dashboard_ifp_list')
    context_object_name = 'otherbook'

class DashboardIfpDetailView(DetailView):
    model = Ifp
    template_name = "dashboard/ifps/details.html"
    context_object_name= 'ifp'


# Dashboard handbook views
class DashboardHandbookAddView(handbook_views.HandbookAddView):
    template_name = 'dashboard/handbooks/add.html'
    success_url = reverse_lazy('dashboard_handbook_list')

class DashboardHandbookListView(handbook_views.HandbookListView):
    template_name = 'dashboard/handbooks/list.html'
    success_url = reverse_lazy('dashboard_handbook_list')

class DashboardHandbookUpdateView(handbook_views.HandbookUpdateView):
    template_name = 'dashboard/handbooks/update.html'
    success_url = reverse_lazy('dashboard_handbook_list')

class DashboardHandbookDeleteView(handbook_views.HandbookDeleteView):
    template_name = 'dashboard/handbooks/delete.html'
    success_url = reverse_lazy('dashboard_handbook_list')
    context_object_name = 'otherbook'

