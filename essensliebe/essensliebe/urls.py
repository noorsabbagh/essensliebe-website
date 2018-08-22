"""essensliebe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from account.views import (login_view, register_view, logout_view)
from profiles.views import profile, edit_profile, edit_food_prefrences, edit_partner_prefrences, prefrences
from questions.views import questions_view, single
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from matches.views import matches_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('webapp.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('questions/', questions_view, name='questions'),
    path('questions/<int:id>/', single, name='questions_single'),
    path('profile/<str:username>/', profile, name='profile'),
    path('profile/<str:username>/edit/', edit_profile, name='edit_profile'),
    path('profile/<str:username>/prefrences', prefrences, name='prefrences'),
    path('profile/<str:username>/prefrences/partner', edit_partner_prefrences, name='edit_partner_prefrences'),
    path('profile/<str:username>/prefrences/food', edit_food_prefrences, name='edit_food_prefrences'),
    path('matches/', matches_view, name='matches_view'), 


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
