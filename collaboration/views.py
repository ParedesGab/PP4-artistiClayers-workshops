from django.shortcuts import render, redirect
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
    contact_form = ContactForm(request.POST or None)

    if request.method == "POST":
        if contact_form.is_valid():
            contact_form.save()
            messages.success(
                request,
                "Thank you for contacting us! "
                "We will reply within two working days"
            )
            return redirect("contact")

        else:
            messages.error(
                request,
                "Error: Please Try Again."
            )

    template = "collaboration/collaboration.html"
    context = {
        "contact_form": contact_form,
    }
    return render(request, template, context)
