from django import urls
from django.contrib import admin
from django.urls import path , include

from home import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('task', views.task, name='task'),
    path('patien', views.patient , name="patien"),
    path('addpatien', views.addpatien , name="Test") ,
    path('addpatien3', views.addpatien3 , name="Test") ,
    path('addpatien4', views.addpatien4 , name="Test") ,
    path('addpatien5', views.addpatien5 , name="Test"), 
    path('addpatien6', views.addpatien6 , name="Test") ,
    path('addpatien7', views.addpatien7 , name="Test"),
    path('addpatien8', views.addpatien8 , name="Test") ,
    path('delpatien/<int:id>', views.delpatien, name='delpatien'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('login', views.login , name="patien"),



    
]

