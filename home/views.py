from django.shortcuts import render
from django.views import generic
from .models import Post

# from django.http import HttpResponse


# Create your views here.
# def index(request):
#     return HttpResponse("This will be my home page")

class PostList(generic.ListView):
    # model = Post
    queryset = Post.objects.all()
    # queryset = Post.objects.filter(author=1)
    # queryset = Post.objects.all().order_by("-created_on")
    # queryset = Post.objects.filter(status=1)
    template_name = "post_list.html"

