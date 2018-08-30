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
from profiles.views import profile, edit_profile, edit_food_prefrences, edit_partner_prefrences, prefrences, user_compose
from questions.views import questions_view, single
from directmessage.views import inbox, sent, compose, view_direct_message, reply
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from matches.views import matches_view
from likes.views import like_user
from dating.views import date_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('webapp.urls')),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),
    path('questions/', questions_view, name='questions'),
    path('questions/<int:id>/', single, name='questions_single'),
    path('directmessage/inbox', inbox, name='inbox'),
    path('directmessage/sent', sent, name='sent'),
    path('directmessage/compose', compose, name='compose'),
    path('directmessage/view/<int:dm_id>/', view_direct_message, name='view_direct_message'),
    path('directmessage/view/<int:dm_id>/reply/', reply, name='reply'),
    path('profile/<str:username>/', profile, name='profile'),
    path('profile/<str:username>/edit/', edit_profile, name='edit_profile'),
    path('profile/<int:user_id>/user_compose', user_compose, name='user_compose'),
    path('profile/<str:username>/prefrences', prefrences, name='prefrences'),
    path('profile/<str:username>/prefrences/partner', edit_partner_prefrences, name='edit_partner_prefrences'),
    path('profile/<str:username>/prefrences/food', edit_food_prefrences, name='edit_food_prefrences'),
    path('matches/', matches_view, name='matches_view'),
    path('like/<int:id>/', like_user, name='like_user'),
    path('dating/', date_view, name='date_view' ),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
