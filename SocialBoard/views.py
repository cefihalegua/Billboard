from django.shortcuts import render, reverse

# Create your views here.
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone




@login_required
def index(request):
    posts = Post.objects.all()
    return render(request, 'SocialBoard/index.html', {'posts': posts})


def logout(request):
    return render(request, "registration/logout.html")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse("main"))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {"form": form})

@csrf_protect
def newpost(request):
    content = request.POST.get("content")
    title = request.POST.get("title")
    author = request.POST.get("author")
    Post.objects.create(title=title, publish_date=timezone.now(), author=author, content=content)
    posts = Post.objects.all()
    return render(request, 'SocialBoard/index.html', {'posts': posts})