from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name='home'),
    path("personal_account", PersonalAccount.as_view(), name='personal_account'),
    path('registration', registration, name='registration'),
    path('startapp', Startapp.as_view(), name='startapp'),
    path('project', Projects.as_view(), name='project'),
    path('my_projects', MyProjects.as_view(), name='my_projects'),
    path('summary', summary, name='summary'),
    path('resume_project', resume_project, name='resume_project'),
    path('resume_person', resume_person, name='resume_person'),
    path('project/<int:project_id>/', PageOfProject.as_view(), name='project'),
    path('my_offers', MyOffers.as_view(), name='my_offers'),
    path('my_otclics', MyOtclics.as_view(), name='my_otclics'),
    path('competitions', Competitions.as_view(), name='competitions'),
    path('resume/<int:resume_id>/', ResumePage.as_view(), name='resume'),
    path('register', register, name='register'),
    path('login', LoginUser.as_view(), name='login'),
    path('resume/<int:resume_id>/update/', UpdateResume.as_view(), name='update'),
    path('resume/<int:resume_id>/delete/', delete_resume, name='delete'),
    path('project/<int:project_id>/delete-project/', delete_project, name='delete-project'),
    path('project/<int:project_id>/update-project/', UpdateProject.as_view(), name='update-project')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)