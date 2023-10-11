from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_interest_user, name='list_interest_user'),
    path("<slug:slug>/", views.add_word_to_interest, name='add_word_to_interest'),
]
