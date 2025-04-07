from django.shortcuts import render
from .models import About


# Create your views here.
def about_me(request):
    """
    Display an individual :model:`home.Post`.

    **Context**

    ``post``
        An instance of :model:`home.Post`.

    **Template:**

    :template:`home/post_detail.html`
    """
    about = About.objects.all().order_by('-updated_on').first()

    return render(
            request,
            "about/about.html",
            {"about": about},
            )
