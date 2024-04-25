"""
Django settings for apmfsite project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&e*ym5g3sj8_qf=9d50v^uqd1o^0rr7)%=1_hxydgm9a=sms3q'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'dashboard.apps.DashboardConfig', #dashboard app
    'users.apps.UsersConfig', # users app
    'textbooks.apps.TextbooksConfig', # textbooks app
    'lessonplans.apps.LessonplansConfig', # lessonplans app
    'projects.apps.ProjectsConfig', # projects app
    'quotes.apps.QuotesConfig', # quotes app
    'news.apps.NewsConfig', # news app
    'questionpapers.apps.QuestionpapersConfig', # questionpapers app
    'notes.apps.NotesConfig', # notes app
    'solutions.apps.SolutionsConfig', # solutions app
    'ppts.apps.PptsConfig', # ppts app
    'nmms_materials.apps.Nmms_materialsConfig', # NMMS Materials app
    'nmms_questionpapers.apps.Nmms_questionpapersConfig', # NMMS Materials app
    'videos.apps.VideosConfig', # videos app
    'examplarmaths.apps.ExamplarmathsConfig', # examplar maths app
    'mcqs.apps.McqsConfig', # mcqs app
    'icts.apps.IctsConfig', # ict & simulations
    'worksheets.apps.WorksheetsConfig', # worksheets app
    'otherbooks.apps.OtherbooksConfig', # otherbooks app
    'ifps.apps.IfpsConfig', # ifp videos app
    'handbooks.apps.HandbooksConfig', # teacher hand books app
    'posts.apps.PostsConfig', # posts app
    'tlms.apps.TlmsConfig', # tlm photos app
    'labs.apps.LabsConfig', # lab manuals app
    'teachingvideos.apps.TeachingvideosConfig', # teaching videos app
    'members.apps.MembersConfig', # apmf members
    'keys.apps.KeysConfig', # principles of valuation app
    'hots.apps.HotsConfig', # cast study and hot questions
    'mindmaps.apps.MindmapsConfig', # mindmaps
    'quizzes.apps.QuizzesConfig', # quizzes app
    'requestitem.apps.RequestitemConfig', # request item app
    'rps.apps.RpsConfig', # rps app
    'search.apps.SearchConfig', # search app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',    
     # third party apps
    'crispy_forms',
    'crispy_bootstrap5',
    'embed_video',
    'ckeditor',
    'imagekit',
    'import_export'
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'apmfsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'apmfsite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'


USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
    ]
STATIC_DIR = os.path.join (BASE_DIR, "static")
STATIC_ROOT = os.path.join (BASE_DIR,'static files')


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR/'media'




# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'users.MyUser'

LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'



# email configuration
# Email server configuration

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'andhrapradeshmathsforum@gmail.com'
EMAIL_HOST_PASSWORD = 'mpxf idjt fppx zqji'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootsrap5"

ENTER_P    = 1 # default
ENTER_BR   = 2
ENTER_DIV  = 3

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Standard',               
        'enterMode': 2,
        'mathJaxClass': 'mathjax-latex',
        'mathJaxLib': '//cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_HTML',
        'extraPlugins': ','.join(['mathjax',]),
    },
}


