from django.urls import path
from . import views

app_name = 'DataBaseApp'

urlpatterns = [
    path('', views.page_detail, {'slug': 'me'},
         name='home'),
    path('programma/', views.page_detail,
         {'slug': 'programma'}, name='program'),
    path('management/', views.management_view, name='management'),
    path('students/', views.classmates_list, name='classmates'),
    path('<slug:slug>/', views.page_detail, name='page_detail'),
]
