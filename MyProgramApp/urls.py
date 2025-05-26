from django.urls import path
from . import views
from .views import (
    ProgramListView,
    program_create,
    program_detail,
    program_update,
    program_delete
)


app_name = 'MyProgramApp'

urlpatterns = [
    path('', views.ProgramListView.as_view(), name='program_list'),
    path('create/', views.program_create, name='program_create'),
    path('<int:pk>/', views.program_detail, name='program_detail'),
    path('<int:pk>/update/', views.program_update, name='program_update'),
    path('<int:pk>/delete/', views.program_delete, name='program_delete'),
]
