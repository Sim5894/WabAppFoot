from django.urls import path
from .import views


urlpatterns =[
    path('', views.covoit, name='covoit'),
    path('add/', views.addcovoit, name='addcovoit'),
]



