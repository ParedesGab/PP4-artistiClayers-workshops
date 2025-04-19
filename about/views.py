from django.shortcuts import render
from .models import About


# Create your views here.
def about_me(request):
    """
    Renders the information on the About page.
    Displays the first instance of :model:`about.About` ordered by title.

    **Context**

    ``about``
        The first instance of model :model:`about.About`,
        ordered alphabetically by title.

    **Template**
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('title').first()

    return render(
            request,
            "about/about.html",
            {"about": about},
            )
