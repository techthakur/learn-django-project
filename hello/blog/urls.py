from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.bloghome, name="bloghome"),
    path('blogpost', views.blogpost, name="blogpost"),
]
