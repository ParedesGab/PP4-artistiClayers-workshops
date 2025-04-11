from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Workshop
from .forms import BookingForm


class WorkshopList(generic.ListView):
    """
    Renders a list of public workshops.
    """
    queryset = Workshop.objects.filter(is_public=True)
    template_name = "workshop/workshop_list.html"
    paginate_by = 3


def workshop_detail(request, id):
    """
    Display details of a single public :model:`workshop.Workshop`.

    **Context**

    ``workshop``
        An instance of :model:`workshop.Workshop`.

    **Template:**

    :template:`workshop/workshop_detail.html`
    """
    queryset = Workshop.objects.filter(is_public=True)
    workshop = get_object_or_404(queryset, id=id)

    return render(
        request,
        "workshop/workshop_detail.html",
        {
            "workshop": workshop,
        },
    )


def booking_display(request):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``commment_count``
        A count of approved comments related to the post.
    ``commment_form``
        An instance of :form:`blog.CommentForm`.

    **Template:**

    :template:`blog/post_detail.html`
    """

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booked_by = request.user
            booking.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Thank you for your Booking! We look forward to seeing you!'
            )

    booking_form = BookingForm()

    return render(
        request,
        "workshop/booking.html",
        {
            "booking_form": booking_form
        },
    )