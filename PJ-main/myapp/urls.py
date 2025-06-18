"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path 
from myapp.views import *

urlpatterns = [
    
    path('disease/', disease_view.as_view()),
    path('disease/<int:id>/', disease_view.as_view()),

    path('medicine/', medicine_view.as_view()),
    path('medicine/<int:id>/', medicine_view.as_view()),

    path('health_parameters/', health_parameters_view.as_view()),
    path('health_parameters/<int:id>/', health_parameters_view.as_view()),
    
    path('sub_health_parameters/', sub_health_parameters_view.as_view()),
    path('sub_health_parameters/<int:id>/', sub_health_parameters_view.as_view()),
 
    path('ask_to_expert/', ask_to_expert_view.as_view()),
    path('ask_to_expert/<int:id>/', ask_to_expert_view.as_view()), 

    path('order/', order_view.as_view()),
    path('order/<int:id>/', order_view.as_view()),  

    path('user_data/', user_view.as_view()),
    path('user_data/<str:id>/', user_view.as_view()),
    path('user_login/', user_login_view.as_view(), name='user_login'),
    
    path('ad/', advertisement_view.as_view()),
    path('ad/<int:id>/', advertisement_view.as_view()),
    
    path('contact_us/', contact_us_view.as_view()),
    path('contact_us/<int:id>/', contact_us_view.as_view()),

    path('plan/', plan_View.as_view()),
    path('plan/<int:id>/', plan_View.as_view()),

    path('membership/', membership_View.as_view()),
    path('membership/<int:id>/', membership_View.as_view()),

    path('admin_login/', admin_login_view.as_view()),
    

]
