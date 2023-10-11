from django.urls import path

from . import views


urlpatterns = [
    path("", views.category, name='category-list'),
    path("", views.word, name='word_list'),
    path("<slug:slug>/", views.category, name='category_detail'),
    path("word/<slug:slug>/", views.word, name='word_detail'),
]
