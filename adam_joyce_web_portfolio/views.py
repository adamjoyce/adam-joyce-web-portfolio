from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from .forms import EmailForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    # If it is a POST request process the form data.
    if request.method == 'POST':
        # Create a form instance and populate it with data from the POST
        # request.
        form = EmailForm(request.POST)
        if form.is_valid():
            # Process dat in form.cleaned_data as needed.

            # Send the email.
            send_mail('Website Project Enquiry',
                      form.cleaned_data['project_description'],
                      'djangotest150@gmail.com',
                      ['djangotest150@gmail.com'])

            # Redirect to thank you page.
            return HttpResponseRedirect('#')
    else:
        # The request if a GET or other method so create a blank form.
        form = EmailForm()
    return render(request, 'contact.html', {'form': form})
