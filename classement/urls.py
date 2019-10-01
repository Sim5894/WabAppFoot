from django.urls import path
from .import views


urlpatterns =[
    path('', views.calendrier, name='calendrier'),
    path('progra/', views.progra, name='progra'),
    path('encode/', views.encode, name='encode'),

]

