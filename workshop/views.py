# from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Workshop


class WorkshopList(generic.ListView):
    """
    Renders a list of public workshops.
    """
    queryset = Workshop.objects.filter(is_public=True)
    template_name = "workshop/workshop_list.html"
    paginate_by = 3
