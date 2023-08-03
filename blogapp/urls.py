"""
URL configuration for blogpro project.

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
from django.urls import path
from blogapp import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('single', views.single, name='single'),
    path('typography', views.typography, name='typography'),


    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),

    path('blogpost', views.blogpost, name = 'blogpost'),
    
    path('blogs', views.blogs, name = 'blogs'),


]
