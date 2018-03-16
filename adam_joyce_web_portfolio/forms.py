from django import forms

class EmailForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    company_name = forms.CharField(label='Company Name',
                                   max_length=100)
    budget = forms.DecimalField(label='Budget', min_value=0, decimal_places=2)
    email_address = forms.EmailField(label='Email', max_length=100)
    project_description = forms.CharField(label='Project Descrition',
                                          widget=forms.Textarea)
