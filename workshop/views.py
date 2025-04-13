from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Workshop, Booking
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
    Displays the booking form and handles booking submissions.
    """
    if request.user.is_authenticated:
        user_bookings = Booking.objects.filter(
            booked_by=request.user).order_by('-appointment_date')
    else:
        user_bookings = None

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booked_by = request.user
            booking.save()
            messages.success(
                request, 'Thank you! We look forward to seeing you!')
            return redirect(reverse('bookings'))
    else:
        booking_form = BookingForm()

    return render(
        request,
        "workshop/booking.html",
        {
            "booking_form": booking_form,
            'bookings': user_bookings,
        },
    )

# This view returns you to the ? webpage after you've edited the comment
# This return is done with a HttpResponseRedirect and reverse to refresh the post_detail view.


def booking_edit(request, id):
    """
    view to edit comments
    """
    if request.method == "POST":
        # queryset = Workshop.objects.filter(is_public=True)
        # workshop = get_object_or_404(queryset, slug=slug)
        booking = get_object_or_404(Booking, pk=id)
        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid() and booking.booked_by == request.user:
            booking = booking_form.save(commit=False)
            # comment.workshop = booking
            booking.approved = False
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'booking Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating booking!'
                )

    return render(
        request,
        "workshop/booking.html",
        {"booking_form": booking_form},
        )

    # return HttpResponseRedirect(reverse('post_detail', args=[slug]))
