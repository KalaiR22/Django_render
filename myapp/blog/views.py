from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'blog/index.html')


def detail(request, post_id):
    return HttpResponse(f"Hello, world. This is blog website no {post_id}")


def welcome(request):
    return render(request, 'blog/index.html')