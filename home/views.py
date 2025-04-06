from django.shortcuts import render
from django.views import generic
from .models import Post

# from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("This will be my home page")

class PostList(generic.ListView):
    model = Post
