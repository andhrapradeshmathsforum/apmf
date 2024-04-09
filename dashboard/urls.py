from django.urls import path
from .import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home' ),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),

    # dash board textbooks path
    path('dashboard/textbooks/', views.DashboardTextbookListView.as_view(), name='dashboard_textbook_list'),
    path('dashboard/textbooks/add/', views.DashboardTextbookAddView.as_view(), name='dashboard_textbook_add'),
    path('dashboard/textbooks/update/<int:pk>/', views.DashboardTextbookUpdateView.as_view(), name='dashboard_textbook_update'),
    path('dashboard/textbooks/delete/<int:pk>/', views.DashboardTextbookDeleteView.as_view(), name='dashboard_textbook_delete'),

     # dash board lessonplan path
    path('dashboard/lessonplans/', views.DashboardLessonplanListView.as_view(), name='dashboard_lessonplan_list'),
    path('dashboard/lessonplans/add/', views.DashboardLessonplanAddView.as_view(), name='dashboard_lessonplan_add'),
    path('dashboard/lessonplans/update/<int:pk>/', views.DashboardLessonplanUpdateView.as_view(), name='dashboard_lessonplan_update'),
    path('dashboard/lessonplans/delete/<int:pk>/', views.DashboardLessonplanDeleteView.as_view(), name='dashboard_lessonplan_delete'),

     # dash board projects path
    path('dashboard/projects/', views.DashboardProjectListView.as_view(), name='dashboard_project_list'),
    path('dashboard/projects/add/', views.DashboardProjectAddView.as_view(), name='dashboard_project_add'),
    path('dashboard/projects/update/<int:pk>/', views.DashboardProjectUpdateView.as_view(), name='dashboard_project_update'),
    path('dashboard/projects/delete/<int:pk>/', views.DashboardProjectDeleteView.as_view(), name='dashboard_project_delete'),


     # dash board questionpaper path
    path('dashboard/questionpapers/', views.DashboardQuestionpaperListView.as_view(), name='dashboard_questionpaper_list'),
    path('dashboard/questionpapers/add/', views.DashboardQuestionpaperAddView.as_view(), name='dashboard_questionpaper_add'),
    path('dashboard/questionpapers/update/<int:pk>/', views.DashboardQuestionpaperUpdateView.as_view(), name='dashboard_questionpaper_update'),
    path('dashboard/questionpapers/delete/<int:pk>/', views.DashboardQuestionpaperDeleteView.as_view(), name='dashboard_questionpaper_delete'),


    # dash board notes path
    path('dashboard/notes/', views.DashboardNotesListView.as_view(), name='dashboard_notes_list'),
    path('dashboard/notes/add/', views.DashboardNotesAddView.as_view(), name='dashboard_notes_add'),
    path('dashboard/notes/update/<int:pk>/', views.DashboardNotesUpdateView.as_view(), name='dashboard_notes_update'),
    path('dashboard/notes/delete/<int:pk>/', views.DashboardNotesDeleteView.as_view(), name='dashboard_notes_delete'),


# dash board notes path
    path('dashboard/solutions/', views.DashboardSolutionListView.as_view(), name='dashboard_solution_list'),
    path('dashboard/solutions/add/', views.DashboardSolutionAddView.as_view(), name='dashboard_solution_add'),
    path('dashboard/solutions/update/<int:pk>/', views.DashboardSolutionUpdateView.as_view(), name='dashboard_solution_update'),
    path('dashboard/solutions/delete/<int:pk>/', views.DashboardSolutionDeleteView.as_view(), name='dashboard_solution_delete'),


# dash board ppts path
    path('dashboard/ppts/', views.DashboardPptListView.as_view(), name='dashboard_ppt_list'),
    path('dashboard/ppts/add/', views.DashboardPptAddView.as_view(), name='dashboard_ppt_add'),
    path('dashboard/ppts/update/<int:pk>/', views.DashboardPptUpdateView.as_view(), name='dashboard_ppt_update'),
    path('dashboard/ppts/delete/<int:pk>/', views.DashboardPptDeleteView.as_view(), name='dashboard_ppt_delete'),

# dash board nmms material path
    path('dashboard/nmms-material/', views.DashboardNmmsMaterialListView.as_view(), name='dashboard_nmmsMaterial_list'),
    path('dashboard/nmms-material/add/', views.DashboardNmmsMaterialAddView.as_view(), name='dashboard_nmmsMaterial_add'),
    path('dashboard/nmms-material/update/<int:pk>/', views.DashboardNmmsMaterialUpdateView.as_view(), name='dashboard_nmmsMaterial_update'),
    path('dashboard/nmms-material/delete/<int:pk>/', views.DashboardNmmsMaterialDeleteView.as_view(), name='dashboard_nmmsMaterial_delete'),

# dash board nmms questionpapers path
    path('dashboard/nmms-questionpaper/', views.DashboardNmmsQuestionpaperListView.as_view(), name='dashboard_nmmsQuestionpaper_list'),
    path('dashboard/nmms-questionpaper/add/', views.DashboardNmmsQuestionpaperAddView.as_view(), name='dashboard_nmmsQuestionpaper_add'),
    path('dashboard/nmms-questionpaper/update/<int:pk>/', views.DashboardNmmsQuestionpaperUpdateView.as_view(), name='dashboard_nmmsQuestionpaper_update'),
    path('dashboard/nmms-questionpaper/delete/<int:pk>/', views.DashboardNmmsQuestionpaperDeleteView.as_view(), name='dashboard_nmmsQuestionpaper_delete'),


# dash board videos path
    path('dashboard/video/', views.DashboardVideoListView.as_view(), name='dashboard_video_list'),
    path('dashboard/video/add/', views.DashboardVideoAddView.as_view(), name='dashboard_video_add'),
    path('dashboard/video/update/<int:pk>/', views.DashboardVideoUpdateView.as_view(), name='dashboard_video_update'),
    path('dashboard/video/delete/<int:pk>/', views.DashboardVideoDeleteView.as_view(), name='dashboard_video_delete'),
    path('dashboard/video/detials/<int:pk>/', views.DashboardVideoDetailView.as_view(), name='dashboard_video_detail'),


# dash board examplar math path
    path('dashboard/examplar-math/', views.DashboardExamplarmathListView.as_view(), name='dashboard_examplarmath_list'),
    path('dashboard/examplar-math/add/', views.DashboardExamplarmathAddView.as_view(), name='dashboard_examplarmath_add'),
    path('dashboard/examplar-math/<int:pk>/', views.DashboardExamplarmathUpdateView.as_view(), name='dashboard_examplarmath_update'),
    path('dashboard/examplar-math/delete/<int:pk>/', views.DashboardExamplarmathDeleteView.as_view(), name='dashboard_examplarmath_delete'),

# dash board mcqs path
    path('dashboard/mcqs/', views.DashboardMcqListView.as_view(), name='dashboard_mcq_list'),
    path('dashboard/mcqs/add/', views.DashboardMcqAddView.as_view(), name='dashboard_mcq_add'),
    path('dashboard/mcqs/<int:pk>/', views.DashboardMcqUpdateView.as_view(), name='dashboard_mcq_update'),
    path('dashboard/mcqs/delete/<int:pk>/', views.DashboardMcqDeleteView.as_view(), name='dashboard_mcq_delete'),


# dash board icts path
    path('dashboard/icts/', views.DashboardIctListView.as_view(), name='dashboard_ict_list'),
    path('dashboard/icts/add/', views.DashboardIctAddView.as_view(), name='dashboard_ict_add'),
    path('dashboard/icts/<int:pk>/', views.DashboardIctUpdateView.as_view(), name='dashboard_ict_update'),
    path('dashboard/icts/delete/<int:pk>/', views.DashboardIctDeleteView.as_view(), name='dashboard_ict_delete'),

# dash board worksheet path
    path('dashboard/worksheets/', views.DashboardWorksheetListView.as_view(), name='dashboard_worksheet_list'),
    path('dashboard/worksheets/add/', views.DashboardWorksheetAddView.as_view(), name='dashboard_worksheet_add'),
    path('dashboard/worksheets/<int:pk>/', views.DashboardWorksheetUpdateView.as_view(), name='dashboard_worksheet_update'),
    path('dashboard/worksheets/delete/<int:pk>/', views.DashboardWorksheetDeleteView.as_view(), name='dashboard_worksheet_delete'),
    
    
    
    
]



