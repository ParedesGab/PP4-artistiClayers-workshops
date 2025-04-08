from django.shortcuts import render, get_object_or_404
from django.views import generic
# from django.contrib import messages
from .models import Post
# from .forms import CommentForm

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
    template_name = "home/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`home.Post`.

    **Context**

    ``post``
        An instance of :model:`home.Post`.

    **Template:**

    :template:`home/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    # comments = post.comments.all().order_by("-created_on")
    # comment_count = post.comments.filter(approved=True).count()

    # if request.method == "POST":
    #   comment_form = CommentForm(data=request.POST)
    #   if comment_form.is_valid():
    #     comment = comment_form.save(commit=False)
    #     comment.author = request.user
    #     comment.post = post
    #     comment.save()
    #     messages.add_message(
    #       request, messages.SUCCESS,
    #       'Comment submitted and awaiting approval'
    # )
    
    # comment_form = CommentForm()

    return render(
            request,
            "home/post_detail.html",
            {"post": post,
             "coder": "Gabriela",
            #  "comments": comments,
            # "comment_count": comment_count,
            # "comment_form": comment_form,
            },
            )
