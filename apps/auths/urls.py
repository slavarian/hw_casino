
''' AUTHS URLS'''

from django.contrib import admin
from django.urls import path

from auths.views import RegisterView , LoginView
from . import views

urlpatterns = [
    path('reg/', RegisterView.as_view()),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'), 
    path('profile/', views.profile, name='profile'),
    ]

