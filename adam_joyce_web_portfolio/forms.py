from django import forms

class EmailForm(forms.Form):
    first_name = forms.CharField(
        label='First Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your first name'})
    )
    last_name = forms.CharField(
        label='Last Name',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your last name'})
    )
    company_name = forms.CharField(
        label='Company Name',
        max_length=100,
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Your company name (if applicable)'}
        )
    )
    budget = forms.DecimalField(
        label='Budget',
        min_value=0,
        decimal_places=2,
        widget=forms.TextInput(attrs={'placeholder': 'Your budget in £\'s'})
    )
    email_address = forms.EmailField(
        label='Email',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Your email address'})
    )
    project_description = forms.CharField(
        label='Project Descrition',
        widget=forms.Textarea(
            attrs={'placeholder': 'A short description of your project...'}
        )
    )
