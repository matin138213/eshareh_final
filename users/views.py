from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from word.views import word
from .models import CustomUser, Interest
from .models import Word


# Create your views here.
def list_interest_user(request, slug=None):
    interest = Interest.objects.filter(user=request.user).first()
    word = interest.word.all()
    return render(request, 'favorite.html', {'words':word})


def add_word_to_interest(request, slug):
    word = get_object_or_404(Word, slug=slug)  # Omid
    interest, created = Interest.objects.get_or_create(user=request.user)  # (obj, False)
    if word not in interest.word.all():
        interest.word.add(word)
        return HttpResponse("added word to bookmark")
    else:
        interest.word.remove(word)
        return HttpResponse("remove as bookmark")
