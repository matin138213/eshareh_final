# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Interest
from .models import Word


# Create your views here.
@login_required
def list_interest_user(request, slug=None):
    interest = Interest.objects.filter(user=request.user).first()
    word = interest.word.all()
    return render(request, 'favorite.html', {'words': word})

@login_required
def add_word_to_interest(request, slug):
    word = get_object_or_404(Word, slug=slug)  # Omid
    interest, created = Interest.objects.get_or_create(user=request.user)  # (obj, False)
    if word not in interest.word.all():
        interest.word.add(word)
        return HttpResponse("added word to bookmark")
    else:
        interest.word.remove(word)
        return HttpResponse("remove as bookmark")

@login_required
def profile(request):
    # context=CustomUser.objects.get(pk=request.user.pk)
    return render(request, 'profile_user.html', {'context': request.user})


def user_login(request):
    if request.method == 'POST':
        # Process the request if posted data are available
        username = request.POST['username']
        password = request.POST['password']
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return HttpResponse("ok")
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'login.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'login.html')
