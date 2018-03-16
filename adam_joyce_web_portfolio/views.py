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
            # Process the form.cleaned_data as needed.
            data = form.cleaned_data
            text_content = ('Full Name: %s %s\n'
                             'Comapny Name: %s\n'
                             'Budget: %d\n'
                             'Email: %s\n'
                             'Message: %s' %(data['first_name'],
                                             data['last_name'],
                                             data['company_name'],
                                             data['budget'],
                                             data['email_address'],
                                             data['project_description']))

            # Send the email.
            send_mail('Website Project Enquiry',
                      text_content,
                      'djangotest150@gmail.com',
                      ['djangotest150@gmail.com'])

            # Redirect to thank you page.
            return HttpResponseRedirect('#')
    else:
        # The request if a GET or other method so create a blank form.
        form = EmailForm()
    return render(request, 'contact.html', {'form': form})
