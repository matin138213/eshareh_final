from django.shortcuts import render, get_object_or_404

from .models import Word, Category


# Create your views here.
def word(request, slug=None):
    queryset = get_object_or_404(Word, slug=slug)
    # category = get_object_or_404(Category, slug=slug)
    return render(request, 'word.html', {"word": queryset})


def category(request, slug=None):
    queryset = Category.objects.filter(parent__isnull=True)
    if slug:
        parent = get_object_or_404(Category, slug=slug)
        queryset = Category.objects.filter(parent=parent)
    if not queryset:
        category = get_object_or_404(Category, slug=slug)
        queryset = Word.objects.filter(category=category)
    return render(request, 'category.html', {'categories': queryset})
