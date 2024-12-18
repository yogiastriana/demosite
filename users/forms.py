# forms.py
from django import forms
from django.contrib.auth.models import User
from .validators import corporate_or_educational_email_validator

class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'First Name'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Last Name'})
        self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Email Address'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Phone Number'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['confirm_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})

    def clean_email(self):
        email = self.cleaned_data.get("email")
        corporate_or_educational_email_validator(email)
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.username = self.cleaned_data["email"]
        user.is_active = False  # Set to inactive by default
        # Do not set status and role here, we will do that in the view
        if commit:
            user.save()
        return user


class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email Address")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control mt-2 mb-5', 'placeholder': 'Email Address'})



class PasswordResetConfirmForm(forms.Form):
    new_password1 = forms.CharField(label="New Password", widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="Confirm New Password", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'New Password'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control mt-2', 'placeholder': 'Confirm New Password'})

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("new_password1")
        password2 = cleaned_data.get("new_password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")