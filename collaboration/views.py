from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_form(request):
    """
    Allows user collaboration request.

    **Context**
    ``contact_form``
        An instance of :form:`collaboration.ContactForm`.

    **Template**
    :template:`collaboration/collaboration.html`

    """
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Thank you for contacting us! We reply within two working days")

    contact_form = ContactForm()
    return render(
            request,
            "collaboration/collaboration.html",
            {
                "contact_form": contact_form
            },
    )
