from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def booking_display(request):
    """
    Displays the booking form for authenticated users
    and lists their existing bookings.

    **Context**

    ``booking_form``
        An instance of :form:`workshop.forms.BookingForm`,
        either an empty form for GET requests or
        a populated form with user input for POST requests.

    ``bookings``
        A queryset of :model:`workshop.Booking` instances
        associated with the currently logged-in user,
        ordered by appointment date in descending order.

    **Template:**

    :template:`workshop/booking.html`
    """
    user_bookings = Booking.objects.filter(
        booked_by=request.user).order_by('-appointment_date')

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.booked_by = request.user
            booking.save()
            messages.success(
                request,
                'Thank you for your booking! We look forward to seeing you!'
                )
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


@login_required
def booking_edit(request, id):
    """
    Handles the editing of a single :model:`workshop.Booking` instance.

    Allows an authenticated user to modify their own booking
    identified by the provided ID.
    If the user does not own the booking, they are redirected
    with an error message.
    On successful form submission (POST request), the booking is updated.

    **Context**

    ``booking_form``
        An instance of :form:`workshop.forms.BookingForm`,
        initialized with the existing booking data for
        GET requests or populated with user input for POST requests.

    **Template:**

    :template:`workshop/booking_edit.html`
    """

    booking = get_object_or_404(Booking, pk=id)

    if booking.booked_by != request.user:
        messages.add_message(
                request, messages.ERROR,
                'You do not have permission to edit this booking'
                )
        return redirect(reverse('bookings'))

    booking_form = BookingForm(instance=booking)

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST, instance=booking)

        if booking_form.is_valid() and booking.booked_by == request.user:
            booking = booking_form.save(commit=False)
            booking.save()
            messages.add_message(request, messages.SUCCESS, 'booking Updated!')
            return redirect(reverse('bookings'))
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating booking!'
                )

    return render(
        request,
        "workshop/booking_edit.html",
        {"booking_form": booking_form},
        )


@login_required
def booking_delete(request, id):
    """
    Handles the deletion of a single :model:`workshop.Booking` instance.

    Allows an authenticated user to delete their own booking
    identified by the provided ID.
    If the user does not own the booking, they are redirected
    with an error message.
    Deletion occurs upon a POST request.

    **Context**

    ``booking``
        An instance of :model:`workshop.Booking` to be deleted,
        retrieved based on the provided ID.

    **Template:**

    :template:`workshop/booking_delete.html`
    """

    booking = get_object_or_404(Booking, pk=id)

    if booking.booked_by != request.user:
        messages.add_message(
                request, messages.ERROR,
                'You do not have permission to delete this booking'
                )
        return redirect(reverse('bookings'))

    if request.method == 'POST':
        booking.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Booking deleted!')
        return redirect(reverse('bookings'))

    return render(
        request,
        "workshop/booking_delete.html",
        {"booking": booking},
        )
