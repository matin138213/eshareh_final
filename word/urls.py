from django.urls import path

from . import views
from . views import word,category


urlpatterns=[
    path("", views.word, name='word'),
    path("<slug:slug>/", views.word,name='word'),
    path("<slug:slug>/", views.category, name='category'),
    path("", views.category, name='category-list'),
]