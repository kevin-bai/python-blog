from django.shortcuts import render
from django.http import HttpResponse
from . import models


def index(request):
    article1 = models.Article.objects.get(pk=1)
    articles = models.Article.objects.all()

    return render(request, 'blog/index.html', {'article': article1, 'articles': articles})


def home(request):
    return render(request, 'blog/home/home.html', {'name': 'home'})
