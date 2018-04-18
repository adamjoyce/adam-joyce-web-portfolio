from django import forms

class EmailForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        label_suffix=' *',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your first name'})
    )
    last_name = forms.CharField(
        label='Last Name',
        label_suffix=' *',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your last name'})
    )
    company_name = forms.CharField(
        label='Company Name',
        label_suffix='',
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Your company name (if applicable)'}
        )
    )
    budget = forms.DecimalField(
        label='Budget',
        label_suffix=' *',
        min_value=0,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': 'Your budget in £\'s'})
    )
    email_address = forms.EmailField(
        label='Email',
        label_suffix=' *',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your email address'})
    )
    phone_number = forms.RegexField(
        label='Phone Number',
        label_suffix=' *',
        regex='^\+\d{8,15}$',
        max_length=16,
        error_messages=
            {'invalid': 'Format: +[area code][number] e.g. +449999999999'},
        widget=forms.TextInput(
            attrs={'placeholder': 'Your phone number (+[area code][number])'}
        )
    )
    project_description = forms.CharField(
        label='Project Descrition',
        label_suffix=' *',
        widget=forms.Textarea(
            attrs={'placeholder': 'A short description of your project...'}
        )
    )
