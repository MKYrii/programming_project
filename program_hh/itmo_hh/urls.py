from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("personal_account", personal_account, name='personal_account'),
    path('registration', registration, name='registration'),
    path('startapp', startapp, name='startapp'),
    path('project', project, name='project'),
    path('summary', summary, name='summary'),
    path('resume_project', resume_project, name='resume_project'),
    path('resume_person', resume_person, name='resume_person'),
    path('page_of_project', page_of_project, name='page_of_project')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
