from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import random

from users.models import Interest
from .models import Word, Category
from django.http.response import HttpResponse


@login_required
# Create your views here.
def word(request, slug=None):
    word_interest = get_object_or_404(Word, slug=slug)
    if word_interest in Interest.objects.get(user=request.user).word.all():
        has_word = True
    else:
        has_word = False
    return render(request, 'word.html', {"word": word_interest, "word_interest": has_word})


@login_required
def category(request, slug=None):
    queryset = Category.objects.filter(parent__isnull=True)
    if slug:
        parent = get_object_or_404(Category, slug=slug)
        queryset = Category.objects.filter(parent=parent)
    if not queryset:
        category = get_object_or_404(Category, slug=slug)
        queryset = Word.objects.filter(category=category)
        return render(request, 'word_list.html', {'words': queryset})

    return render(request, 'category.html', {'categories': queryset})


@login_required
def random_word_exam(request):
    random_word = random.choices(Word.objects.all(), k=4)
    selected_one_word = random.sample(random_word, k=1)
    context = {
        'random_word': random_word,
        'selected_one_word': selected_one_word[0],
    }
    return render(request, 'random.html', context)


@login_required
def true_exam(request):
    return HttpResponse("T")


@login_required
def false_exam(request):
    return HttpResponse("F")


@login_required
def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        words = Word.objects.filter(title__icontains=searched)
        return render(request, 'result.html', {'searched': searched, 'words': words})
    else:
        return render(request, 'result.html', {})
