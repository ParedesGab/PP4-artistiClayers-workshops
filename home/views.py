from django.shortcuts import render


def home(request):
    """
    Renders the homepage of the website.
    Displays the content defined in the 'home/index.html' template.

    **Context**

    This view does not pass any specific context variables to the template.

    **Template**

    :template:`home/index.html`
    """

    template = "home/index.html"
    context = {}
    return render(request, template, context)
