from django.urls import path
from . import views

urlpatterns = [
    path("list_interest_user/", views.list_interest_user, name='list_interest_user'),
    path("add_word_to_interest/<slug:slug>/", views.add_word_to_interest, name='add_word_to_interest'),
    path("profile/", views.profile, name='profile'),
]
