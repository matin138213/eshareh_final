from django.urls import path

from . import views

urlpatterns = [
    path("word/", views.word, name='word_list'),
    path("word/<slug:slug>/", views.word, name='word_detail'),
    path("category/", views.category, name='category-list'),
    path("category/<slug:slug>/", views.category, name='category_detail'),
    path("exam/", views.random_word_exam, name='random_word_exam'),
    path("true/", views.true_exam, name='true_exam'),
    path("false/", views.false_exam, name='false_exam'),
    path("search/", views.search, name='search'),
]
