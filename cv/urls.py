from django.urls import path
from . import views

app_name = 'cv'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('create-resume/', views.resume_form, name='create-resume'),
    path('resume/<int:id>/', views.final_resume, name='final-resume'),
    path('resume/list', views.list_view, name='list'),
]
