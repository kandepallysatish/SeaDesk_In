from django.contrib import admin
from django.urls import path, include
from apps import views
from django.conf import settings
from django.conf.urls.static import static

# login, register, logout
import apps.views as user_view
from django.contrib.auth import views as auth_view


urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.registerPage, name="register"),     # LOGIN, LOGOUT, REGISTER
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('new-question', views.newQuestionPage, name='new-question'),
    path('question/<int:id>', views.questionPage, name='question'),
    path('reply', views.replyPage, name='reply'),
    path("classes", views.classes, name="classes"),       # FOR QUESTIONS & ANSWERS
    path("animes", views.animes, name="animes"),       # FOR ANIMES
    path("animesview/<int:ids>", views.animesview, name="animesview"),
    path("searchanimes", views.searchanimes, name="searchanimes"),
    path("jobupdates", views.jobupdates, name="jobupdates"),        # FOR JOBS
    path("jobupdatesview/<int:id>", views.jobupdatesview, name='jobupdatesview'),
#   path("plagiarism", views.plagiarism, name='plagiarism'),   LINK https://github.com/TristanPerry/plagiarism-detection-software
    path("contact", views.contact, name="contact"),       # FOR CONTACT US
]
