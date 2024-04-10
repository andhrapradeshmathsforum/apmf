"""
URL configuration for apmfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('users/', include('users.urls')), # custom users urls
    path('users/', include('django.contrib.auth.urls')),
    path('news/', include('news.urls')),
    path('textbook/', include('textbooks.urls')),
    path('lessonplan/', include('lessonplans.urls')),
    path('project/', include('projects.urls')),
    path('questionpaper/', include('questionpapers.urls')),
    path('notes/', include('notes.urls')),
    path('solutions/', include('solutions.urls')),
    path('ppts/', include('ppts.urls')),
    path('nmms-material/', include('nmms_materials.urls')),
    path('nmms-questionpaper/', include('nmms_questionpapers.urls')),
    path('videos/', include('videos.urls')),
    path('examplar-math/', include('examplarmaths.urls')),
    path('mcqs/', include('mcqs.urls')),
    path('ict-simulations/', include('icts.urls')),
    path('worksheets/', include('worksheets.urls')), 
    path('otherbooks/', include('otherbooks.urls')),
    path('ifp-usage/', include('ifps.urls')),
    path('teacher-hand-books/',include('handbooks.urls')),
]

admin.site.site_header = 'APMF Administration'
admin.site.site_title  = 'APMF'
admin.site.index_title   = 'Admin'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)