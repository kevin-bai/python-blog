from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    article1 = models.Article.objects.get(pk=1)
    article2 = models.Article.objects.get(pk=2)

    return render(request, 'blog/index.html', {'article': article2})


def home(request):
    return render(request, 'blog/home/home.html', {'name': 'home'})
