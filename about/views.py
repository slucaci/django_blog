from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
from django.contrib import messages

def about_me(request):
    """
    Renders the most recent information on the website owner and allows user collaboration requests.
    Displays an individual :model:`about.About`.
    **Context**
    ``about``
        An instance of :model:`about.About`.
    ``collaborate_form``
        An instance of :form:`about.CollaborateForm`.
    :template:`about/about.html`
    """
    about = About.objects.all().order_by('-updated_on').first()
    
    # Check if the request method is POST
    if request.method == "POST":
        collaborate_form = CollaborateForm(request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Collaboration request received! I endeavour to respond within 2 working days.'
            )
    else:
        # Initialize the form in case of GET request
        collaborate_form = CollaborateForm()

    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )
